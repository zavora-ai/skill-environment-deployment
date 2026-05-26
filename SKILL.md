---
name: environment-deployment
description: Manage environments and deployments — inspect environments, run health checks, scale workers, promote releases, rollback, and detect configuration drift. Use when deploying services, checking environment health, scaling workers, promoting between environments, rolling back, or detecting drift.
version: "1.0.0"
license: Apache-2.0
allowed-tools: [list_environments, inspect_environment, sync_environment, run_checks, scale_workers, promote_release, rollback_release, audit_trail, detect_drift, worker_status]
tags: [infrastructure, deployment, environments, scaling, promotion]
metadata:
  author: Zavora AI
  mcp-server: mcp-environment
  success-criteria:
    trigger-rate: "90% on deployment/environment queries"
    safe-deploys: "Always run checks before promoting"
---

# Environment & Deployment Management

You manage environments safely. Always run health checks before promoting, detect drift proactively, and maintain rollback capability.

## Decision Tree
```
├── "deploy", "promote", "release"? → promote_release (after run_checks)
├── "health", "status", "check"? → inspect_environment / run_checks
├── "scale", "workers", "capacity"? → scale_workers / worker_status
├── "rollback", "revert"? → rollback_release
├── "drift", "out of sync"? → detect_drift / sync_environment
├── "audit", "who deployed"? → audit_trail
```

## Key Workflows

### Safe Promotion (3 calls)
1. `run_checks(env: "staging")` → verify health
2. `promote_release(from: "staging", to: "production", version: "v2.3.1")`
3. `run_checks(env: "production")` → verify post-deploy health

### Rollback (2 calls)
1. `rollback_release(env: "production", to_version: "v2.3.0")`
2. `run_checks(env: "production")` → verify rollback succeeded

## MUST DO
- Run health checks before AND after promotion
- Never promote directly to production without staging verification
- Maintain rollback capability for every deployment
- Detect and resolve drift before promoting

## MUST NOT DO
- Never deploy without health checks
- Don't scale to zero without explicit confirmation
- Don't promote with detected drift (resolve first)
