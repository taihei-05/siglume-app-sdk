"""Tests for the v0.7 capability-bundles client wrappers."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import httpx

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from siglume_api_sdk import (  # noqa: E402
    BundleListingRecord,
    BundleMember,
    SiglumeClient,
)


def envelope(data, *, trace_id: str = "trc_test", request_id: str = "req_test") -> dict[str, object]:
    return {"data": data, "meta": {"request_id": request_id, "trace_id": trace_id}, "error": None}


def _bundle_payload(
    *,
    bundle_id: str = "b-001",
    status: str = "draft",
    members: list[dict[str, object]] | None = None,
    price_value_minor: int | None = 1000,
) -> dict[str, object]:
    return {
        "bundle_id": bundle_id,
        "id": bundle_id,
        "principal_user_id": "u-001",
        "bundle_key": "shop-helper",
        "display_name": "Shop helper",
        "description": "A test bundle.",
        "category": "commerce",
        "status": status,
        "price_model": "subscription",
        "price_value_minor": price_value_minor,
        "currency": "USD",
        "jurisdiction": "US",
        "members": members or [],
        "submitted_at": None,
        "published_at": None,
        "created_at": "2026-04-21T00:00:00Z",
        "updated_at": "2026-04-21T00:00:00Z",
    }


def _build(handler) -> SiglumeClient:
    return SiglumeClient(
        api_key="sig_test",
        base_url="https://api.example.test/v1",
        transport=httpx.MockTransport(handler),
    )


def test_create_bundle_posts_payload_and_returns_typed_record() -> None:
    captured: dict[str, object] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["method"] = request.method
        captured["path"] = request.url.path
        captured["body"] = json.loads(request.content.decode("utf-8")) if request.content else {}
        return httpx.Response(201, json=envelope(_bundle_payload()))

    client = _build(handler)
    bundle = client.create_bundle(
        bundle_key="shop-helper",
        display_name="Shop helper",
        description="A test bundle.",
        category="commerce",
        price_model="subscription",
        price_value_minor=1000,
        currency="USD",
        jurisdiction="US",
    )

    assert captured["method"] == "POST"
    assert captured["path"] == "/v1/market/bundles"
    assert captured["body"]["bundle_key"] == "shop-helper"
    assert captured["body"]["price_value_minor"] == 1000
    assert isinstance(bundle, BundleListingRecord)
    assert bundle.bundle_id == "b-001"
    assert bundle.status == "draft"
    assert bundle.price_value_minor == 1000


def test_get_bundle_parses_members() -> None:
    members = [
        {
            "link_id": "lnk-1",
            "capability_listing_id": "cap-1",
            "capability_key": "k1",
            "title": "T1",
            "position": 0,
            "status": "active",
            "added_at": "2026-04-21T00:00:00Z",
        },
    ]

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.method == "GET"
        assert request.url.path == "/v1/market/bundles/b-001"
        return httpx.Response(200, json=envelope(_bundle_payload(members=members)))

    bundle = _build(handler).get_bundle("b-001")
    assert len(bundle.members) == 1
    member = bundle.members[0]
    assert isinstance(member, BundleMember)
    assert member.capability_listing_id == "cap-1"
    assert member.capability_key == "k1"


def test_list_bundles_returns_cursor_page() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/v1/market/bundles"
        params = dict(request.url.params)
        assert params["mine"] == "true"
        return httpx.Response(
            200,
            json=envelope({
                "items": [_bundle_payload(bundle_id="b-001"), _bundle_payload(bundle_id="b-002")],
                "next_cursor": None,
                "limit": 20,
                "offset": 0,
            }),
        )

    page = _build(handler).list_bundles(mine=True)
    assert len(page.items) == 2
    assert page.items[0].bundle_id == "b-001"
    assert page.next_cursor is None


def test_add_and_remove_bundle_capability_round_trip() -> None:
    calls: list[tuple[str, str]] = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append((request.method, request.url.path))
        return httpx.Response(200, json=envelope(_bundle_payload(members=[])))

    client = _build(handler)
    client.add_bundle_capability("b-001", capability_listing_id="cap-9", position=2)
    client.remove_bundle_capability("b-001", "cap-9")
    assert calls == [
        ("POST", "/v1/market/bundles/b-001/capabilities"),
        ("DELETE", "/v1/market/bundles/b-001/capabilities/cap-9"),
    ]


def test_submit_bundle_for_review_returns_pending_review() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.method == "POST"
        assert request.url.path == "/v1/market/bundles/b-001/submit-review"
        return httpx.Response(
            200,
            json=envelope(_bundle_payload(status="pending_review")),
        )

    bundle = _build(handler).submit_bundle_for_review("b-001")
    assert bundle.status == "pending_review"


def test_update_bundle_only_sends_provided_fields() -> None:
    captured: dict[str, object] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["body"] = json.loads(request.content.decode("utf-8")) if request.content else {}
        return httpx.Response(200, json=envelope(_bundle_payload()))

    _build(handler).update_bundle("b-001", display_name="New name", price_value_minor=2000)
    body = captured["body"]
    assert body == {"display_name": "New name", "price_value_minor": 2000}
