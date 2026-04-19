from __future__ import annotations

from typing import Any, Mapping

from .client import SiglumeClient


def score_tool_manual_remote(
    tool_manual: Mapping[str, Any],
    *,
    api_key: str,
    base_url: str | None = None,
) -> Any:
    """Fetch the authoritative ToolManual quality report from the platform."""
    with SiglumeClient(api_key=api_key, base_url=base_url) as client:
        return client.preview_quality_score(tool_manual)
