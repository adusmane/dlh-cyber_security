# Mitigation Strategies: Defense-in-Depth Plan

## Scenario
SecureBank must protect its online banking platform from **SQL injection (SQLi)** attacks.
**Budget:** $100,000 | **Timeline:** 90 days

*Note: Costs are planning estimates. Validate them with vendor quotes.*

## Defense-in-Depth Strategy

| Layer | Control | Type | Cost | Priority |
|---|---|---|---|---|
| Network | Managed Web Application Firewall (WAF) with SQLi rule sets, rate limiting, and virtual patching for known vulnerable endpoints | Tech | $18,000 | High |
| Host | Database server hardening (CIS benchmarks), patching, disabling unused features such as `xp_cmdshell`, and EDR on web and DB servers | Tech | $12,000 | Medium |
| Application | Parameterized queries/prepared statements, ORM adoption, server-side input validation, secure error handling, and SAST/DAST in the CI/CD pipeline | Tech | $30,000 | **Critical** |
| Data | Least-privilege DB accounts (no admin rights for the app), field-level encryption of sensitive data, database activity monitoring (DAM), and SIEM alerting on anomalous queries | Tech | $20,000 | High |
| Administrative | Secure coding training for developers, code review policy, incident response playbook for SQLi, and an external penetration test | Admin | $15,000 | High |
| **TOTAL** | | | **$95,000** | |

**Budget remaining:** $5,000 held as contingency (5%) for retesting or unexpected licensing costs.

**Notes on layer choices:**
- **Physical controls** are not a primary SQLi defense, so the plan relies on technical and administrative controls. Existing data center physical security is assumed adequate.
- **Application is the top priority** because SQLi is fundamentally a code flaw. Parameterized queries remove the vulnerability itself, while the other layers contain or detect attacks that get past it.
- **The WAF is a compensating control**, not a fix. It buys time while code is remediated.

## Implementation Timeline

| Week | Action |
|---|---|
| 1-2 | **Quick wins and visibility.** Deploy the WAF in detection mode, then move to blocking after tuning. Run a vulnerability scan (DAST) to identify injectable endpoints. Reduce DB account privileges. Start the DB hardening baseline. Kick off vendor procurement. |
| 3-6 | **Fix the root cause.** Refactor vulnerable code to parameterized queries, starting with login, payments, and account-search endpoints. Integrate SAST/DAST into CI/CD. Complete host hardening and EDR rollout. Run developer secure coding training. Enable DB activity monitoring and SIEM rules. |
| 7-12 | **Validate and sustain.** Deploy field-level encryption for sensitive data. Complete remaining code remediation. Conduct an external penetration test and fix findings. Finalize and tabletop-test the incident response playbook. Retest, tune the WAF, and hand over to operations. |

## Success Metric

**Zero exploitable SQL injection vulnerabilities** in the final external penetration test and DAST scan (no critical or high SQLi findings), with:
- **100%** of database queries in critical endpoints using parameterized queries
- **100%** of developers trained in secure coding
- WAF and DAM alerts reviewed within **24 hours**

## Summary

This plan uses **five layers** so no single failure exposes the platform. The WAF blocks known attack patterns, hardened hosts and least-privilege accounts limit damage, secure code removes the vulnerability, and encryption and monitoring protect and watch the data. Training and testing keep the fix in place over time. Total spend is **$95,000**, within the $100,000 budget and the 90-day timeline.
