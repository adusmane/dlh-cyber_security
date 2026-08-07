Financial Trading Platform  Threat Modeling

1. Which CIA component is most critical? Can security requirements conflict with performance requirements?

The most critical CIA component for a financial trading platform is Integrity.

Integrity

Integrity ensures that:

* Stock prices are accurate.
* Buy and sell orders are not modified.
* Account balances remain correct.
* Trading rules execute as intended.
* Financial transactions are recorded accurately.

A loss of integrity could allow attackers to:

* Modify trading orders.
* Change account balances.
* Execute fraudulent trades.
* Manipulate financial data.

Example:

An attacker changes a sell order from:
"Sell 100 shares at $150"

to:
"Sell 100 shares at $1"
This could cause major financial losses and regulatory problems.


Availability

Availability is also extremely important because trading platforms require **99.99% uptime**.
A system outage could prevent users from:

* Buying or selling stocks.
* Managing investments.
* Reacting to market changes.
However, incorrect transactions caused by compromised integrity are usually more dangerous than a temporary outage.


Confidentiality

Confidentiality protects:

* Customer financial information.
* Account details.
* Trading strategies.
* Personal data.

A data leak could cause fraud, identity theft, and regulatory penalties.


2.Can security requirements conflict with performance requirements?

Yes. Security and performance requirements can conflict.

Examples:

* Encryption:Protects financial data but adds processing time.
* Authentication checks: Improve security but add latency before executing trades.
* Fraud detection: Helps identify suspicious activity but requires additional processing.

A trading platform requires very low latency (<100ms), so security controls must be optimized.

Solutions include:

* Hardware-accelerated encryption.
* Efficient authentication systems.
* Scalable infrastructure.
* Risk-based security checks.
* Optimized database operations.

The goal is to maintain strong security while meeting performance requirements.


2. Threat model for the "automated trading rules" feature

Risk 1: Unauthorized modification of trading rules

Category:Tampering
Threat description:An attacker gains access to a user's account and changes automated trading rules.

Example:
Original rule:"Buy 10 shares when the price reaches $50."

Attacker changes it to: "Buy 10,000 shares immediately."

Impact:

* Unauthorized trades.
* Financial losses.
* Market manipulation.
* Regulatory violations.
* Loss of customer trust.

Mitigation:

* Multi-factor authentication (MFA).
* Strong authorization checks.
* Confirmation before major rule changes.
* Trading limits.
* Audit logs.
* Notifications for rule modifications.



Risk 2: Logic flaws in automated trading algorithms

Category: Tampering / Elevation of Privilege

Threat description:A programming error or incorrect trading rule causes unexpected transactions.

Examples:

* Incorrect calculation of order quantity.
* Missing risk limits.
* Infinite trading loops.
* Incorrect price conditions.

Impact:

* Large financial losses.
* Excessive trading activity.
* Incorrect investment decisions.
* Regulatory issues.

Mitigation:

* Validate trading rules before activation.
* Use testing and simulation environments.
* Apply maximum trade limits.
* Implement risk management controls.
* Monitor automated trading behavior.


Risk 3: Race conditions during trade execution

Category:Tampering

Threat description:Multiple automated trading rules execute at the same time, causing inconsistent results.

Example:

A user has $10,000.
Two automated rules execute simultaneously:

* Rule 1 buys $8,000 of stock.
* Rule 2 buys $8,000 of another stock.
If both transactions check the balance at the same time, the system may incorrectly approve both.

Impact:

* Negative account balances.
* Invalid transactions.
* Incorrect financial records.
* Regulatory compliance problems.

Mitigation:

* Use atomic database transactions.
* Implement locking mechanisms.
* Use concurrency controls.
* Verify account balance before execution.
* Use transaction queues.


3. Defense-in-depth controls after account compromise

If an attacker compromises a user account, multiple security layers should limit the damage.

Layer 1: Multi-Factor Authentication (MFA)

Purpose:Prevents attackers from accessing accounts using only stolen passwords.

Layer 2: Transaction and trading limits

Purpose:Limits the amount of damage an attacker can cause.

Examples:

* Maximum daily trading amount.
* Maximum order size.
* Transfer limits.
* Additional approval for large transactions.


Layer 3: Anomaly detection

Purpose:Detects unusual account behavior.

Examples:

* Login from unusual locations.
* Sudden large trades.
* Unusual trading patterns.
* Rapid transactions.


Layer 4: Secure session management

Purpose:Protects against stolen sessions.

Controls:

* Short session expiration.
* Secure cookies.
* Device monitoring.
* Session revocation.


Layer 5: Authorization controls

Purpose:Ensures users can only perform permitted actions.

Examples:

* Verify account ownership.
* Validate trading permissions.
* Restrict sensitive operations.


Layer 6: Audit logging

Purpose:provides accountability and helps investigate incidents.

Logs should record:

* Login activity.
* Trades executed.
* Rule changes.
* Fund transfers.
* Account modifications.


Layer 7: Real-time monitoring and alerts

Purpose:Detects attacks quickly and enables response.

Examples:

* Suspicious transactions.
* Multiple failed logins.
* Abnormal API activity.

Summary
Most critical CIA component:
Integrity -  because unauthorized modification of trades, balances, or financial data can directly cause financial losses and regulatory violations

Security vs performance conflict:
Encryption, authentication, and fraud detection improve security but may increase latency. The solution is optimized security controls that maintain the required <100ms trading speed.

Top automated trading risks:

1. Unauthorized rule modification
Mitigation: MFA, authorization, audit logs, trading limits.

2. Logic flaws in trading algorithms
Mitigation: Testing, validation, simulations, risk controls.

3. Race conditions
Mitigation: Atomic transactions, locking, concurrency controls.

Defense-in-depth layers:

1. Multi-factor authentication (MFA)
2. Transaction and trading limits
3. Anomaly detection
4. Secure session management
5. Authorization controls
6. Audit logging
7. Real-time monitoring and alerts

Main security principle: Even if an attacker compromises a user account, multiple security layers should prevent unauthorized trades, limit financial damage, and provide detection and investigation capabilities.

