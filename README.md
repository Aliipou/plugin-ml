# plugin-ml

Risk-scoring advisor for the Decision OS / AuthGate stack.

> Part of the Decision OS — governed by the Legitimacy ⊥ Authority pipeline
> (FDK legitimacy → AuthGate authority). Plugins are advisory only and hold
> **no authority**; the kernel remains the single authority.

**Status: reference (real, working) — advisory only.**

## What it advises

`risk_advisor(action, signals)` returns a threat class (`"malicious"`,
`"suspicious"`, or `None`) from cheap signals. It plugs into the kernel via
`decide(action, advisor=risk_advisor)`. The shipped scorer is a small, transparent
weighted heuristic; swap it for a real model and the contract is unchanged.

## Authority

This plugin holds **no authority**. By construction it can only return a threat
class the kernel *may* act on — it can never emit ALLOW/DENY, and it cannot invent
a verdict from no signals (see `test_advisor_is_restriction_only_and_bounded`).

## Install

```bash
pip install "decision-os-min @ git+https://github.com/Aliipou/decision-os-min.git"
pip install -e . --no-deps
pytest -q          # AUTHGATE_BACKEND=python
```

## Usage

```python
from dos_plugin_ml import risk_advisor
risk_advisor({}, ["known_bad_actor"])     # -> "malicious"
risk_advisor({}, [])                        # -> None
```

## Status and limitations

- The built-in scorer is a **heuristic placeholder**, not a trained model — its
  weights are illustrative. Real detection quality requires a real model.
- Advisory output only. The kernel remains the single authority.
