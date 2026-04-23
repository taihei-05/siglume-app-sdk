from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import contract_sync  # noqa: E402


def test_docs_and_contracts_are_in_sync() -> None:
    issues = contract_sync.run_contract_sync(ROOT)
    assert not issues, "\n".join(str(issue) for issue in issues)


def test_openapi_keeps_connected_account_oauth_routes_public() -> None:
    text = (ROOT / "openapi" / "developer-surface.yaml").read_text(encoding="utf-8")
    required_fragments = [
        "/me/connected-accounts/providers:",
        "/me/connected-accounts/oauth/authorize:",
        "/me/connected-accounts/oauth/callback:",
        "/me/connected-accounts/{accountId}/refresh:",
        "/me/connected-accounts/{accountId}/revoke:",
        "/market/capabilities/{listingId}/oauth-credentials:",
        "ConnectedAccountProviderListEnvelope:",
        "ConnectedAccountOAuthAuthorizeRequest:",
        "ConnectedAccountOAuthStartEnvelope:",
        "ConnectedAccountOAuthCallbackRequest:",
        "ConnectedAccountLifecycleEnvelope:",
        "ListingOAuthCredentialsStatusEnvelope:",
    ]
    for fragment in required_fragments:
        assert fragment in text, fragment
