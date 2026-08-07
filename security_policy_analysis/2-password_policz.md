Document Control

| Field | Value |
| ------------------ | ----------- |
| Policy ID | POL-PWD-001 |
| Version | 1.0 |
| Effective Date | 2026-08-07 |
| Review Date | 2027-08-07 |
| Policy Owner | Information Security Manager |
| Approved By | Executive Management |
| Classification | Internal |

---

1. Purpose

This Password Policy establishes requirements for creating, managing, storing, and protecting passwords used within SecureBank Financial Services systems.

The purpose of this policy is to:

- Protect customer financial information and confidential business data.
- Prevent unauthorized access to banking systems.
- Reduce risks associated with weak, reused, or compromised passwords.
- Ensure compliance with PCI-DSS, SOX, FFIEC, NIST SP 800-63B, and industry security best practices.

This policy defines minimum password security requirements for all users, systems, applications, and privileged accounts.

---

# 2. Scope

2.1 Applicability

This policy applies to:

- ☑ All employees
- ☑ Contractors and consultants
- ☑ Third-party service providers
- ☑ System administrators
- ☑ Developers
- ☑ Application service accounts
- ☑ Privileged account users

Any individual or system accessing SecureBank resources must comply with this policy.

---

2.2 Systems/Assets Covered

This policy applies to:

- Core banking systems
- Customer online banking portal
- Employee workstations
- Administrative systems
- Database systems
- Cloud services
- Development and testing environments
- Network infrastructure
- Privileged access management systems

---

2.3 Exclusions

The following are excluded unless explicitly approved:

- Temporary test accounts without security approval.
- Emergency break-glass accounts managed under separate procedures.
- Vendor accounts without documented access agreements.

---

3. Policy Statements

---

3.1 Password Requirements

All passwords must meet minimum security requirements to protect against unauthorized access.

Requirements:

All user passwords must:

- Have a minimum length of **14 characters**.
- Support passphrases containing multiple words.
- Be unique and not reused across company systems.
- Not contain easily guessed information, including:
  - Usernames.
  - Employee IDs.
  - Company names.
  - Birth dates.
  - Common words.

Passwords must not:

- Appear in known breached password databases.
- Be shared with other users.
- Be stored in plain text.
- Be written in unsecured locations.

Password Complexity:

Passwords should support:

- Uppercase letters.
- Lowercase letters.
- Numbers.
- Special characters.

However, length and resistance against password guessing attacks are prioritized over mandatory complexity rules according to NIST SP 800-63B recommendations.

---

Prohibited Passwords

The following passwords are forbidden:

| Category | Examples |
|---|---|
| Common passwords | Password123, Welcome1 |
| Previously compromised passwords | Passwords found in breach databases |
| Company-related passwords | SecureBank2026 |
| Personal information | JohnSmith1985 |
| Sequential passwords | Password1, Password2 |

---

3.2 Password Management

Passwords must be securely created, maintained, and changed according to approved procedures.

## Password Changes:

Users must change passwords when:

- A password compromise is suspected.
- Security monitoring detects suspicious activity.
- Required by regulatory or business requirements.
- An administrator performs an approved reset.

Routine password expiration is not required for normal users unless risk-based assessment requires it.

Privileged accounts must follow enhanced rotation requirements.

---

Password Reset Procedures:

Password resets must:

- Require identity verification.
- Be performed through approved company processes.
- Never be completed only through email requests.
- Generate temporary credentials that require immediate change.

Help desk personnel must follow identity verification procedures before resetting passwords.

---

Account Lockout and Protection

To prevent brute-force attacks:

- Accounts must be temporarily locked after repeated failed login attempts.
- Failed login attempts must be monitored.
- Security alerts must be generated for suspicious authentication activity.

Recommended configuration:

| Control | Requirement |
|---|---|
| Failed attempts before lockout | 5 attempts |
| Lockout duration | Minimum 15 minutes |
| Monitoring | Security Information and Event Management (SIEM) |

---

Session Timeouts

Systems must enforce automatic session termination.

Requirements:

| System Type | Timeout Requirement |
|---|---|
| Customer portal | 15 minutes inactivity |
| Administrative systems | 15 minutes inactivity |
| Employee workstations | 15 minutes inactivity |
| Critical banking systems | According to risk assessment |

---

3.3 Multi-Factor Authentication (MFA)

Multi-factor authentication is required for systems containing sensitive financial information or administrative access.

MFA Required For:

MFA must be enabled for:

- Core banking systems.
- Customer online banking portal.
- Administrative accounts.
- Remote access/VPN.
- Cloud services.
- Privileged accounts.
- Security management platforms.

---

Approved MFA Methods

Approved authentication methods include:

| Method | Approved Usage |
|---|---|
| Hardware security keys (FIDO2/WebAuthn) | Preferred for privileged users |
| Authenticator applications | Approved for employees |
| Push notification with number verification | Approved |
| Hardware OTP tokens | Approved for specific systems |
| SMS authentication | Restricted and only allowed where no stronger option exists |

---

3.4 Password Storage Requirements

Passwords must be protected throughout their lifecycle.

Requirements:

Systems storing passwords must:

- Never store passwords in plaintext.
- Use strong cryptographic hashing algorithms.
- Apply unique salts for every password.
- Protect password databases from unauthorized access.

Approved password hashing algorithms:

- Argon2id (preferred)
- bcrypt
- PBKDF2 with appropriate configuration

Weak hashing methods are prohibited:

- MD5
- SHA-1
- Unsalted SHA-256

---

Password Managers

Password managers are approved and encouraged.

Employees should:

- Use company-approved password managers.
- Store unique passwords for each service.
- Enable MFA on password manager accounts.
- Never share passwords through insecure communication channels.

Examples of approved password manager capabilities:

- Encryption of stored credentials.
- Secure password generation.
- Audit logging.
- Controlled password sharing.

---

3.5 Privileged Account Requirements

Privileged accounts require additional security controls due to their high-risk nature.

#Requirements:

Privileged accounts must:

- Use MFA.
- Use unique administrator passwords.
- Avoid shared administrator accounts.
- Be monitored and logged.
- Use separate accounts for administrative and normal activities.

Example:

| Incorrect | Correct |
|---|---|
| admin account used for daily email | Separate admin and user accounts |
| Shared administrator password | Individual privileged credentials |

---

Privileged Access Management (PAM)

SecureBank must implement a Privileged Access Management solution.

PAM requirements:

- Store privileged credentials securely.
- Automatically rotate privileged passwords.
- Record privileged sessions.
- Provide just-in-time access when possible.
- Limit administrative privileges based on least privilege.
- Generate audit logs.

---

3.6 Service and Application Accounts

Service accounts must follow additional controls.

Requirements:

- Service accounts must have unique passwords.
- Default vendor passwords must be changed immediately.
- Passwords must be stored in approved vaults.
- Access must be reviewed regularly.
- Interactive login must be disabled where possible.

---

4. Roles and Responsibilities

| Role | Responsibilities |
| ------------------------ | ---------------------------------------------------------- |
| Executive Management | Approve policy and provide resources for password security |
| Information Security Team | Define requirements, monitor compliance, manage security controls |
| IT Department | Implement authentication controls and password management systems |
| System Administrators | Protect privileged accounts and maintain secure configurations |
| Developers | Implement secure authentication mechanisms in applications |
| Employees | Create strong passwords, protect credentials, report compromised passwords |
| Compliance Team | Verify compliance with PCI-DSS, SOX, and FFIEC requirements |

---

5. Compliance

5.1 Monitoring

SecureBank may monitor:

- Authentication attempts.
- Failed login attempts.
- Password policy violations.
- Privileged account activity.
- MFA usage.

Monitoring activities support security investigations and regulatory compliance.

---

5.2 Reporting

Employees must immediately report:

- Suspected password compromise.
- Lost authentication devices.
- Unauthorized login attempts.
- Suspicious MFA requests.

Reports must be submitted to:

**Information Security Team**

---

5.3 Auditing

Password controls must be audited regularly to verify:

- Password policy compliance.
- MFA implementation.
- Privileged account protection.
- Password storage security.
- Access control effectiveness.

Audit evidence must be maintained according to regulatory requirements.

---

6. Enforcement

6.1 Violations

Violations of this policy may result in:

- Mandatory password reset.
- Removal of access privileges.
- Security awareness training.
- Disciplinary action.
- Termination of employment.
- Legal action where applicable.

Examples of violations:

- Sharing passwords.
- Using weak passwords.
- Bypassing MFA.
- Storing passwords insecurely.
- Misusing privileged accounts.

---

6.2 Reporting Violations

Suspected violations must be reported to:

Information Security Team
Security Incident Reporting System

---

7. Exceptions

7.1 Exception Process

Exceptions require:

1. Written request submitted to the Information Security Manager.
2. Business justification.
3. Security risk assessment.
4. Compensating controls.
5. Formal approval.

---

7.2 Exception Duration

Approved exceptions:

- Must have an expiration date.
- Must be reviewed annually.
- Must be documented and tracked.

---

8. Definitions

| Term | Definition |
|---|---|
| **MFA** | Multi-Factor Authentication requiring multiple verification methods |
| **PAM** | Privileged Access Management system for controlling administrator access |
| **Password Hashing** | One-way cryptographic transformation used to protect stored passwords |
| **Passphrase** | A long password made from multiple words |
| **Privileged Account** | Account with elevated administrative permissions |

---

9. Related Documents

- Information Security Policy
- Access Control Policy
- Incident Response Policy
- Data Protection Policy
- Privileged Access Management Standard
- NIST SP 800-63B Digital Identity Guidelines
- OWASP Authentication Cheat Sheet
- PCI-DSS v4.0 Requirement 8
- FFIEC Authentication Guidance

---

10. Revision History

| Version | Date | Author | Description |
| ------------ | ---------- | ------ | ---------------- |
| 1.0 | 2026-08-07 | Information Security Manager | Initial release |

---

11. Acknowledgment

By accessing SecureBank Financial Services systems, users acknowledge that they:

- Have read and understood this Password Policy.
- Agree to comply with all password security requirements.
- Understand the risks associated with weak or compromised passwords.
- Accept responsibility for protecting authentication credentials.

For formal acknowledgment tracking, users must complete the company's policy acknowledgment process.

---

End of Policy Document



Technical Standards
---

Document Control

| Field | Value |
|---|---|
| Document ID | STD-PWD-001 |
| Version | 1.0 |
| Owner | Information Security Team |
| Classification | Internal |

---

1. Password Technical Requirements

| Control | Standard |
|---|---|
| Minimum user password length | 14 characters |
| Privileged account length | 20 characters recommended |
| Password history | Prevent reuse of last 10 passwords |
| Password storage | Salted adaptive hashing |
| Approved hashing | Argon2id, bcrypt, PBKDF2 |
| MFA | Required for critical systems |
| Lockout threshold | 5 failed attempts |
| Lockout duration | 15 minutes minimum |

---

2. Authentication Standards

Systems must support:

- MFA integration.
- Strong password policies.
- Secure session management.
- Logging of authentication events.

---

3. Password Hashing Standards

Required:

- Unique salt per password.
- Strong computational cost settings.
- Secure cryptographic libraries.

Forbidden:

- Plain text storage.
- Reversible encryption.
- MD5 hashing.
- SHA-1 hashing.

---

4. Privileged Account Standards

Administrators must:

- Use PAM solutions.
- Enable MFA.
- Use individual administrator accounts.
- Avoid shared credentials.
- Rotate privileged credentials automatically.

---

5. Review Requirements

Technical password standards must be reviewed:

- Annually.
- After major security incidents.
- After regulatory changes.

---

End of Technical Standard
