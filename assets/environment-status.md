# 🌍 Environment Status

**Generated:** {timestamp}
**Environment:** {environment_name}
**Stage:** {stage}

## Services

| Service | Version | Status | Replicas |
|---------|---------|--------|----------|
| {service_1} | {ver_1} | {status_1} | {replicas_1} |
| {service_2} | {ver_2} | {status_2} | {replicas_2} |
| {service_3} | {ver_3} | {status_3} | {replicas_3} |

## Health

| Metric | Value |
|--------|-------|
| Uptime | {uptime} |
| Last Deploy | {last_deploy} |
| Config Version | {config_version} |
| Healthy Services | {healthy_count}/{total_services} |

## Status Legend

- ✅ Healthy — All checks passing
- ⚠️ Degraded — Partial availability
- ❌ Down — Service unavailable
- 🔄 Deploying — Rollout in progress

---
*Managed by {agent_name} • Region: {region}*
