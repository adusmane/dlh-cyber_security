Data Classification Policy

HealthPlus Medical Group

Document Control

| Field | Value |
|---|---|
| Policy ID | POL-SEC-002 |
| Version | 1.0 |
| Effective Date | 2026-08-07 |
| Review Date | 2027-08-07 |
| Policy Owner | Information Security Manager |
| Approved By | Chief Information Security Officer (CISO) |
| Classification | Internal |

---

1. Purpose

This policy establishes a framework for classifying organizational data based on its sensitivity and the potential impact of unauthorized disclosure, alteration, or destruction. It defines the handling, storage, transmission, and disposal requirements for each classification level to protect patient, employee, and business information, and to support compliance with HIPAA, GDPR, and applicable state privacy laws.

2. Scope

2.1 Applicability

This policy applies to:

- All employees, physicians, and clinical staff
- Contractors, consultants, and temporary workers
- Business associates and third-party vendors with access to company data
- Volunteers and interns

2.2 Data Covered

This policy applies to all data created, received, stored, processed, or transmitted by HealthPlus Medical Group, including:

- Patient medical records (Protected Health Information - PHI)
- Employee information (Personally Identifiable Information - PII)
- Financial data
- Research data
- Business operations data
- Public marketing materials

2.3 Exclusions

- Data that has been fully de-identified in accordance with HIPAA Safe Harbor or Expert Determination methods
- Publicly published materials with no residual sensitivity (e.g., press releases already released)

3. Compliance Requirements

This policy supports compliance with:

- HIPAA (Health Insurance Portability and Accountability Act) — Security Rule and Privacy Rule requirements for PHI
- GDPR (General Data Protection Regulation) — protections for personal data of EU data subjects, per Article 4 definitions
- State privacy laws — applicable state-level requirements for PII and breach notification

4. Classification Levels

| Level | Description | Examples |
|---|---|---|
| PUBLIC | Information approved for public release with no restriction on distribution. | Marketing brochures, public website content, press releases |
| INTERNAL | Information intended for internal use only; not confidential but not for external release. | Internal memos, organizational charts, internal policies, meeting notes |
| CONFIDENTIAL | Information that could cause harm to the organization, employees, or patients if disclosed. | Employee PII, financial data, vendor contracts, research data |
| RESTRICTED | Information that would cause severe damage — legal, financial, reputational, or patient safety harm — if disclosed. | Patient medical records (PHI), system credentials, encryption keys |

5. Handling Requirements by Classification Level

| Requirement | Public | Internal | Confidential | Restricted |
|---|---|---|---|---|
| Labeling | N | Y | Y | Y |
| Encryption at Rest | N | N | Y | Y |
| Encryption in Transit | N | Y | Y | Y |
| Access Control | Open / No restriction | Role-based (employees only) | Role-based, need-to-know | Role-based, need-to-know + MFA |

6. Labeling

6.1 Document Headers and Footers**

- INTERNAL, CONFIDENTIAL, and RESTRICTED documents must display the classification level in the header or footer of every page.
- PUBLIC materials do not require a classification label but should be reviewed for approval before release.

6.2 File Naming**

- File names for CONFIDENTIAL and RESTRICTED data must not include patient names, diagnoses, or other sensitive identifiers.
- Recommended convention: `[ClassificationLevel]_[DocumentType]_[Date]` (e.g., `RESTRICTED_PatientChart_20260807`).

6.3 Digital Metadata**

- Where supported, classification level must be applied as document metadata or a digital watermark for CONFIDENTIAL and RESTRICTED files.

7. Storage

| Level | Approved Storage Locations | Prohibited Locations |
|---|---|---|
| PUBLIC | Public website, marketing content management system | None specific |
| INTERNAL | Company intranet, approved internal shared drives | Personal cloud storage, personal devices |
| CONFIDENTIAL | Encrypted company servers, approved encrypted cloud storage | Personal email, personal devices, unencrypted USB drives |
| RESTRICTED | Encrypted electronic health record (EHR) systems, encrypted and access-logged servers | Personal devices, personal cloud storage, unencrypted removable media, printed copies left unattended |

- CONFIDENTIAL and RESTRICTED data must never be stored on personal devices or personal cloud accounts.
- RESTRICTED data storage systems must maintain access logs sufficient to support HIPAA audit requirements.

8. Transmission

8.1 Email**

- PUBLIC and INTERNAL data may be sent via standard company email.
- CONFIDENTIAL and RESTRICTED data must only be sent via encrypted email or a secure messaging platform approved by IT Security; PHI must never be sent via unencrypted email, including to external recipients.

8.2 File Transfer**

- CONFIDENTIAL and RESTRICTED data must be transferred only through approved secure file transfer methods (e.g., encrypted SFTP, approved secure portals).
- Faxing of RESTRICTED data (e.g., PHI) must use approved secure fax lines and follow HIPAA transmission safeguards.

8.3 External Sharing**

- Sharing CONFIDENTIAL or RESTRICTED data with external parties (including business associates) requires a signed data-sharing or Business Associate Agreement (BAA) prior to transmission.

9. Disposal

| Level | Paper Disposal | Electronic Media Disposal |
|---|---|---|
| PUBLIC | Standard recycling | Standard deletion |
| INTERNAL | Shredding recommended | Standard deletion |
| CONFIDENTIAL | Cross-cut shredding required | Secure wipe per NIST SP 800-88 |
| RESTRICTED | Cross-cut shredding or incineration, with disposal logged | Certified media sanitization/destruction per NIST SP 800-88, with certificate of destruction retained |

- Devices and media that stored RESTRICTED or CONFIDENTIAL data must be sanitized or physically destroyed before reuse, resale, or disposal.
- Disposal of RESTRICTED data must be documented to support HIPAA accountability requirements.

10. Access Control

| Level | Who May Access | How Access Is Granted | Access Reviews |
|---|---|---|---|
| PUBLIC | Anyone | No restriction | Not required |
| INTERNAL | All employees | Default access upon hire | Annual |
| CONFIDENTIAL | Employees with a business need | Manager approval, role-based access | Semi-annual |
| RESTRICTED | Employees with a documented need-to-know (e.g., treating clinicians, billing staff) | Manager and Information Security approval; multi-factor authentication (MFA) required | Quarterly |

- All access to RESTRICTED data must be logged, and logs must be retained in accordance with HIPAA requirements.
- Access must be revoked immediately upon role change or termination.
- Minimum necessary standard applies to all access to PHI, per HIPAA.

11. Roles and Responsibilities

| Role | Responsibilities |
|---|---|
| Executive Management | Approve policy, allocate resources, ensure organizational compliance. |
| Information Security Team | Maintain classification standards, enforce encryption and access controls, monitor compliance, investigate incidents. |
| Privacy Officer / Compliance | Oversee HIPAA and GDPR compliance, manage breach notification obligations, review exceptions involving PHI. |
| Department Managers | Ensure staff classify and handle data correctly within their department. |
| Data Owners | Assign the correct classification level to data they are responsible for and approve access requests. |
| All Employees | Classify, label, and handle data according to this policy; report suspected mishandling or breaches immediately. |
| IT/System Administrators | Implement technical controls (encryption, access restrictions, logging) and manage secure disposal of media. |

12. Compliance and Monitoring

- Compliance will be monitored through access log reviews, periodic audits, and data loss prevention (DLP) tooling where deployed.
- Department-level classification practices will be reviewed annually as part of the internal audit program.
- Suspected violations or data breaches must be reported immediately to the Information Security Team and the Privacy Officer, consistent with HIPAA breach notification timelines.

13. Enforcement

Violations of this policy may result in:

- Verbal or written warning
- Mandatory retraining on data classification and privacy requirements
- Temporary or permanent suspension of system access
- Disciplinary action up to and including termination
- Legal or regulatory action where applicable (including HIPAA/GDPR penalties)

14. Exceptions

- Exceptions require a written request to the Information Security Manager, including business justification and a risk assessment.
- Any exception involving PHI must also be reviewed and approved by the Privacy Officer.
- All exceptions must have a defined expiration date and be reviewed annually.

15. Definitions

| Term | Definition |
|---|---|
| PHI (Protected Health Information) | Individually identifiable health information protected under HIPAA. |
| PII (Personally Identifiable Information) | Information that can be used to identify a specific individual. |
| Data Owner | The individual or department accountable for the accuracy, classification, and protection of a given dataset. |
| Encryption at Rest | Encryption applied to data while it is stored on a device or system. |
| Encryption in Transit | Encryption applied to data while it is being transmitted between systems. |
| Minimum Necessary Standard | HIPAA principle requiring access to PHI be limited to the minimum needed to accomplish an intended purpose. |
| Sanitization | The process of removing data from media such that it cannot be recovered, per NIST SP 800-88. |

16. Related Documents

- Information Security Policy
- Access Control Policy
- Password Policy
- Incident Response Procedure
- Acceptable Use Policy
- NIST SP 800-60: Guide for Mapping Types of Information and Information Systems to Security Categories
- NIST SP 800-88: Guidelines for Media Sanitization
- HIPAA Security Rule
- GDPR Article 4 (Definitions of Personal Data)

17. Revision History

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0 | 2026-08-07 | Information Security Manager | Initial release |

18. Acknowledgment

By accessing HealthPlus Medical Group systems and data, all users acknowledge that they have read, understood, and agree to comply with this Data Classification Policy, and that mishandling classified data — particularly PHI — may result in disciplinary action and legal consequences.

End of Policy Document




Data Classification Quick Reference Guide


HealthPlus Medical Group — For All Employees

Classification Levels at a Glance

| Level | What It Means | Examples |
|---|---|---|
| 🟢 **PUBLIC** | Safe for anyone to see | Marketing materials, public website content |
| 🔵 **INTERNAL** | Company use only | Memos, org charts, internal policies |
| 🟠 **CONFIDENTIAL** | Could cause harm if leaked | Employee PII, financials, research data |
| 🔴 **RESTRICTED** | Could cause severe harm if leaked | Patient records (PHI), passwords/credentials |

## What You Must Do by Level

| Action | Public | Internal | Confidential | Restricted |
|---|---|---|---|---|
| Label it | No | Yes | Yes | Yes |
| Encrypt when stored | No | No | Yes | Yes |
| Encrypt when sent | No | Yes | Yes | Yes |
| Who can access it | Anyone | All employees | Need-to-know only | Need-to-know only + MFA |

Quick Rules

- Storage: Never store CONFIDENTIAL or RESTRICTED data on personal devices, personal email, or personal cloud accounts.
- Email: CONFIDENTIAL and RESTRICTED data must be sent only through approved encrypted email or secure file transfer. Never email PHI unencrypted.
- Disposal: Shred CONFIDENTIAL/RESTRICTED paper documents (cross-cut). Electronic devices with CONFIDENTIAL/RESTRICTED data must be securely wiped or destroyed — never just deleted.
- Access: Only access patient or employee data you need for your job (the "minimum necessary" rule).
- When unsure: If you're not sure how to classify something, treat it as CONFIDENTIAL until your manager or Information Security confirms.

If You Suspect a Problem

Report immediately to:

- IT Help Desk
- Information Security Team
- Privacy Officer (for anything involving patient information)

Remember: Mishandling patient information (PHI) can violate HIPAA and result in serious consequences for the company and for you personally.
