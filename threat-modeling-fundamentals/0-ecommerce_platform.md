E-commerce Platform  Threat Modeling
1. Three STRIDE threats for the checkout process

STRIDE is a threat-modeling methodology used to identify six categories of security threats:

Spoofing  pretending to be another user.
Tampering  modifying data without authorization.
Repudiation  denying that an action was performed.
Information Disclosure exposing confidential information.
Denial of Service  making a system or service unavailable.
Elevation of Privilege  obtaining unauthorized permissions.

For the checkout process, three important threats are Tampering, Spoofing, and Information Disclosure/Tampering.

Threat 1: Manipulating the product price

STRIDE category: Tampering

Threat description:

The React frontend runs in the customer's browser, so it cannot be trusted. An attacker can use browser developer tools or a proxy such as Burp Suite to modify the HTTP request sent to the Node.js API.

For example, if a product costs 100, the frontend might send the following information:

product_id = 123, quantity = 1, price = 100

An attacker could modify the request and send:

product_id = 123, quantity = 1, price = 1

If the backend trusts the price received from the frontend, the attacker could potentially purchase a ¬100 product
Potential impact:

Financial losses for the company.
Fraudulent orders.
Unauthorized discounts.
Incorrect order records.
Revenue loss.
Potential large-scale exploitation if the attack can be automated.

Suggested mitigation:

The backend must never trust the price or total calculated by the frontend.

The frontend should only send information such as the product ID and quantity. The Node.js backend should retrieve the official product price from PostgreSQL and calculate the total itself.

The backend should also validate:

Product ID.
Quantity.
Product availability.
Discounts.
Taxes.
Shipping costs.
Final order amount.

The amount sent to Stripe should be calculated and verified by the backend.

The main security principle is that the frontend is untrusted, while the backend must enforce the business rules.

Threat 2: Spoofing an authenticated customer

STRIDE category: Spoofing

Threat description:

Checkout requires authentication. An attacker who obtains a customer's authentication token, session cookie, or credentials could potentially impersonate that customer.

For example, if an attacker obtains a valid session token belonging to another user, they could send requests to the Node.js API that appear to come from the legitimate customer.

The attacker might then create fraudulent orders or access protected account functionality.

Potential impact:

Unauthorized purchases.
Account takeover.
Financial losses for customers.
Exposure of personal information.
Unauthorized access to order history.
Damage to the reputation of the e-commerce company.

Suggested mitigation:

The application should implement strong authentication and secure session management.

Recommended protections include:

Use HTTPS/TLS for all communications.
Use secure authentication mechanisms.
Use short-lived tokens where appropriate.
Use HttpOnly and Secure cookies for session cookies where appropriate.
Use appropriate SameSite cookie settings.
Expire inactive sessions.
Invalidate sessions after logout.
Use multi-factor authentication for sensitive operations where appropriate.
Check authorization on every protected API request.

It is also important to distinguish authentication from authorization. The server must verify not only that the user is logged in, but also that the user is authorized to access or modify the requested resource.

Threat 3: Payment information interception or manipulation

STRIDE category: Information Disclosure / Tampering

Threat description:

During checkout, payment-related information is exchanged between the customer's browser, the Node.js API, and Stripe.

An attacker could attempt to intercept or modify payment-related information, such as the payment amount, order ID, currency, or payment status.

Another risk would occur if the application trusts the browser to tell the backend that a payment was successful.

For example, an attacker might attempt to modify a request from:

payment_status = failed

to:

payment_status = successful

If the backend accepts this information without independently verifying the payment, the attacker could potentially receive an order without actually paying.

Potential impact:

Fraudulent payments.
Orders being fulfilled without successful payment.
Financial losses.
Exposure of sensitive payment information.
Chargebacks and payment disputes.
Damage to the company's reputation.

Suggested mitigation:

The application should:

Use HTTPS/TLS.
Avoid unnecessarily handling raw card information.
Use Stripe's secure payment/tokenization mechanisms.
Keep Stripe secret API keys on the backend.
Never trust payment status received directly from the browser.
Verify payment status server-side.
Verify Stripe webhook signatures.
Only mark an order as paid after receiving trusted confirmation from Stripe.

This ensures that the customer cannot simply modify a browser request and claim that a payment was successful.

2. Trust boundaries in the system

A trust boundary is a point where data crosses between components with different levels of trust.

There are at least four important trust boundaries in this e-commerce system.

Trust Boundary 1: React frontend to Node.js API

The first and most important trust boundary is between the customer's browser and the Node.js backend.

The browser should be considered untrusted because the customer has complete control over their own browser and can modify requests before they reach the server.

For example, an attacker can modify:

Prices.
Quantities.
Product IDs.
API parameters.
Authentication information.
Payment-related fields.

Therefore, the Node.js API must validate all incoming data.

The backend must not assume that information is trustworthy simply because it was generated by the React application.

Trust Boundary 2: Node.js API to PostgreSQL

The second trust boundary is between the Node.js application and the PostgreSQL database.

The database contains important and potentially sensitive information, including:

Customer accounts.
Product information.
Prices.
Orders.
Order history.
Payment information or payment references.

The backend should access the database using controlled permissions.

Important security measures include:

Parameterized SQL queries.
Prepared statements.
Strong database authentication.
Least-privilege database accounts.
Input validation.
Database monitoring.
Appropriate encryption.

This boundary is especially important for preventing SQL injection.

Trust Boundary 3: Node.js API to Stripe

The third trust boundary exists between the Node.js backend and Stripe.

Stripe is an external third-party payment service. The application must therefore securely communicate with Stripe and should not expose sensitive Stripe credentials to the browser.

The backend should:

Use HTTPS.
Keep Stripe secret keys on the server.
Authenticate API requests properly.
Verify payment results.
Handle payment errors securely.
Avoid trusting payment information supplied by the client.
Trust Boundary 4: Stripe to Node.js webhook

The fourth boundary exists when Stripe sends payment notifications to the Node.js backend through webhooks.

Although Stripe is a trusted external service, the webhook endpoint may be accessible from the public Internet.

Therefore, the application should verify that the webhook actually came from Stripe.

Webhook signatures should be validated before the application processes the event.

For example, the application should not simply accept a request saying:

payment_status = successful

It should first verify that the request is an authentic Stripe webhook.

3. SQL Injection in product search using DREAD

DREAD is a risk-assessment methodology consisting of five factors:

Damage Potential
Reproducibility
Exploitability
Affected Users
Discoverability

Each factor can be rated from 0 to 10.

For this scenario, SQL injection in product search should receive a high rating because product search is publicly accessible and does not require authentication.

1. Damage Potential  9/10

A successful SQL injection could potentially allow an attacker to access or manipulate information in the PostgreSQL database.

The database may contain:

Customer information.
Product information.
Orders.
Order history.
Other sensitive application data.

Depending on the database permissions and the exact vulnerability, an attacker might be able to read, modify, or delete data.

Therefore, the damage potential is very high.

Score: 9/10

2. Reproducibility  8/10

If the product search functionality contains a SQL injection vulnerability, an attacker who discovers a working attack could potentially repeat it multiple times.

The attacker could send specially crafted search requests repeatedly and potentially automate the attack.

The exact reliability would depend on the implementation of the vulnerable query and database configuration.

Score: 8/10

3. Exploitability  7/10

The product search functionality does not require authentication.

This means an attacker does not necessarily need an account to interact with it.

The attacker only needs to access the search functionality and understand how to construct a suitable SQL injection attack.

Because some technical knowledge is required, a score of 7 is reasonable.

Score: 7/10

4. Affected Users  9/10

A successful SQL injection could potentially affect a large number of users because the attacker may gain access to data stored in the central database.

Potentially affected information could include customer information, orders, and other application data.

Because the vulnerability is in a public search function, the attack does not need to be directed at one particular customer.

Score: 9/10

5. Discoverability  9/10

Product search is normally easy to find because it is a public feature of an e-commerce website.

An attacker can simply visit the website and use the search function.

They can then investigate how the search request is sent to the backend.

Because authentication is not required, the vulnerability would be relatively easy to discover and test.

Score: 9/10

DREAD calculation
DREAD factor	Score
Damage Potential	9/10
Reproducibility	8/10
Exploitability	7/10
Affected Users	9/10
Discoverability	9/10
Total	42/50

Average score:

(9 + 8 + 7 + 9 + 9) Ã· 5 = 8.4/10

Overall rating: HIGH

SQL injection in the product search functionality should therefore be considered a high-risk vulnerability.

The fact that product search is unauthenticated makes the vulnerability particularly concerning because an attacker does not need to log in before attempting to exploit it.

SQL Injection Mitigation

The primary defense against SQL injection is the use of parameterized queries or prepared statements.

An unsafe application might construct a query by directly concatenating user input into SQL.

This is dangerous because the user's search term could become part of the SQL command.

A safer approach is to use a parameterized query where the search term is treated strictly as data.

Other recommended protections include:

Parameterized queries.
Prepared statements.
Input validation.
Least-privilege database accounts.
Secure error handling.
Database monitoring and logging.
Regular security testing.
Keeping PostgreSQL and Node.js dependencies updated.
Conclusion

The e-commerce platform has several important security risks because it combines an untrusted client, a trusted backend, a database, and an external payment provider.

The three most important STRIDE threats for checkout are:

Tampering: An attacker modifies the price or order information sent by the frontend.
Spoofing: An attacker obtains another user's credentials or session and performs actions as that user.
Information Disclosure/Tampering: An attacker attempts to intercept or manipulate payment information or payment status.

The main trust boundaries are:

React frontend  Node.js API.
Node.js API  PostgreSQL.
Node.js API  Stripe.
Stripe  Node.js webhook.

Finally, SQL injection in the public product search function has a DREAD score of 8.4/10, making it a high-risk threat. The most important mitigation is to use parameterized queries, combined with least-privilege database access and proper input validation.
