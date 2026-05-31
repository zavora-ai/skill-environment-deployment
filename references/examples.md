# Environment Deployment Examples

## Example 1: "Promote staging to production"
```
detect_drift(env: "staging") → {drifted: false, in_sync: true}
run_checks(env: "staging") → {healthy: true, checks: [{name: "api", status: "pass"}, {name: "worker", status: "pass"}, {name: "db", status: "pass"}]}
promote_release(from: "staging", to: "production", version: "v3.1.0") → {promoted: true, deployment_id: "dep-781"}
run_checks(env: "production") → {healthy: true, checks: [{name: "api", status: "pass"}, {name: "worker", status: "pass"}, {name: "db", status: "pass"}]}
```
Response: "✅ Promoted v3.1.0 to production (dep-781). Pre-checks: all pass. Post-checks: all pass. No drift detected. 3/3 services healthy."

## Example 2: "Production is down — rollback immediately"
```
inspect_environment(env: "production") → {version: "v3.1.0", services: [{name: "api", status: "unhealthy", error: "OOM killed"}], deployed_at: "10min ago", deployed_by: "ci-bot"}
rollback_release(env: "production", to_version: "v3.0.9") → {rolled_back: true, from: "v3.1.0", to: "v3.0.9", duration: "45s"}
run_checks(env: "production") → {healthy: true, checks: [{name: "api", status: "pass"}]}
audit_trail(env: "production", limit: 2) → [{version: "v3.1.0", actor: "ci-bot", time: "10min ago"}, {version: "v3.0.9", actor: "rollback", time: "now"}]
```
Response: "🔄 Rolled back production: v3.1.0 → v3.0.9 in 45s. API was OOM-killed after deploy 10min ago. Post-rollback health: all pass. Investigate memory regression in v3.1.0."

## Example 3: "Scale up workers for the batch job tonight"
```
worker_status(env: "production") → {workers: 4, cpu_avg: 72%, memory_avg: 68%, queue_depth: 1200}
scale_workers(env: "production", count: 8) → {scaled: true, from: 4, to: 8}
worker_status(env: "production") → {workers: 8, cpu_avg: 38%, memory_avg: 35%, queue_depth: 1200}
```
Response: "⬆️ Scaled production workers: 4 → 8. CPU dropped from 72% to 38%. Queue depth: 1,200 jobs — should clear faster now. Remember to scale back down after the batch completes."
