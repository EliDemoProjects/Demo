# Authentication Support

Currently, our DAST engine can run scans using the following authentication types:

- No authentication
- Browser-based pop-up authentication
- Form-based authentication
- JSON-based authentication
- Basic HTTP/NTLM authentication
- Single Sign-On (using custom scripts)
- Multi-step authentication (using custom scripts)
- Single Sign-On (Using ZEST script from ZAP browser extension)
- Multi-step authentication (Using ZEST script from ZAP browser extension)
- Multi-factor Authentication (TOTP Only) (Only supported via onboarding wizard)

Authentication types not supported:

- Multi-factor authentication
- Single sign-on using encryption or decryption methods
- Multi-step authentication using encryption or decryption methods
- Dynamic credentials
- Knowledge-based
- OTP-based authentication
- CAPTCHA authentication
- Operating system pop-up authentication
- IWA (Integrated Windows Authentication)
