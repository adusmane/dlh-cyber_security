# Risk Assessment Methodologies: FAIR Analysis

## Scenario
GlobalTech faces a data breach risk: **misconfigured cloud storage exposing 50,000 customer records.**

*Note: The inputs below are my reasoned estimates, since the scenario provides no historical data. In a real assessment, calibrate them against incident logs, scan data, and industry benchmarks.*

## Completed FAIR Analysis

| FAIR Component | Your Estimate | Reasoning |
|---|---|---|
| Threat Event Frequency (events/year) | **4** | Automated scanners and opportunistic actors continuously probe for exposed cloud storage. Discovery attempts happen far more often than 4 times a year, but only a fraction reach the specific misconfigured resource and attempt access. A conservative estimate of about one credible access attempt per quarter is used. |
| Vulnerability (0-1 probability) | **0.5** | A publicly exposed bucket requires no exploit, so a capable attacker who finds it is likely to succeed. The estimate is held at 0.5 rather than higher because the exposure may be partly mitigated by obscure naming, monitoring that catches access early, or data that is not fully readable. |
| Loss Event Frequency (TEF × Vuln) | **2 events/year** | 4 × 0.5 |

| Loss Category | Estimated Cost |
|---|---|
| Response & Investigation | **$150,000** |
| Notification costs ($5/record) | **$250,000** |
| Regulatory fines | **$500,000** |
| Reputation damage | **$400,000** |
| **Total Loss Magnitude** | **$1,300,000** |

**Loss category reasoning:**
- **Response & Investigation ($150,000):** Forensic firm, legal counsel, incident response staff time, and remediation of the misconfiguration.
- **Notification ($250,000):** 50,000 records × $5 = $250,000, using the given rate.
- **Regulatory fines ($500,000):** Assumes personal data of EU or US residents falls under GDPR or state breach laws. GDPR fines can reach 4% of global turnover, but real fines for a single misconfiguration of this size are typically far below the maximum, so a mid-range figure is used.
- **Reputation damage ($400,000):** Customer churn, lost sales, and credit monitoring or goodwill offers, roughly $8 per affected record.

| Final Calculation | Value |
|---|---|
| LEF × LM = Annualized Risk | 2 × $1,300,000 = **$2,600,000 per year** |

## Risk Treatment Recommendation

**Mitigate immediately.** An annualized risk of $2.6M is well above the level most organizations would accept, so accepting the risk is not appropriate.

1. **Fix the root cause now.** Set the storage to private, enforce block-public-access at the account level, and review access logs to check whether the data has already been accessed.
2. **Prevent recurrence.** Deploy cloud security posture management (CSPM) with automated alerts on public exposure, and use infrastructure-as-code policy checks so misconfigurations are blocked before deployment.
3. **Reduce impact.** Encrypt data at rest, minimize what is stored (delete records that are no longer needed), and tokenize sensitive fields so any exposure is less damaging.
4. **Transfer residual risk.** Maintain cyber insurance to cover response and notification costs.
5. **Re-run the analysis after remediation.** If the controls drop Vulnerability to about 0.05 and TEF stays at 4, LEF falls to 0.2 and annualized risk falls to $260,000, a 90% reduction that would justify substantial control spend.

**Sensitivity note:** The result is most sensitive to Vulnerability and TEF. A more conservative TEF of 1 with Vulnerability of 0.3 gives an LEF of 0.3 and an annualized risk of $390,000, which would still justify mitigation.
