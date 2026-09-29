# Risk Fundamentals: Risk Assessment for TechCorp

## Scenario
**Risk:** SQL injection vulnerability in customer database
- Asset Value (AV): $2,000,000 (customer records)
- Exposure Factor (EF): 40%
- Annual Rate of Occurrence (ARO): 0.3

## Calculations

**SLE (Single Loss Expectancy)** = Asset Value × Exposure Factor
SLE = $2,000,000 × 0.40 = **$800,000**

**ALE (Annualized Loss Expectancy)** = SLE × ARO
ALE = $800,000 × 0.3 = **$240,000**

## Completed Risk Assessment Table

| Component | Your Answer |
|---|---|
| Threat | External attacker (or malicious insider) exploiting the SQL injection flaw to read, modify, or exfiltrate customer records |
| Vulnerability | Unsanitized user input reaching database queries (no parameterized queries or input validation) in the customer database application |
| Likelihood (Low/Medium/High) | **Medium** |
| Impact (Low/Medium/High) | **High** |
| Risk Level (use matrix) | **High** |
| SLE (Asset × EF) | **$800,000** |
| ALE (SLE × ARO) | **$240,000** |
| Treatment (Mitigate/Transfer/Accept/Avoid) | **Mitigate** |

## Reasoning

**Likelihood: Medium.** An ARO of 0.3 means the event is expected roughly once every 3.3 years (a 30% chance per year). That is not rare, but it is not expected every year, so Medium fits. SQL injection is also a well-known, heavily automated attack, which supports not rating it Low.

**Impact: High.** A single loss of $800,000 is 40% of the asset's value, and the exposure involves customer records, which brings regulatory, legal, and reputational consequences beyond the direct cost.

**Risk Level: High.** Using the matrix, the Medium Likelihood row and High Impact column intersect at **High**.

| | Low Impact | Medium | High |
|---|---|---|---|
| High Likelihood | Medium | High | Critical |
| **Medium Likelihood** | Low | Medium | **High** ← |
| Low Likelihood | Low | Low | Medium |

## Treatment: Mitigate

Mitigation is the right choice for these reasons:
- **Avoid** is impractical, since the database is needed for business operations.
- **Accept** is not appropriate for a High risk with a $240,000 annual expected loss.
- **Transfer** (cyber insurance) can cover part of the financial loss but does not fix the flaw or the reputational and regulatory fallout.
- **Mitigate** removes the root cause at a cost that is small relative to the exposure.

**Recommended controls:**
1. Replace dynamic SQL with parameterized queries or prepared statements.
2. Add server-side input validation.
3. Deploy a web application firewall (WAF) as a compensating control.
4. Apply least-privilege database accounts and monitor database activity.
5. Add SAST/DAST scanning to the development pipeline.

**Cost justification:** Any mitigation costing well under $240,000 per year is cost-effective. If the controls reduce risk by 75%, the new ALE would be $60,000, saving $180,000 per year. Residual risk (any remaining likelihood after controls) should be accepted formally by management once it falls to an acceptable level.
