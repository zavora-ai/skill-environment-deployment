# Environment & Deployment Skill

> Safe deployment operations — health checks, promotion gates, rollback, drift detection, and worker scaling across dev/staging/production.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Calls | Achieves |
|----------|-------|----------|
| Safe Promotion | 3 | Check → promote → verify |
| Rollback | 2 | Revert → verify health |
| Drift Detection | 1-2 | Find config mismatches |
| Scale | 1 | Adjust worker capacity |

### Without this skill:
- Deploys without health checks
- No rollback plan
- Config drift undetected
- Production promoted without staging verification

### With this skill:
- Health checked before AND after promotion
- Rollback always available
- Drift detected proactively
- Staging must be healthy before production

## Installation

```bash
git clone https://github.com/zavora-ai/skill-environment-deployment.git \
  ~/.skills/skills/environment-deployment
```

## Requirements

**Required:** `mcp-environment (10 tools)`

**Cross-MCP:** mcp-cicd (CI verification), mcp-itsm (rollback on incidents), mcp-slack (deploy notifications)

## Folder Structure

```
environment-deployment/
├── SKILL.md                       # Decision tree + workflows + MUST DO/MUST NOT DO
├── scripts/
│   └── deploy_readiness.py
├── references/
│   ├── tool-sequences.md
│   ├── cross-mcp-workflows.md
│   └── examples.md
├── README.md
└── LICENSE
```

## Example

**User:** "Is production ready for v2.3.1?"

**Result:**
```
Deploy Readiness Check:
✅ CI passes (run_200)
✅ Staging healthy
✅ No drift detected
❌ Approval pending (@eng_lead)
→ Not ready: needs approval
```

## Scripts

### `deploy_readiness.py`
```bash
python scripts/deploy_readiness.py '{"ci_status": "success", "staging_health": "healthy", "drift_detected": false, "approved": false}'
```

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)
