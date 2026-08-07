# Security Policy Assignment

## Part A: Identify Missing Components

| Missing Component | Why It's Important |
|---|---|
| Header information (Policy ID, Version, Effective Date, Review Date, Owner, Approval) | Provides document control, accountability, and ensures users know which version is current and who is responsible for maintaining the policy. |
| Purpose Statement | Explains why the policy exists, what security problem it addresses, and what objectives it aims to achieve. |
| Scope Definition | Defines who must follow the policy, which systems are covered, and any exclusions. Without scope, users may not know whether the policy applies to them. |
| Specific Policy Statements | The policy only gives general advice. Clear requirements are needed to define exactly what users must do. |
| Roles and Responsibilities | Identifies who is responsible for implementing, managing, monitoring, and following the policy. |
| Enforcement Section | Defines consequences for violations and ensures the policy is taken seriously. |
| Definitions | Provides explanations for security terms such as password, MFA, privileged account, and credential. This avoids misunderstandings. |
| Related Documents | Links the policy to standards, procedures, guidelines, and security frameworks for additional guidance. |
| Review/Revision History | Tracks changes over time and ensures the policy remains updated and relevant. |
| Compliance and Monitoring Requirements | Defines how compliance will be checked, measured, and reported. |
| Exception Process | Explains how users can request exceptions and ensures risks are reviewed before approval. |
| Acknowledgment Section | Confirms that employees have read and accepted their responsibilities under the policy. |

## Part B: Identify Weaknesses

| Quote from Policy | What's Wrong | Why It Matters |
|---|---|---|
| "All employees should use good passwords." | "Good passwords" is vague and does not define requirements. | Employees may create weak passwords because there are no measurable rules such as length, complexity, or uniqueness requirements. |
| "Don't share them." | The statement is too simple and does not explain acceptable credential handling. | Users need guidance about password storage, password managers, phishing attempts, and account security. |
| "IT will handle security stuff." | Responsibilities are unclear and incorrectly place all security responsibility on IT. | Security is a shared responsibility between employees, managers, and IT teams. |
| "Report problems to someone." | The reporting process is undefined. | Employees do not know who to contact, how quickly to report issues, or what incidents require reporting. |
| "Updated: Sometime last year" | The date is inaccurate and unprofessional. | Policies require precise version control and review dates to ensure they remain current. |
| Entire policy lacks enforcement requirements | No consequences are described for non-compliance. | Employees may ignore requirements because violations have no defined impact. |
| No mention of multi-factor authentication (MFA) | Modern authentication controls are missing. | Passwords alone are insufficient protection against credential theft. |
| No password change/reset procedures | No instructions exist for compromised or forgotten passwords. | Users may continue using exposed credentials or create insecure recovery methods. |

## Part C: Password Policy

# Password Policy

### Document Control

| Field | Value |
|---|---|
| Policy ID | POL-SEC-001 |
| Version | 1.0 |
| Effective Date | 2026-08-07 |
| Review Date | 2027-08-07 |
| Policy Owner | Information Security Manager |
| Approved By | Chief Information Security Officer (CISO) |
| Classification | Internal |

### 1. Purpose

This policy establishes password management requirements to protect organizational systems, applications, and sensitive information from unauthorized access.

The objective of this policy is to ensure that all users create, manage, and protect strong passwords and authentication credentials according to security best practices.

### 2. Scope

**2.1 Applicability**

This policy applies to:

- All employees
- Contractors and consultants
- Third-party vendors with authorized access
- Temporary workers and interns

**2.2 Systems/Assets Covered**

This policy applies to:

- Corporate computers and laptops
- Email accounts
- Internal applications
- Cloud services
- Network systems
- Databases
- Administrative and privileged accounts

**2.3 Exclusions**

The following are excluded:

- Publicly accessible systems requiring no authentication
- Test environments without access to company data

### 3. Policy Statements

**3.1 Password Creation Requirements**

All users must create passwords that meet minimum security requirements.

Requirements:

- Passwords must contain a minimum of 12 characters.
- Passwords must not contain easily guessed information such as names, birthdays, or company information.
- Passwords must not be reused across multiple company systems.
- Passwords must contain a combination of letters, numbers, and special characters where technically supported.
- Users must use passphrases whenever possible.

**3.2 Password Protection and Management**

Users are responsible for protecting their authentication credentials.

Requirements:

- Passwords must never be shared with other individuals.
- Users must not write passwords on visible locations such as sticky notes.
- Passwords must not be stored in unsecured files or documents.
- Approved password managers should be used for storing credentials.
- Users must immediately report suspected password compromise.

**3.3 Multi-Factor Authentication and Password Changes**

Additional authentication controls must be used to reduce unauthorized access risks.

Requirements:

- Multi-factor authentication (MFA) must be enabled for privileged accounts and sensitive systems.
- Users must change passwords immediately if compromise is suspected.
- Default passwords provided by vendors must be changed before systems are placed into production.
- Privileged accounts must follow stricter password requirements defined by IT Security standards.

### 4. Roles and Responsibilities

| Role | Responsibilities |
|---|---|
| Executive Management | Approve policy, provide resources, and support security initiatives. |
| IT Security Team | Implement password controls, enforce MFA requirements, monitor compliance, and investigate violations. |
| Department Managers | Ensure employees follow password requirements and support security awareness activities. |
| All Employees | Create secure passwords, protect credentials, report incidents, and complete security training. |
| System Administrators | Configure authentication systems, remove default credentials, and maintain access controls. |

### 5. Compliance

**5.1 Monitoring**

The IT Security Team will monitor compliance through:

- Password policy enforcement tools.
- Authentication logs.
- Security audits.
- Access reviews.

**5.2 Reporting**

Security incidents involving passwords must be reported immediately to:

- IT Help Desk
- Information Security Team
- Security Incident Response Team

**5.3 Auditing**

Password controls will be reviewed annually through security audits to verify compliance with this policy.

### 6. Enforcement

**6.1 Violations**

Violations of this policy may result in:

- Verbal warning
- Mandatory security training
- Written warning
- Temporary suspension of system access
- Disciplinary action up to and including termination
- Legal action where applicable

**6.2 Reporting Violations**

Suspected violations must be reported through:

- Company IT Help Desk
- Security incident reporting system
- Information Security Manager

### 7. Exceptions

**7.1 Exception Process**

Exceptions to this policy require:

- Written request submitted to the Information Security Manager.
- Business justification explaining the need.
- Security risk assessment.
- Implementation of compensating controls if required.
- Formal approval and documentation.

**7.2 Exception Duration**

All approved exceptions must have:

- A defined expiration date.
- Annual review by the Security Team.
- Documentation of continued business justification.

### 8. Definitions

| Term | Definition |
|---|---|
| Password | A secret authentication value used to verify a user's identity. |
| Multi-Factor Authentication (MFA) | Authentication method requiring two or more verification factors. |
| Privileged Account | An account with elevated permissions that can modify systems or security settings. |
| Credential | Information used to authenticate a user, such as passwords or authentication tokens. |

### 9. Related Documents

- Information Security Policy
- Access Control Policy
- Acceptable Use Policy
- Incident Response Procedure
- Security Awareness Training Procedure
- NIST SP 800-63B Digital Identity Guidelines

### 10. Revision History

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0 | 2026-08-07 | Information Security Manager | Initial release |

### 11. Acknowledgment

By accessing company systems, all users acknowledge that they have read, understood, and agree to comply with this Password Policy.

Users are responsible for protecting their credentials and reporting suspected security incidents immediately.

For formal acknowledgment tracking, use the company's policy acknowledgment system.

*End of Policy Document*
