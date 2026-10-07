# Type of Results/Alerts Covered

The DAST engine includes passive and active scan rules which find specific vulnerabilities.

Currently the type of alerts covered by DAST are the following:

| Id | Alert | Severity | Type |
| --- | --- | --- | --- |
| [0](https://www.zaproxy.org/docs/alerts/0/) | [Directory Browsing](https://www.zaproxy.org/docs/alerts/0/) | Medium | Active |
| [2](https://www.zaproxy.org/docs/alerts/2/) | [Private IP Disclosure](https://www.zaproxy.org/docs/alerts/2/) | Low | Passive |
| [3](https://www.zaproxy.org/docs/alerts/3/) | [Session ID in URL Rewrite](https://www.zaproxy.org/docs/alerts/3/) |  | Passive |
| [44929](https://www.zaproxy.org/docs/alerts/3-1/) | [Session ID in URL Rewrite](https://www.zaproxy.org/docs/alerts/3-1/) | Medium | Passive |
| [44960](https://www.zaproxy.org/docs/alerts/3-2/) | [Session ID in URL Rewrite](https://www.zaproxy.org/docs/alerts/3-2/) | Medium | Passive |
| [44988](https://www.zaproxy.org/docs/alerts/3-3/) | [Referer Exposes Session ID](https://www.zaproxy.org/docs/alerts/3-3/) | Medium | Passive |
| [6](https://www.zaproxy.org/docs/alerts/6/) | [Path Traversal](https://www.zaproxy.org/docs/alerts/6/) |  | Active |
| [44932](https://www.zaproxy.org/docs/alerts/6-1/) | [Path Traversal](https://www.zaproxy.org/docs/alerts/6-1/) | High | Active |
| [44963](https://www.zaproxy.org/docs/alerts/6-2/) | [Path Traversal](https://www.zaproxy.org/docs/alerts/6-2/) | High | Active |
| [44991](https://www.zaproxy.org/docs/alerts/6-3/) | [Path Traversal](https://www.zaproxy.org/docs/alerts/6-3/) | High | Active |
| [45022](https://www.zaproxy.org/docs/alerts/6-4/) | [Path Traversal](https://www.zaproxy.org/docs/alerts/6-4/) | High | Active |
| [45052](https://www.zaproxy.org/docs/alerts/6-5/) | [Path Traversal](https://www.zaproxy.org/docs/alerts/6-5/) | High | Active |
| [7](https://www.zaproxy.org/docs/alerts/7/) | [Remote File Inclusion](https://www.zaproxy.org/docs/alerts/7/) | High | Active |
| [10003](https://www.zaproxy.org/docs/alerts/10003/) | [Vulnerable JS Library](https://www.zaproxy.org/docs/alerts/10003/) | Medium | Passive |
| [10010](https://www.zaproxy.org/docs/alerts/10010/) | [Cookie No HttpOnly Flag](https://www.zaproxy.org/docs/alerts/10010/) | Low | Passive |
| [10011](https://www.zaproxy.org/docs/alerts/10011/) | [Cookie Without Secure Flag](https://www.zaproxy.org/docs/alerts/10011/) | Low | Passive |
| [10015](https://www.zaproxy.org/docs/alerts/10015/) | [Re-examine Cache-control Directives](https://www.zaproxy.org/docs/alerts/10015/) | Informational | Passive |
| [10017](https://www.zaproxy.org/docs/alerts/10017/) | [Cross-Domain JavaScript Source File Inclusion](https://www.zaproxy.org/docs/alerts/10017/) | Low | Passive |
| [10019](https://www.zaproxy.org/docs/alerts/10019/) | [Content-Type Header Missing](https://www.zaproxy.org/docs/alerts/10019/) | Informational | Passive |
| [10020](https://www.zaproxy.org/docs/alerts/10020/) | [Anti-clickjacking Header](https://www.zaproxy.org/docs/alerts/10020/) |  | Passive |
| [10020-1](https://www.zaproxy.org/docs/alerts/10020-1/) | [Missing Anti-clickjacking Header](https://www.zaproxy.org/docs/alerts/10020-1/) | Medium | Passive |
| [10020-2](https://www.zaproxy.org/docs/alerts/10020-2/) | [Multiple X-Frame-Options Header Entries](https://www.zaproxy.org/docs/alerts/10020-2/) | Medium | Passive |
| [10020-3](https://www.zaproxy.org/docs/alerts/10020-3/) | [X-Frame-Options Defined via META (Non-compliant with Spec)](https://www.zaproxy.org/docs/alerts/10020-3/) | Medium | Passive |
| [10020-4](https://www.zaproxy.org/docs/alerts/10020-4/) | [X-Frame-Options Setting Malformed](https://www.zaproxy.org/docs/alerts/10020-4/) | Medium | Passive |
| [10021](https://www.zaproxy.org/docs/alerts/10021/) | [X-Content-Type-Options Header Missing](https://www.zaproxy.org/docs/alerts/10021/) | Low | Passive |
| [10023](https://www.zaproxy.org/docs/alerts/10023/) | [Information Disclosure - Debug Error Messages](https://www.zaproxy.org/docs/alerts/10023/) | Low | Passive |
| [10024](https://www.zaproxy.org/docs/alerts/10024/) | [Information Disclosure - Sensitive Information in URL](https://www.zaproxy.org/docs/alerts/10024/) | Informational | Passive |
| [10025](https://www.zaproxy.org/docs/alerts/10025/) | [Information Disclosure - Sensitive Information in HTTP Referrer Header](https://www.zaproxy.org/docs/alerts/10025/) | Informational | Passive |
| [10027](https://www.zaproxy.org/docs/alerts/10027/) | [Information Disclosure - Suspicious Comments](https://www.zaproxy.org/docs/alerts/10027/) | Informational | Passive |
| [10028](https://www.zaproxy.org/docs/alerts/10028/) | [Open Redirect](https://www.zaproxy.org/docs/alerts/10028/) |  | Passive |
| [10029](https://www.zaproxy.org/docs/alerts/10029/) | [Cookie Poisoning](https://www.zaproxy.org/docs/alerts/10029/) |  | Passive |
| [10030](https://www.zaproxy.org/docs/alerts/10030/) | [User Controllable Charset](https://www.zaproxy.org/docs/alerts/10030/) |  | Passive |
| [10031](https://www.zaproxy.org/docs/alerts/10031/) | [User Controllable HTML Element Attribute (Potential XSS)](https://www.zaproxy.org/docs/alerts/10031/) |  | Passive |
| [10032](https://www.zaproxy.org/docs/alerts/10032/) | [Viewstate](https://www.zaproxy.org/docs/alerts/10032/) |  | Passive |
| [10032-1](https://www.zaproxy.org/docs/alerts/10032-1/) | [Potential IP Addresses Found in the Viewstate](https://www.zaproxy.org/docs/alerts/10032-1/) | Medium | Passive |
| [10032-2](https://www.zaproxy.org/docs/alerts/10032-2/) | [Emails Found in the Viewstate](https://www.zaproxy.org/docs/alerts/10032-2/) | Medium | Passive |
| [10032-3](https://www.zaproxy.org/docs/alerts/10032-3/) | [Old Asp.Net Version in Use](https://www.zaproxy.org/docs/alerts/10032-3/) | Low | Passive |
| [10032-4](https://www.zaproxy.org/docs/alerts/10032-4/) | [Viewstate without MAC Signature (Unsure)](https://www.zaproxy.org/docs/alerts/10032-4/) | High | Passive |
| [10032-5](https://www.zaproxy.org/docs/alerts/10032-5/) | [Viewstate without MAC Signature (Sure)](https://www.zaproxy.org/docs/alerts/10032-5/) | High | Passive |
| [10032-6](https://www.zaproxy.org/docs/alerts/10032-6/) | [Split Viewstate in Use](https://www.zaproxy.org/docs/alerts/10032-6/) | Informational | Passive |
| [10033](https://www.zaproxy.org/docs/alerts/10033/) | [Directory Browsing](https://www.zaproxy.org/docs/alerts/10033/) |  | Passive |
| [10034](https://www.zaproxy.org/docs/alerts/10034/) | [Heartbleed OpenSSL Vulnerability (Indicative)](https://www.zaproxy.org/docs/alerts/10034/) |  | Passive |
| [10035](https://www.zaproxy.org/docs/alerts/10035/) | [Strict-Transport-Security Header](https://www.zaproxy.org/docs/alerts/10035/) |  | Passive |
| [10036](https://www.zaproxy.org/docs/alerts/10036/) | [HTTP Server Response Header](https://www.zaproxy.org/docs/alerts/10036/) |  | Passive |
| [10036-1](https://www.zaproxy.org/docs/alerts/10036-1/) | [Server Leaks its Webserver Application via 'Server' HTTP Response Header Field](https://www.zaproxy.org/docs/alerts/10036-1/) | Informational | Passive |
| [10036-2](https://www.zaproxy.org/docs/alerts/10036-2/) | [Server Leaks Version Information via 'Server' HTTP Response Header Field](https://www.zaproxy.org/docs/alerts/10036-2/) | Low | Passive |
| [10037](https://www.zaproxy.org/docs/alerts/10037/) | [Server Leaks Information via 'X-Powered-By' HTTP Response Header Field(s)](https://www.zaproxy.org/docs/alerts/10037/) | Low | Passive |
| [10038](https://www.zaproxy.org/docs/alerts/10038/) | [Content Security Policy (CSP) Header Not Set](https://www.zaproxy.org/docs/alerts/10038/) |  | Passive |
| [10038-1](https://www.zaproxy.org/docs/alerts/10038-1/) | [Content Security Policy (CSP) Header Not Set](https://www.zaproxy.org/docs/alerts/10038-1/) | Medium | Passive |
| [10038-2](https://www.zaproxy.org/docs/alerts/10038-2/) | [Obsolete Content Security Policy (CSP) Header Found](https://www.zaproxy.org/docs/alerts/10038-2/) | Informational | Passive |
| [10038-3](https://www.zaproxy.org/docs/alerts/10038-3/) | [Content Security Policy (CSP) Report-Only Header Found](https://www.zaproxy.org/docs/alerts/10038-3/) | Informational | Passive |
| [10039](https://www.zaproxy.org/docs/alerts/10039/) | [X-Backend-Server Header Information Leak](https://www.zaproxy.org/docs/alerts/10039/) |  | Passive |
| [10040](https://www.zaproxy.org/docs/alerts/10040/) | [Secure Pages Include Mixed Content](https://www.zaproxy.org/docs/alerts/10040/) |  | Passive |
| [10041](https://www.zaproxy.org/docs/alerts/10041/) | [HTTP to HTTPS Insecure Transition in Form Post](https://www.zaproxy.org/docs/alerts/10041/) |  | Passive |
| [10042](https://www.zaproxy.org/docs/alerts/10042/) | [HTTPS to HTTP Insecure Transition in Form Post](https://www.zaproxy.org/docs/alerts/10042/) |  | Passive |
| [10043](https://www.zaproxy.org/docs/alerts/10043/) | [User Controllable JavaScript Event (XSS)](https://www.zaproxy.org/docs/alerts/10043/) |  | Passive |
| [10044](https://www.zaproxy.org/docs/alerts/10044/) | [Big Redirect Detected (Potential Sensitive Information Leak)](https://www.zaproxy.org/docs/alerts/10044/) |  | Passive |
| [10045](https://www.zaproxy.org/docs/alerts/10045/) | [Source Code Disclosure - /WEB-INF folder](https://www.zaproxy.org/docs/alerts/10045/) | High | Active |
| [10050](https://www.zaproxy.org/docs/alerts/10050/) | [Retrieved from Cache](https://www.zaproxy.org/docs/alerts/10050/) |  | Passive |
| [10052](https://www.zaproxy.org/docs/alerts/10052/) | [X-ChromeLogger-Data (XCOLD) Header Information Leak](https://www.zaproxy.org/docs/alerts/10052/) |  | Passive |
| [10054](https://www.zaproxy.org/docs/alerts/10054/) | [Cookie without SameSite Attribute](https://www.zaproxy.org/docs/alerts/10054/) | Low | Passive |
| [10055](https://www.zaproxy.org/docs/alerts/10055/) | [CSP](https://www.zaproxy.org/docs/alerts/10055/) |  | Passive |
| [10055-1](https://www.zaproxy.org/docs/alerts/10055-1/) | [CSP: X-Content-Security-Policy](https://www.zaproxy.org/docs/alerts/10055-1/) | Low | Passive |
| [10055-2](https://www.zaproxy.org/docs/alerts/10055-2/) | [CSP: X-WebKit-CSP](https://www.zaproxy.org/docs/alerts/10055-2/) | Low | Passive |
| [10055-3](https://www.zaproxy.org/docs/alerts/10055-3/) | [CSP: Notices](https://www.zaproxy.org/docs/alerts/10055-3/) | Low | Passive |
| [10055-4](https://www.zaproxy.org/docs/alerts/10055-4/) | [CSP: Wildcard Directive](https://www.zaproxy.org/docs/alerts/10055-4/) | Medium | Passive |
| [10055-5](https://www.zaproxy.org/docs/alerts/10055-5/) | [CSP: script-src unsafe-inline](https://www.zaproxy.org/docs/alerts/10055-5/) | Medium | Passive |
| [10055-6](https://www.zaproxy.org/docs/alerts/10055-6/) | [CSP: style-src unsafe-inline](https://www.zaproxy.org/docs/alerts/10055-6/) | Medium | Passive |
| [10055-7](https://www.zaproxy.org/docs/alerts/10055-7/) | [CSP: script-src unsafe-hashes](https://www.zaproxy.org/docs/alerts/10055-7/) | Medium | Passive |
| [10055-8](https://www.zaproxy.org/docs/alerts/10055-8/) | [CSP: style-src unsafe-hashes](https://www.zaproxy.org/docs/alerts/10055-8/) | Medium | Passive |
| [10055-9](https://www.zaproxy.org/docs/alerts/10055-9/) | [CSP: Malformed Policy (Non-ASCII)](https://www.zaproxy.org/docs/alerts/10055-9/) | Medium | Passive |
| [10055-10](https://www.zaproxy.org/docs/alerts/10055-10/) | [CSP: script-src unsafe-eval](https://www.zaproxy.org/docs/alerts/10055-10/) | Medium | Passive |
| [10055-11](https://www.zaproxy.org/docs/alerts/10055-11/) | [CSP: Meta Policy Invalid Directive](https://www.zaproxy.org/docs/alerts/10055-11/) | Medium | Passive |
| [10055-12](https://www.zaproxy.org/docs/alerts/10055-12/) | [CSP: Header & Meta](https://www.zaproxy.org/docs/alerts/10055-12/) | Informational | Passive |
| [10056](https://www.zaproxy.org/docs/alerts/10056/) | [X-Debug-Token Information Leak](https://www.zaproxy.org/docs/alerts/10056/) | Low | Passive |
| [10057](https://www.zaproxy.org/docs/alerts/10057/) | [Username Hash Found](https://www.zaproxy.org/docs/alerts/10057/) | Informational | Passive |
| [10058](https://www.zaproxy.org/docs/alerts/10058/) | [GET for POST](https://www.zaproxy.org/docs/alerts/10058/) | Informational | Active |
| [10061](https://www.zaproxy.org/docs/alerts/10061/) | [X-AspNet-Version Response Header](https://www.zaproxy.org/docs/alerts/10061/) | Low | Passive |
| [10062](https://www.zaproxy.org/docs/alerts/10062/) | [PII Disclosure](https://www.zaproxy.org/docs/alerts/10062/) | High | Passive |
| [10096](https://www.zaproxy.org/docs/alerts/10096/) | [Timestamp Disclosure](https://www.zaproxy.org/docs/alerts/10096/) | Low | Passive |
| [10097](https://www.zaproxy.org/docs/alerts/10097/) | [Hash Disclosure](https://www.zaproxy.org/docs/alerts/10097/) |  | Passive |
| [10098](https://www.zaproxy.org/docs/alerts/10098/) | [Cross-Domain Misconfiguration](https://www.zaproxy.org/docs/alerts/10098/) | Medium | Passive |
| [10104](https://www.zaproxy.org/docs/alerts/10104/) | [User Agent Fuzzer](https://www.zaproxy.org/docs/alerts/10104/) | Informational | Active |
| [10105](https://www.zaproxy.org/docs/alerts/10105/) | [Weak Authentication Method](https://www.zaproxy.org/docs/alerts/10105/) |  | Passive |
| [10108](https://www.zaproxy.org/docs/alerts/10108/) | [Reverse Tabnabbing](https://www.zaproxy.org/docs/alerts/10108/) |  | Passive |
| [10109](https://www.zaproxy.org/docs/alerts/10109/) | [Modern Web Application](https://www.zaproxy.org/docs/alerts/10109/) |  | Passive |
| [10202](https://www.zaproxy.org/docs/alerts/10202/) | [Absence of Anti-CSRF Tokens](https://www.zaproxy.org/docs/alerts/10202/) |  | Passive |
| [20015](https://www.zaproxy.org/docs/alerts/20015/) | [Heartbleed OpenSSL Vulnerability](https://www.zaproxy.org/docs/alerts/20015/) | High | Active |
| [20017](https://www.zaproxy.org/docs/alerts/20017/) | [Source Code Disclosure - CVE-2012-1823](https://www.zaproxy.org/docs/alerts/20017/) | High | Active |
| [20018](https://www.zaproxy.org/docs/alerts/20018/) | [Remote Code Execution - CVE-2012-1823](https://www.zaproxy.org/docs/alerts/20018/) | High | Active |
| [20019](https://www.zaproxy.org/docs/alerts/20019/) | [External Redirect](https://www.zaproxy.org/docs/alerts/20019/) |  | Active |
| [20019-1](https://www.zaproxy.org/docs/alerts/20019-1/) | [External Redirect](https://www.zaproxy.org/docs/alerts/20019-1/) | High | Active |
| [20019-2](https://www.zaproxy.org/docs/alerts/20019-2/) | [External Redirect](https://www.zaproxy.org/docs/alerts/20019-2/) | High | Active |
| [20019-3](https://www.zaproxy.org/docs/alerts/20019-3/) | [External Redirect](https://www.zaproxy.org/docs/alerts/20019-3/) | High | Active |
| [20019-4](https://www.zaproxy.org/docs/alerts/20019-4/) | [External Redirect](https://www.zaproxy.org/docs/alerts/20019-4/) | High | Active |
| [30001](https://www.zaproxy.org/docs/alerts/30001/) | [Buffer Overflow](https://www.zaproxy.org/docs/alerts/30001/) | Medium | Active |
| [30002](https://www.zaproxy.org/docs/alerts/30002/) | [Format String Error](https://www.zaproxy.org/docs/alerts/30002/) | Medium | Active |
| [40003](https://www.zaproxy.org/docs/alerts/40003/) | [CRLF Injection](https://www.zaproxy.org/docs/alerts/40003/) | Medium | Active |
| [40008](https://www.zaproxy.org/docs/alerts/40008/) | [Parameter Tampering](https://www.zaproxy.org/docs/alerts/40008/) | Medium | Active |
| [40009](https://www.zaproxy.org/docs/alerts/40009/) | [Server Side Include](https://www.zaproxy.org/docs/alerts/40009/) | High | Active |
| [40012](https://www.zaproxy.org/docs/alerts/40012/) | [Cross Site Scripting (Reflected)](https://www.zaproxy.org/docs/alerts/40012/) | High | Active |
| [40014](https://www.zaproxy.org/docs/alerts/40014/) | [Cross Site Scripting (Persistent)](https://www.zaproxy.org/docs/alerts/40014/) | High | Active |
| [40016](https://www.zaproxy.org/docs/alerts/40016/) | [Cross Site Scripting (Persistent) - Prime](https://www.zaproxy.org/docs/alerts/40016/) | Informational | Active |
| [40017](https://www.zaproxy.org/docs/alerts/40017/) | [Cross Site Scripting (Persistent) - Spider](https://www.zaproxy.org/docs/alerts/40017/) | Informational | Active |
| [40018](https://www.zaproxy.org/docs/alerts/40018/) | [SQL Injection](https://www.zaproxy.org/docs/alerts/40018/) | High | Active |
| [40019](https://www.zaproxy.org/docs/alerts/40019/) | [SQL Injection - MySQL](https://www.zaproxy.org/docs/alerts/40019/) | High | Active |
| [40020](https://www.zaproxy.org/docs/alerts/40020/) | [SQL Injection - Hypersonic SQL](https://www.zaproxy.org/docs/alerts/40020/) | High | Active |
| [40021](https://www.zaproxy.org/docs/alerts/40021/) | [SQL Injection - Oracle](https://www.zaproxy.org/docs/alerts/40021/) | High | Active |
| [40022](https://www.zaproxy.org/docs/alerts/40022/) | [SQL Injection - PostgreSQL](https://www.zaproxy.org/docs/alerts/40022/) | High | Active |
| [40024](https://www.zaproxy.org/docs/alerts/40024/) | [SQL Injection - SQLite](https://www.zaproxy.org/docs/alerts/40024/) | High | Active |
| [40026](https://www.zaproxy.org/docs/alerts/40026/) | [Cross Site Scripting (DOM Based)](https://www.zaproxy.org/docs/alerts/40026/) | High | Active |
| [40027](https://www.zaproxy.org/docs/alerts/40027/) | [SQL Injection - MsSQL](https://www.zaproxy.org/docs/alerts/40027/) | High | Active |
| [40028](https://www.zaproxy.org/docs/alerts/40028/) | [ELMAH Information Leak](https://www.zaproxy.org/docs/alerts/40028/) | Medium | Active |
| [40029](https://www.zaproxy.org/docs/alerts/40029/) | [Trace.axd Information Leak](https://www.zaproxy.org/docs/alerts/40029/) | Medium | Active |
| [40032](https://www.zaproxy.org/docs/alerts/40032/) | [.htaccess Information Leak](https://www.zaproxy.org/docs/alerts/40032/) | Medium | Active |
| [40034](https://www.zaproxy.org/docs/alerts/40034/) | [.env Information Leak](https://www.zaproxy.org/docs/alerts/40034/) | Medium | Active |
| [40035](https://www.zaproxy.org/docs/alerts/40035/) | [Hidden File Found](https://www.zaproxy.org/docs/alerts/40035/) | Medium | Active |
| [90001](https://www.zaproxy.org/docs/alerts/90001/) | [Insecure JSF ViewState](https://www.zaproxy.org/docs/alerts/90001/) | Medium | Passive |
| [90011](https://www.zaproxy.org/docs/alerts/90011/) | [Charset Mismatch](https://www.zaproxy.org/docs/alerts/90011/) | Informational | Passive |
| [90017](https://www.zaproxy.org/docs/alerts/90017/) | [XSLT Injection](https://www.zaproxy.org/docs/alerts/90017/) | Medium | Active |
| [90019](https://www.zaproxy.org/docs/alerts/90019/) | [Server Side Code Injection](https://www.zaproxy.org/docs/alerts/90019/) |  | Active |
| [90019-1](https://www.zaproxy.org/docs/alerts/90019-1/) | [Server Side Code Injection - PHP Code Injection](https://www.zaproxy.org/docs/alerts/90019-1/) | High | Active |
| [90019-2](https://www.zaproxy.org/docs/alerts/90019-2/) | [Server Side Code Injection - ASP Code Injection](https://www.zaproxy.org/docs/alerts/90019-2/) | High | Active |
| [90020](https://www.zaproxy.org/docs/alerts/90020/) | [Remote OS Command Injection](https://www.zaproxy.org/docs/alerts/90020/) | High | Active |
| [90022](https://www.zaproxy.org/docs/alerts/90022/) | [Application Error Disclosure](https://www.zaproxy.org/docs/alerts/90022/) | Medium | Passive |
| [90023](https://www.zaproxy.org/docs/alerts/90023/) | [XML External Entity Attack](https://www.zaproxy.org/docs/alerts/90023/) | High | Active |
| [90024](https://www.zaproxy.org/docs/alerts/90024/) | [Generic Padding Oracle](https://www.zaproxy.org/docs/alerts/90024/) | High | Active |
| [90033](https://www.zaproxy.org/docs/alerts/90033/) | [Loosely Scoped Cookie](https://www.zaproxy.org/docs/alerts/90033/) | Informational | Passive |
| [90034](https://www.zaproxy.org/docs/alerts/90034/) | [Cloud Metadata Potentially Exposed](https://www.zaproxy.org/docs/alerts/90034/) | High | Active |
| [110001](https://www.zaproxy.org/docs/alerts/110001/) | [Application Error Disclosure via WebSockets](https://www.zaproxy.org/docs/alerts/110001/) | Medium | WebSocket Passive |
| [110002](https://www.zaproxy.org/docs/alerts/110002/) | [Base64 Disclosure in WebSocket message](https://www.zaproxy.org/docs/alerts/110002/) | Informational | WebSocket Passive |
| [110003](https://www.zaproxy.org/docs/alerts/110003/) | [Information Disclosure - Debug Error Messages via WebSocket](https://www.zaproxy.org/docs/alerts/110003/) | Low | WebSocket Passive |
| [110004](https://www.zaproxy.org/docs/alerts/110004/) | [Email address found in WebSocket message](https://www.zaproxy.org/docs/alerts/110004/) | Informational | WebSocket Passive |
| [110005](https://www.zaproxy.org/docs/alerts/110005/) | [Personally Identifiable Information via WebSocket](https://www.zaproxy.org/docs/alerts/110005/) | High | WebSocket Passive |
| [110006](https://www.zaproxy.org/docs/alerts/110006/) | [Private IP Disclosure via WebSocket](https://www.zaproxy.org/docs/alerts/110006/) | Low | WebSocket Passive |
| [110007](https://www.zaproxy.org/docs/alerts/110007/) | [Username Hash Found in WebSocket message](https://www.zaproxy.org/docs/alerts/110007/) | Informational | WebSocket Passive |
| [110008](https://www.zaproxy.org/docs/alerts/110008/) | [Information Disclosure - Suspicious Comments in XML via WebSocket](https://www.zaproxy.org/docs/alerts/110008/) | Informational | WebSocket Passive |
| [10205-2](https://www.zaproxy.org/docs/alerts/10205-2/) | [Quantum Cryptography Alert](https://www.zaproxy.org/docs/alerts/10205-2/) | High | Active |
