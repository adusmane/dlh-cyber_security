## SecureBank Online Banking: Risk Register

| ID | Asset (Category) | Threat (Category) | Vulnerability | Risk Statement |
|---|---|---|---|---|
| R1 | Customer PII and account data for 50,000 customers (Information) | Attacker using phished or stolen credentials (Adversarial) | No mandatory multi-factor authentication and a weak password policy | "The attacker using stolen credentials exploiting missing MFA in customer account data could cause unauthorized access, fraudulent transfers, a data breach and regulatory penalties." |
| R2 | Online banking web application (Software) | External attacker running injection and web-application attacks (Adversarial) | Insufficient input validation and unpatched third-party libraries | "The external attacker exploiting unvalidated input and unpatched libraries in the online banking application could cause exposure or alteration of customer records, service compromise and loss of customer trust." |
| R3 | Database and system administrators (People) | Administrator error or misconfiguration (Accidental) | Excessive privileges, no formal change management, no peer review of production changes | "The administrator error exploiting excessive privileges and weak change control in the production environment could cause data loss, exposed databases or an unplanned outage of the banking platform." |
| R4 | Primary data center servers and network equipment (Hardware) | Fire, flood or extended power failure (Environmental) | Single data center site, no geographic redundancy and an untested disaster recovery plan | "The fire or power failure exploiting the single-site hosting and untested DR plan in the primary data center could cause a prolonged outage, failure to meet recovery objectives and financial and regulatory consequences." |
| R5 | Third-party payment processing and cloud hosting service (Services) | Provider outage or failure (Structural) | Single-provider dependency, no failover arrangement and weak SLA terms | "The provider outage exploiting single-vendor dependency and weak SLAs in the payment processing service could cause customers to be unable to transact, missed settlements and reputational damage." |

### Coverage check

- **Asset categories:** Information (R1), Software (R2), People (R3), Hardware (R4), Services (R5)
- **Threat categories:** Adversarial (R1, R2), Accidental (R3), Environmental (R4), Structural (R5)
