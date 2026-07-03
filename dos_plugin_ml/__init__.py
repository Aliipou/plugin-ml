"""ML/heuristic risk advisor — a real advisor plugin.

Plugs into `decision_os_min` via `decide(action, advisor=risk_advisor)`. It is
ADVISORY ONLY by construction: it returns a threat class the kernel MAY act on; it
can never emit ALLOW/DENY. Swap the scorer for a real model; the contract holds.
"""

from __future__ import annotations

from typing import Any

_WEIGHTS = {"known_bad_actor": 0.9, "capability_probing": 0.4, "off_purpose": 0.4}


def risk_advisor(action: dict[str, Any], signals: list[str] | None = None) -> str | None:
    """Return 'malicious' / 'suspicious' / None from cheap signals. Advisory only."""
    signals = signals or action.get("_signals", [])
    score = min(1.0, sum(_WEIGHTS.get(s, 0.05) for s in signals))
    if score >= 0.8:
        return "malicious"
    if score >= 0.4:
        return "suspicious"
    return None
