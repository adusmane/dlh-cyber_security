## CVSS v3.1 Assessment

**Vector:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

| CVSS Metric | Your Value | Justification |
|---|---|---|
| Attack Vector | **N** (Network) | The web server is reachable remotely over the network. |
| Attack Complexity | **L** (Low) | No special conditions are needed, so the exploit works repeatably. |
| Privileges Required | **N** (None) | The vulnerability is unauthenticated. |
| User Interaction | **N** (None) | No victim action is needed. |
| Scope | **U** (Unchanged) | The impact stays within the web server's own security authority. |
| Confidentiality | **H** (High) | Code execution gives access to all data on the server. |
| Integrity | **H** (High) | The attacker can modify files, code and data. |
| Availability | **H** (High) | The attacker can crash, disable or destroy the service. |
| **CVSS Score** | **9.8** | See the calculation below. |
| **Severity** | **Critical** | The 9.0-10.0 range is Critical. |

### CVSS calculation

Metric weights: AV:N = 0.85, AC:L = 0.77, PR:N = 0.85, UI:N = 0.85, C/I/A:H = 0.56 each.

- **ISS** = 1 − [(1 − 0.56) × (1 − 0.56) × (1 − 0.56)] = 1 − 0.085 = **0.9148**
- **Impact** (Scope Unchanged) = 6.42 × ISS = 6.42 × 0.9148 = **5.873**
- **Exploitability** = 8.22 × 0.85 × 0.77 × 0.85 × 0.85 = **3.887**
- **Base Score** = Roundup(min(Impact + Exploitability, 10)) = Roundup(9.76) = **9.8**

**Scope note:** If the compromised server could be used to break out into a different security authority (for example, a hypervisor or a separate trust zone), Scope would be Changed and the score would rise to **10.0**. With no such information in the scenario, Unchanged (9.8) is the standard answer.

## Financial Metrics

| Financial Metric | Calculation | Result |
|---|---|---|
| SLE | Asset Value × EF = $500,000 × 0.80 | **$400,000** |
| ALE | SLE × ARO = $400,000 × 0.2 | **$80,000** |

## Conclusion

The vulnerability is **Critical (9.8)** with an expected annual loss of **$80,000**, so it warrants immediate remediation. Patch or apply a vendor fix, restrict network exposure with a WAF or firewall rule as a temporary control, and monitor for exploitation. Any control costing under $80,000 per year that substantially reduces the ARO is financially justified.
