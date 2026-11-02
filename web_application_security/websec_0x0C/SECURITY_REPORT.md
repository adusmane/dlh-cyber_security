# Penetration Test Report – NexusShop XSS Assessment

**Target:** `http://web0x0c.hbtn`  
**Assessment date:** 2 November 2026  
**Assessment type:** Authorized security assessment in a controlled training lab  
**Scope:** NexusShop XSS challenge Tasks 0–7  
**Evidence basis:** Written lab notes, recorded browser/console/network observations, endpoint responses, and the supplied captured-flag list. 

 Captured challenge flags are listed separately from technical proof of impact.

---

## 1. Executive Summary

The assessment examined reflected, stored, and DOM-based Cross-Site Scripting (XSS) weaknesses in NexusShop. The tested input paths included search terms, product sorting, product reviews, profile fields, Markdown product descriptions, URL fragments, and messages handled through `postMessage`.

The written lab notes demonstrate that several application components render untrusted input as HTML or insert it into the DOM using unsafe sinks such as `innerHTML`. The notes also document incomplete filtering approaches: removing `<script>` elements or selected event-handler attributes did not consistently prevent alternative execution paths. In particular, image error handlers, SVG animation events, and `javascript:` links were tested in different stages.

The most significant risks are persistent XSS in content displayed to other users and DOM-based XSS in client-side message or URL handling. These vulnerabilities can allow attacker-controlled JavaScript to execute in a visitor's browser under the application's origin. Depending on the user's session and the data exposed to page JavaScript, impact may include page manipulation, phishing, unauthorized same-origin actions, and access to browser-accessible information.

### 1.1 Captured challenge flags

The following values are transcribed from the supplied final captured-flag list. Filenames are preserved as supplied; they are not assumed to correspond one-to-one with the task numbering.

| Challenge flag file | Captured flag |
|---|---|
| `0-flag.txt` | `FLAG{69ed7f8940b50827fc8620fe2d0ec443}` |
| `2-flag.txt` | `FLAG{df0527e87cd04f93be93b4185fde767c}` |
| `3-flag.txt` | `FLAG{fe135f926c84d2a8b90cf7e57df1ae15}` |
| `4-flag.txt` | `FLAG{14ba906131407473c256b2d9259dd061}` |
| `5-flag.txt` | `FLAG{f5bc6b1d70995153b1a8517a0c377fda}` |
| `6-flag.txt` | `FLAG{d472b170ed096cb64a67b7acd9305a6d}` |
| `7-flag.txt` | `FLAG{5a5d3246488201f3914a86ac94437b1b}` |



### 1.2 Overall risk

**Overall assessment: High**, based on the demonstrated unsafe rendering patterns and successful JavaScript execution recorded in the written notes. Persistent XSS affecting customer-facing pages or privileged users may warrant a Critical rating once the application's user roles, exposure, and exploit prerequisites are confirmed.

---

## 2. Scope and Methodology

### 2.1 In-scope application areas

- Search and reflected query parameters.
- Product sorting and JavaScript-context reflection.
- Product review submission and display.
- User profile fields and profile API rendering.
- Product description Markdown editor and preview.
- Product-page URL-fragment handling.
- Cart-page `postMessage` event handling.
- Lab-provided attacker/C2 endpoints and tracking endpoints, where recorded in the notes.

### 2.2 Testing methodology

Testing followed a manual, controlled approach:

1. Identify user-controlled inputs and submit unique marker values.
2. Inspect the rendered DOM to determine whether input is treated as text or parsed as HTML.
3. Inspect client-side JavaScript for source-to-sink flows, including `location.hash`, `MessageEvent.data`, API-returned profile data, and `innerHTML`.
4. Use non-destructive proof-of-execution payloads that write a unique marker to the browser Console.
5. Inspect Network activity and endpoint responses where the notes record tracking or C2 requests.
6. Record whether filters block the tested payload, whether execution requires user interaction, and whether the input is stored.
7. Recommend secure rendering, validation, sanitization, and browser security controls.

All testing described here is limited to the authorized training environment.

---

## 3. Findings

## Finding 1 – Reflected XSS in Basic Search

**Category:** Reflected Cross-Site Scripting  
**Affected input:** `q`  
**Affected routes:** `/search`, `/search/filtered`, `/search/advanced`  
**Severity:** High

### Description

The search feature reflects the user-controlled `q` parameter into the search-results heading. The written notes record that a supplied HTML marker was interpreted as an actual DOM element, demonstrating HTML injection rather than safe text rendering.

The three stages applied progressively stricter filters, but the recorded tests found alternative execution paths:

- Stage 1: direct script execution was demonstrated.
- Stage 2: a `<script>` filter did not prevent an image `onerror` handler from executing.
- Stage 3: common event-handler filtering did not prevent the tested SVG animation `onbegin` handler.

This indicates that blacklist filtering is not a reliable replacement for context-aware output encoding or safe HTML sanitization.

### Test evidence recorded

- A unique marker was located in the search heading.
- `<strong id="xss-probe">HTML_PROBE</strong>` was rendered as a real `<strong>` element.
- Console markers `XSS_STAGE1_EXECUTED`, `XSS_STAGE2_EXECUTED`, and `XSS_STAGE3_EXECUTED` were recorded.
- The notes record a successful `POST /attacker/api/exfil` response (HTTP 200) and a corresponding C2 dashboard entry.
- The Stage 2 C2 value was `no-readable-cookie`; this proves that the test request was transmitted, not that an actual cookie was stolen.
- The notes record successful Stage 3 tracking through `/search/api/track`.

### Representative test payloads

HTML rendering test:

```html
<strong id="xss-probe">HTML_PROBE</strong>
```

Stage 2 event-handler test:

```html
<img src=x onerror='console.log("XSS_STAGE2_EXECUTED")'>
```

Stage 3 SVG event test:

```html
<svg><animate attributeName=x dur=1s
onbegin='console.log("XSS_STAGE3_EXECUTED")'></animate></svg>
```

### Impact

An attacker could send a crafted search URL to a victim. If the victim opens it, injected JavaScript may execute in the NexusShop origin, potentially changing page content, presenting fraudulent prompts, or making authenticated same-origin requests. `HttpOnly` cookies are not readable through `document.cookie`, although XSS may still abuse an authenticated browser session.

### Recommendations

- Render search terms with `textContent`, not `innerHTML`.
- Apply context-specific output encoding at the final rendering point.
- If rich HTML is required, use a maintained allowlist-based sanitizer.
- Do not rely on blacklists of tags, attributes, or event names.
- Validate values against expected formats and reject unexpected input.
- Deploy a restrictive Content Security Policy (CSP) as defense in depth.

---

## Finding 2 – Reflected Input in Product-Sorting JavaScript Context

**Category:** Reflected XSS risk / JavaScript-context injection  
**Affected input:** `by`  
**Affected routes:** `/products/sort`, `/products/sort/dynamic`, `/products/sort/advanced`  
**Severity:** High if executable injection is confirmed; the supplied notes do not establish successful execution for the tested Stage 1 payloads.

### Description

The product-sorting endpoint reflects the `by` query parameter into a JavaScript assignment for `currentSort`. This is a sensitive context: untrusted input should not be concatenated into executable JavaScript.

The written notes show that Stage 1 encoded quote and angle-bracket characters as HTML entities. The recorded single-quote breakout and `</script>` breakout attempts did not execute. The notes refer to further Stage 2 and Stage 3 investigation, but do not preserve a complete successful payload and matching execution evidence for this finding.

The supplied flag list includes `2-flag.txt`; that captured flag is recorded in Section 1.1, but is not treated as proof that the particular Stage 1 test payload succeeded.

### Test evidence recorded

- `TESTINPUT123` was reflected into the `currentSort` JavaScript assignment.
- The inspected output encoded quote and angle-bracket characters as entities.
- The tested string-breakout payload did not execute.
- The tested script-block breakout did not execute.
- A complete successful Stage 2/Stage 3 execution chain is not documented in the supplied written notes.

### Representative tested input

```text
/products/sort?by=TESTINPUT123
```

Attempted string breakout (recorded as unsuccessful):

```javascript
';console.log("XSS_TASK1_STAGE1_EXECUTED");//
```

### Impact

If an untrusted sort value reaches executable JavaScript without correct encoding, a crafted URL could execute script in a victim's browser under the NexusShop origin. Potential consequences include page manipulation and unauthorized same-origin actions. The exact impact for this route should be confirmed with a reproducible successful payload before treating exploitability as demonstrated.

### Recommendations

- Avoid placing untrusted values inside inline JavaScript.
- Pass data through safely serialized JSON or non-executable DOM data attributes.
- Allowlist supported sort keys, such as `name`, `price`, and `rating`.
- Use a safe JSON serializer that escapes script-breaking characters.
- Remove inline scripts where practical and enforce CSP nonces or hashes.

---

## Finding 3 – Stored XSS in Product Reviews

**Category:** Stored Cross-Site Scripting  
**Affected routes:** `/product/1/reviews`, `/product/1/reviews/verified`, `/product/1/reviews/all`  
**Affected fields:** Review body and reviewer name  
**Severity:** High; potentially Critical where stored content is displayed to customers or privileged users.

### Description

The review feature stores user-supplied content and later renders it on product pages. The notes demonstrate that HTML in the review body is interpreted by the browser and that an image `onerror` handler executes after the page is reloaded. This confirms persistence.

The later review stage also exposes the reviewer-name field. The notes record that the name is rendered in both a title attribute and a text element, and that an image event-handler payload in the name field executed. This shows that all user-controlled fields require context-appropriate handling.

### Test evidence recorded

- A `<b>` marker was rendered as a real HTML element.
- A stored image event-handler payload executed after reloading the review page (`STORED-XSS-OK`).
- In the verified stage, the script element was removed but the image event handler remained executable (`V2-OK`).
- In the all-reviews stage, a payload in the reviewer name executed (`NAME-XSS`).
- The notes record uncertainty about the correct review tracking callback and do not provide a complete final C2 loot record for this finding.

### Representative test payloads

Stored review-body test:

```html
<img src=x onerror="console.log('STORED-XSS-OK')">
```

Reviewer-name test:

```html
<img src=x onerror=console.log('NAME-XSS')>
```

### Impact

A malicious review may execute whenever another user views the affected product. This can expose customers and potentially moderators or administrators to page manipulation, fraudulent content, or unauthorized actions performed through their browser session.

### Recommendations

- Render review bodies and reviewer names as text by default.
- If formatting is required, sanitize with a maintained allowlist-based HTML sanitizer.
- Encode reviewer names separately for HTML text and attribute contexts.
- Avoid constructing review markup by concatenating untrusted values into `innerHTML`.
- Add moderation and removal procedures for malicious stored content.
- Test every review field, not only the review body.

---

## Finding 4 – Stored XSS in User Profile Rendering

**Category:** Stored XSS / DOM-based rendering flaw  
**Affected routes:** `/profile`, `/profile/settings`, `/profile/edit`  
**API endpoints:** `/profile/api/data`, `/profile/api/update`  
**Affected fields:** Bio and username  
**Severity:** High; potentially Critical if other users or privileged viewers load the affected profile.

### Description

The profile page retrieves profile fields from a JSON API and renders them in the browser. The written source inspection identifies unsafe `innerHTML` assignments for API-returned profile values.

The notes demonstrate stored execution through the bio field in earlier stages. In the later stage, the bio is encoded but the username remains raw HTML and is rendered as markup. This inconsistent treatment leaves another stored XSS path.

### Test evidence recorded

- Network inspection identified `GET /profile/api/data`.
- Source inspection identified assignments such as:

```javascript
document.getElementById('profile-bio').innerHTML = data.bio || 'No bio set';
```

- Stage 1 bio payload executed after reload (`PROFILE_XSS_STAGE1_EXECUTED`).
- Stage 2 removed the script element but retained an executable image event handler (`STAGE2_XSS_EXECUTED`).
- Stage 3 showed raw HTML in `username` while `bio` was encoded.
- A username payload executed after reload (`PROFILE_XSS_STAGE3_EXECUTED`).
- The supplied notes do not reproduce the final tracking response for this finding.

### Representative test payload

```html
<img src=x onerror="console.log('PROFILE_XSS_STAGE3_EXECUTED')">
```

### Impact

An attacker able to modify profile fields may cause script execution when the profile is rendered. Depending on who can view the profile, affected users may include customers, moderators, or administrators. The script may alter profile content, present fraudulent prompts, or perform actions available to the victim's authenticated browser.

### Recommendations

- Replace `innerHTML` with `textContent` for profile values that do not require HTML.
- Apply the same output-safety policy to every profile field.
- Sanitize rich text with a strict allowlist if formatting is required.
- Validate website fields with a URL parser and allow only approved schemes.
- Treat JSON as a transport format, not as proof that values are safe to insert into HTML.

---

## Finding 5 – Stored XSS in Markdown Product Descriptions

**Category:** Stored XSS through Markdown-to-HTML rendering  
**Affected routes:** `/admin/products/1/edit`, `/admin/products/1/edit/safe`, `/admin/products/1/edit/strict`  
**Affected input:** Product description (`description`)  
**Severity:** High; potentially Critical if customer-facing product descriptions can contain active content.

### Description

The product editor converts Markdown into HTML for preview and product-description rendering. The notes show that raw HTML survived the initial Markdown rendering and that the resulting output was marked safe in the server-side template. This permits editor-controlled HTML to reach the browser.

The later stages applied filters, but the recorded tests show that removing script tags did not prevent an image event handler from executing. The strict stage blocked the tested image event-handler payload and removed a direct `javascript:` link. An entity-encoded URL probe nevertheless produced an anchor with `href="javascript:1"`. The notes do not confirm JavaScript execution from that link.

A separate direct tracking-endpoint test is recorded in the notes, but a manual tracking request is not proof that the Markdown payload triggered the callback.

### Test evidence recorded

- Raw `<b>` HTML survived in the Stage 1 preview.
- The Stage 1 stored image event-handler payload executed.
- Stage 2 escaped the script element but retained an executable image event handler.
- Stage 3 escaped the tested image event handler.
- Stage 3 removed the direct `javascript:` link `href`.
- An entity-encoded URL probe produced `href="javascript:1"`; execution was not confirmed.
- The notes record a tracking-endpoint test, but do not establish an XSS-triggered tracking callback for the strict stage.

### Representative test payloads

Stage 1 execution test:

```html
<img src=x onerror="console.log('MARKDOWN_STAGE1_XSS_EXECUTED')">
```

Stage 2 filtering test:

```html
<script>console.log('STAGE2_SCRIPT_EXECUTED')</script>
<img src=x onerror="console.log('MARKDOWN_STAGE2_XSS_EXECUTED')">
```

Entity-encoded URL probe:

```markdown
[STAGE3_ENTITY_SIMPLE](java&#x73;cript:1)
```

### Impact

If an attacker can store active markup in a product description, customers viewing the affected product may receive attacker-controlled content. Potential consequences include fraudulent product information, phishing overlays, or unauthorized actions through the visitor's browser.

### Recommendations

- Disable raw HTML in Markdown unless explicitly required.
- Sanitize generated HTML with a maintained allowlist-based sanitizer.
- Canonicalize and validate URL schemes after entity decoding.
- Remove event-handler attributes, dangerous elements, and unsafe URL schemes.
- Do not mark untrusted Markdown output as safe unless it has passed an appropriate sanitizer.
- Apply identical protections to editor previews and customer-facing product pages.

---

## Finding 6 – DOM XSS Through URL Fragment Handling

**Category:** DOM-based Cross-Site Scripting  
**Affected routes:** `/product/1`, `/product/1/gallery`, `/product/1/specs`  
**Source:** `location.hash`  
**Sink:** `section-title.innerHTML`  
**Severity:** High; the strict-stage tested payload requires user interaction.

### Description

The product page reads the URL fragment, decodes it, and inserts the value into the page using `innerHTML`. Because the URL fragment is processed by client-side code and is not included in the initial HTTP request path, server-side request filtering alone may not detect or prevent the issue.

The notes identify the source-to-sink flow:

```javascript
decodeURIComponent(location.hash.slice(1))
```

followed by an assignment to `section-title.innerHTML`.

Stages 1 and 2 allowed event-handler execution. In Stage 3, common event-handler attributes were rewritten to `data-blocked`, but a `javascript:` link remained usable and executed after a click.

### Test evidence recorded

- A marker in the URL fragment changed the page title.
- Inspector/source review identified the fragment-to-`innerHTML` flow.
- HTML injection was confirmed.
- Stages 1 and 2 produced JavaScript execution markers.
- Stage 3 changed the tested `onerror` attribute to `data-blocked`.
- A `javascript:` anchor survived and executed after a click (`DOM_STAGE3_LINK_EXECUTED`).
- A synthetic C2 marker was recorded with HTTP 200 and appeared in the C2 dashboard.
- The C2 value was a test marker, not evidence of stolen cookie data.
- The notes record successful tracking through `/product/api/track`.

### Representative test payload

```javascript
location.hash = encodeURIComponent(
  `<a href="javascript:console.log('DOM_STAGE3_LINK_EXECUTED')">CLICK_TO_TEST_XSS</a>`
);
```

### Impact

An attacker could distribute a crafted product URL containing a malicious fragment. When opened, the client-side code may interpret the fragment as HTML. The Stage 3 test required the victim to click the injected link, but successful execution could still manipulate the page or make same-origin requests.

### Recommendations

- Use `textContent` for titles and labels derived from URL fragments.
- Validate fragment values against a fixed set of permitted identifiers.
- Do not use regular expressions as the primary HTML sanitizer.
- If rich HTML is necessary, use a vetted allowlist sanitizer and reject unsafe URL schemes after canonicalization.
- Apply CSP as defense in depth.

---

## Finding 7 – DOM XSS Through postMessage Handling

**Category:** DOM-based Cross-Site Scripting  
**Affected routes:** `/cart`, `/cart/checkout`, `/cart/payment`  
**Source:** `MessageEvent.data`  
**Sink:** `widget-message.innerHTML`  
**Severity:** High; potentially Critical depending on embedding context and affected users.

### Description

The cart page listens for browser `message` events and renders message content in a Special Offers widget. The written notes identify a handler that accepts strings or objects containing a `content` property and inserts the value using `innerHTML`.

The handler did not validate `event.origin` in the inspected stage. Later stages applied filters, but the notes record that removing script tags did not prevent image event-handler execution. In the stricter stage, the handler required an object with `type: "widget-update"` and a `content` property. A clickable `javascript:` link remained an execution path.

### Test evidence recorded

- A harmless `postMessage` object displayed its `content` in the widget.
- Inspector/source review identified the `message` event listener and `innerHTML` sink.
- A real `<b>` element was created from message content.
- An image `onerror` payload executed in Stage 1.
- Stage 2 removed the script element but retained the image event handler.
- Stage 3 required the `widget-update` message type and a `content` field.
- A clickable `javascript:` link survived filtering and executed after a click.
- A synthetic C2 marker was recorded with HTTP 200 and appeared in the dashboard under Level 8 / Stage 3.
- The notes record submission of the page tracking token through `/cart/api/track`.

### Representative test messages

Harmless message:

```javascript
window.postMessage(
  { content: 'TASK7_STAGE1_TEST' },
  window.location.origin
);
```

Stage 1 execution proof:

```javascript
window.postMessage({
  content: `<img src="x" onerror="console.log('POSTMESSAGE_STAGE1_XSS_EXECUTED')">`
}, window.location.origin);
```

Stage 3 expected message structure:

```javascript
window.postMessage({
  type: "widget-update",
  content: "CONTROLLED_TEST_CONTENT"
}, window.location.origin);
```

### Impact

If an untrusted or insufficiently validated sender can deliver a message to the page, attacker-controlled content may be rendered as HTML and executed in the NexusShop origin. A vulnerable message handler can therefore expose users to DOM XSS through cross-window communication. Depending on the page and session, impact may include page manipulation, phishing, and authenticated same-origin actions.

### Recommendations

- Validate `event.origin` against an explicit allowlist of trusted origins.
- Validate `event.source` where the application expects messages from a specific window or frame.
- Validate message structure and types using a strict schema.
- Render message content using `textContent`, not `innerHTML`.
- If HTML is a genuine requirement, sanitize it using a maintained allowlist-based sanitizer.
- Do not rely on script-tag or event-handler regex filters.
- Use a restrictive CSP as an additional mitigation.

---

## 4. Cross-Cutting Security Observations

The findings show recurring weaknesses that should be addressed centrally rather than fixed only at individual endpoints.

### 4.1 Unsafe DOM sinks

The written notes identify `innerHTML` as a recurring sink in search rendering, profile rendering, URL-fragment handling, and `postMessage` handling. The application should establish a rule that untrusted values are rendered as text by default.

### 4.2 Incomplete blacklist filtering

The tested stages demonstrate that removing `<script>` elements or selected event-handler attributes does not reliably prevent XSS. Alternative execution paths were observed or tested, including:

- Image `onerror` handlers.
- SVG animation `onbegin` handlers.
- `javascript:` links.
- Entity-encoded URL schemes.

A blacklist must not be treated as a security boundary.

### 4.3 Stored content has wider exposure

Review, profile, and product-description content can persist and execute when another user loads the relevant page. Stored XSS should be prioritized according to who can view the content and whether privileged users are exposed.

### 4.4 Browser-side sources need validation

Client-side sources such as `location.hash` and `MessageEvent.data` are untrusted. They require validation and safe rendering even if the server does not receive the original value.

### 4.5 C2 evidence must be interpreted accurately

The written notes record successful test requests and C2 dashboard entries for some stages. A successful HTTP response or a synthetic marker proves that the test data reached the endpoint; it does not automatically prove that real cookies or sensitive user data were stolen. The report therefore distinguishes synthetic proof markers from actual sensitive-data exposure.

---

## 5. Remediation Plan and Priorities

| Priority | Recommended action | Reason |
|---|---|---|
| P1 – Immediate | Replace unsafe `innerHTML` use with `textContent` wherever HTML is not required. | Removes the recurring DOM execution path. |
| P1 – Immediate | Sanitize all stored rich-text content with a maintained allowlist-based sanitizer. | Protects reviews, profile content, and Markdown descriptions. |
| P1 – Immediate | Validate `postMessage` origin, source, and message schema. | Prevents untrusted cross-window messages from reaching sensitive rendering logic. |
| P1 – Immediate | Validate URL-fragment values and never render them as HTML. | Removes the client-side fragment injection path. |
| P1 – Immediate | Allowlist product sort keys and avoid inline JavaScript interpolation. | Prevents unsafe JavaScript-context reflection. |
| P2 – Short term | Canonicalize and validate URLs and schemes after entity decoding. | Prevents encoded dangerous schemes from bypassing filters. |
| P2 – Short term | Deploy a restrictive Content Security Policy. | Reduces the impact of injection flaws. |
| P2 – Short term | Set session cookies with `HttpOnly`, `Secure`, and appropriate `SameSite` attributes. | Reduces cookie exposure and cross-site request risk. |
| P2 – Short term | Add automated regression tests for every user-controlled field and rendering route. | Prevents the same weakness from reappearing in another field or stage. |
| P3 – Ongoing | Review code for unsafe DOM sinks and centralize safe rendering utilities. | Makes secure behavior consistent across the application. |

---

## 6. Retesting Requirements

After remediation, retest each affected route and field using both benign HTML markers and non-destructive execution probes. Retesting should verify:

1. User-controlled input is displayed as text unless explicitly sanitized rich text is required.
2. No injected event handler or script executes after page load or reload.
3. Stored content remains inert when viewed by a different account.
4. URL fragments cannot create executable DOM elements or unsafe links.
5. `postMessage` events from untrusted origins are rejected.
6. Invalid message structures are rejected without rendering.
7. Encoded and mixed-case dangerous URL schemes are rejected after canonicalization.
8. CSP violations are logged and expected application functionality continues to work.
9. Tracking and C2 test endpoints are not treated as proof of sensitive-data theft unless the transmitted data is independently verified.

---

## 7. Conclusion

The NexusShop assessment demonstrates multiple XSS weaknesses across reflected input, stored user content, and browser-side DOM processing. The written test notes show that unsafe HTML rendering and incomplete blacklist filters are recurring root causes. Several controlled payloads successfully executed JavaScript, including cases where an initial filter removed script tags but left alternative browser execution mechanisms available.

The highest priority is to eliminate unsafe rendering of untrusted data, sanitize any business-required rich HTML, validate cross-window messages, and avoid placing user-controlled values into executable JavaScript. These changes should be followed by regression testing across every affected field and route.

The captured challenge flags are included , while evidence gaps are explicitly identified. 

---

**End of report**  
**Document:** `SECURITY_REPORT.md`  
**Assessment target:** `http://web0x0c.hbtn`  
**Assessment date:** 2 November 2026
