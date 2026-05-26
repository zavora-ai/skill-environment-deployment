# Environment Cross-MCP Workflows

## Environment + CI/CD: Safe Promotion
```
CICD: list_pipeline_runs(branch: "main", status: "success") → CI green
ENVIRONMENT: run_checks(env: "staging") → healthy
ENVIRONMENT: promote_release(from: "staging", to: "production", version: "v2.3.1")
ENVIRONMENT: run_checks(env: "production") → verify post-deploy
SLACK: send_message(channel: "#deploys", text: "🚀 v2.3.1 promoted to production. Health: ✅")
```

## Environment + ITSM: Rollback on Incident
```
ITSM: create_ticket(priority: "critical", subject: "Production errors after deploy")
ENVIRONMENT: rollback_release(env: "production", to_version: "v2.3.0")
ENVIRONMENT: run_checks(env: "production") → healthy after rollback
ITSM: add_ticket_note(id: "INC-1001", body: "Rolled back to v2.3.0. Production stable.")
```
