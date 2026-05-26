#!/usr/bin/env python3
"""Check deployment readiness — CI, health, drift, approvals."""
import json, sys

def check(data):
    checks = {
        "ci_passes": data.get("ci_status") == "success",
        "staging_healthy": data.get("staging_health") == "healthy",
        "no_drift": not data.get("drift_detected", False),
        "approved": data.get("approved", False),
        "no_active_incidents": not data.get("active_incidents", False),
    }
    ready = all(checks.values())
    blockers = [k for k, v in checks.items() if not v]
    return {"ready": ready, "checks": checks, "blockers": blockers}

if __name__ == "__main__":
    print(json.dumps(check(json.loads(sys.argv[1])), indent=2))
