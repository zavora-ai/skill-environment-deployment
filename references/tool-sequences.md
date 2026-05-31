# Environment Deployment Tool Sequences (10 tools)

## Inspection (3)
| Tool | Purpose | Risk |
|------|---------|------|
| `list_environments` | List all environments (prod, staging, dev) | read |
| `inspect_environment` | Environment details, services, versions | read |
| `worker_status` | Worker health and capacity | read |

## Health (2)
| Tool | Purpose | Risk |
|------|---------|------|
| `run_checks` | Run health checks on environment | read |
| `detect_drift` | Detect config drift between envs | read |

## Deployment (3)
| Tool | Purpose | Risk |
|------|---------|------|
| `promote_release` | Promote release between environments | **production** |
| `rollback_release` | Revert to previous version | **production** |
| `sync_environment` | Sync drifted config to match source | **production** |

## Scaling (1)
| Tool | Purpose | Risk |
|------|---------|------|
| `scale_workers` | Scale worker count up/down | production |

## Audit (1)
| Tool | Purpose | Risk |
|------|---------|------|
| `audit_trail` | Deployment history with actors | read |

## Sequence: Safe Promotion (4 calls)
```
1. detect_drift(env: "staging") → {drifted: false, in_sync: true}
2. run_checks(env: "staging") → {healthy: true, checks: [{name: "api", status: "pass"}, {name: "db", status: "pass"}]}
3. promote_release(from: "staging", to: "production", version: "v2.5.0") → {promoted: true, deployment_id: "dep-450"}
4. run_checks(env: "production") → {healthy: true, checks: [{name: "api", status: "pass"}, {name: "db", status: "pass"}]}
```

## Sequence: Rollback on Failure (3 calls)
```
1. run_checks(env: "production") → {healthy: false, checks: [{name: "api", status: "fail", error: "connection timeout"}]}
2. rollback_release(env: "production", to_version: "v2.4.9") → {rolled_back: true, from: "v2.5.0", to: "v2.4.9"}
3. run_checks(env: "production") → {healthy: true, checks: [{name: "api", status: "pass"}]}
```

## Sequence: Detect and Fix Drift (3 calls)
```
1. detect_drift(env: "production") → {drifted: true, differences: [{key: "MAX_CONNECTIONS", expected: "100", actual: "50"}, {key: "LOG_LEVEL", expected: "warn", actual: "debug"}]}
2. sync_environment(env: "production", source: "staging") → {synced: true, changes: 2}
3. run_checks(env: "production") → {healthy: true}
```
