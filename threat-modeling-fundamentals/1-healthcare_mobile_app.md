Healthcare Mobile App  Threat Modeling

1. Most Critical Asset CIA Triad

The most critical asset is patient medical data (Protected Health Information  PHI), including medical records, prescriptions, appointment information, and messages with healthcare providers.

Using the CIA Triad:

Confidentiality: Medical information is highly sensitive. Unauthorized disclosure could violate patient privacy and result in legal, financial, and reputational damage.
Integrity:Medical records and prescriptions must not be modified without authorization. Incorrect medical information or medication instructions could directly harm a patient.
Availability:Patients and healthcare providers need access to medical information when required for treatment. An unavailable system could affect patient care.

Conclusion:
Patient medical data is the most critical asset because it requires very high levels of confidentiality, integrity, and availability.
In healthcare, integrity is particularly critical because unauthorized changes to medical information could directly affect patient safety.


2. STRIDE Threats for "Message Healthcare Providers"

2.1. Spoofing

Threat:An attacker compromises a healthcare provider's account and sends messages to patients while pretending to be the legitimate doctor.

Impact:Patients could receive fraudulent medical advice, potentially leading to incorrect treatment or medication decisions.

Mitigation:Use strong authentication, MFA, secure session management, and clearly identify verified healthcare providers.

2. 2. Tampering

Threat:An attacker modifies a message while it is being transmitted or stored. For example, a medication instruction could be changed from "10 mg" to "100 mg."

Impact:Incorrect medical information could lead to medication errors and potentially harm the patient.

Mitigation:Use HTTPS/TLS, strong access controls, message integrity protections, and server-side validation.



3. Repudiation

Threat:A patient or healthcare provider denies sending a particular message.

Impact: It could be difficult to determine who sent the message, making security investigations and legal disputes more difficult.

Mitigation:Use secure audit logs recording the sender, recipient, timestamp, message ID, and relevant access events. Logs must be protected from unauthorized modification.



4. Information Disclosure

Threat:An attacker gains unauthorized access to private patient-provider messages.

Impact:Sensitive medical information could be exposed, resulting in privacy violations, legal consequences, and reputational damage.

Mitigation:Encrypt data in transit and at rest, use strong authentication and authorization, and ensure users can only access conversations they are authorized to view.



3. Five Security Controls in Priority Order

1. Strong Authentication and MFA

Use strong authentication and multi-factor authentication, especially for healthcare providers.

Why:It reduces the risk of account takeover and prevents attackers from easily impersonating legitimate users.

2. Access Control and Authorization

Implement strict role-based access control.

Patients should only access their own medical records and conversations. Healthcare providers should only access information for patients they are authorized to treat.

Why: Even if an attacker obtains a valid account, authorization controls can prevent access to other patients' data.

3. Encryption

Use TLS/HTTPS for data transmitted between the mobile application, REST API, and hospital systems. Encrypt sensitive information stored in the cloud database and backups.

Why:Encryption protects patient information from interception and unauthorized access.

4. Audit Logging and Monitoring

Log important security events such as logins, failed authentication attempts, medical-record access, message access, prescription changes, and administrative actions.

Why: Logging provides accountability and helps detect and investigate security incidents.

5. Secure API and Input Validation

Protect the REST API with authentication, authorization, input validation, parameterized database queries, rate limiting, and secure error handling.

Why: The API is the main interface between the mobile application and the backend and is therefore a major attack surface.



Final Summary                          |
Patient medical data / PHI | Confidentiality: Prevent unauthorized disclosure | Integrity: Prevent unauthorized modification | Availability: Ensure information is accessible | Spoofing: Impersonating a healthcare provider | Tampering: Modifying medical messages | Repudiation: Denying a message was sent | Information Disclosure: Accessing private conversations | Strong authentication + MFA | Authorization and access control | Encryption in transit and at rest | Audit logging and monitoring | Secure API + input validation
