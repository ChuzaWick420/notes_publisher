---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-12-04
---

<span style="color: gray;">Dated: 04-12-2024</span>

# Ch03. case Study Security Hardening - Php Version X

- PHP Security Guidelines
- https://docs.php.earth/security/intro/
- Cross site scripting (XSS)
- Injections
    - SQL injection
    - Directory traversal (path injection)
    - Command injection
    - Code injection
- Cross site request forgery (XSRF/CSRF)
- Public files
- Passwords
- Uploading files
- Session hijacking
- Remote file inclusion
- PHP configuration
    - Error reporting
    - Exposing PHP version
    - Remote files
    - Open_basedir
    - Session settings
- Use HTTPS
- Things not listed
- PHP Configuration
	- Always keep the installed PHP version updated.
	- You can use versionscan to check for possible vulnerabilities of your PHP version.
	- Update open source libraries and applications, and keep your web server well maintained.  
	- Here are some of the important settings from php.ini that you should check out. You can also use **iniscan** to scan your php.ini files for best security practices.
- Error Reporting:  
   In your production environment, you must always turn off displaying errors to the screen. If errors occur in your application and they are visible to the outside world, an attacker could get valuable data for attacking your application. 

```php
; Disable displaying errors to screen
display_errors = off
; Enable writing errors to server logs
log_errors = on
```