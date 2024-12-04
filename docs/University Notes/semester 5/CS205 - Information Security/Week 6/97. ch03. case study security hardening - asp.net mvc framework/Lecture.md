---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-12-04
---

<span style="color: gray;">Dated: 04-12-2024</span>

# Ch03. case Study Security Hardening - asp.net Mvc Framework

- ASP.NET MVC Security Guidelines
- https://www.owasp.org/index.php/.NET_Security_Cheat_Sheet#ASP.NET_MVC_Guidance
- ASP.NET MVC (Model-View-Controller) is a contemporary web application framework that uses more standardized HTTP communication than the Web Forms postback model.
- The OWASP Top 10 lists the most prevalent and dangerous threats to web security in the world today and is reviewed every 3 years.
- After covering the top 10 it is generally advisable to assess for other threats or get a professional Penetration Test.
- Your approach to securing your web application should be to start at the top threat A1 below and work down, this will ensure that any time spent on security will be spent most effectively and cover the top threats first and lesser threats afterwards.
- A.6 sensitive data exposure
	- DO NOT: Store encrypted passwords.
	- DO: Use a strong hash to store password credentials. Use PBKDF2, BCrypt or SCrypt with at least 8000 iterations and a strong key.
	- DO: Enforce passwords with a minimum complexity that will survive a dictionary attack i.e. longer passwords that use the full character set (numbers, symbols and letters) to increase the entropy.
	- DO: Use a strong encryption routine such as AES-512 where personally identifiable data needs to be restored to it's original format. Do not encrypt passwords. Protect encryption keys more than any other asset.
	- Apply the following test:
	    - Would you be happy leaving the data on a spreadsheet on a bus for everyone to read.
	    - Assume the attacker can get direct access to your database and protect it accordingly.
	- DO: Use TLS 1.2 for your entire site. Get a free certificate from StartSSL.com or LetsEncrypt.org.
	- DO NOT: Allow SSL, this is now obsolete.
	- DO: Have a strong TLS policy (see SSL Best Practices), use TLS 1.2 wherever possible. Then check the configuration using SSL Test
	- DO: Ensure headers are not disclosing information about your application.
	- See HttpHeaders.cs, Dio nach StripHeaders or disable via web.config