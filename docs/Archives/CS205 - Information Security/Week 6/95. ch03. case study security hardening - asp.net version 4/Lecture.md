---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-12-03
---

<span style="color: gray;">Dated: 03-12-2024</span>

# Ch03. case Study Security Hardening - asp.net Version 4

- OWASP ASP.NET Cheat Sheet
- https://www.owasp.org/index.php/.NET_Security_Cheat_Sheet
- .NET Framework Guidance
- ASP.NET Web Forms Guidance
- ASP.NET MVC Framework Guidance
- Data access
- Encryption
- General guidelines
- .NET Framework, Data Access Guidance
	- Use Parameterized SQL commands for all data access, without exception.
	- Do not use SqlCommand with a string parameter made up of a concatenated SQL String.
	- Whitelist allowable values coming from the user.
	- Use enums, TryParse or lookup values to assure that the data coming from the user is as expected.
	- Apply the principle of least privilege when setting up the Database User in your database of choice. The database user should only be able to access items that make sense for the use case.
	- Use of the Entity Framework is a very effective SQL injection prevention mechanism. When using SQL Server, prefer integrated authentication over SQL authentication.
	- Use Always Encrypted where possible for sensitive data (SQL Server 2016 and SQL Azure)
- .NET Framework, General Guidance
	- Lock down the config file.
	- Remove all aspects of configuration that are not in use.
	- Encrypt sensitive parts of the web.config using aspnet_regiis -pe
	- For Click Once applications the .Net Framework should be upgraded to use version 4.6.2 to ensure TLS 1.1/1.2 support.
- ASP.NET Web Forms Guidance
	- HTTPS & some general configuration
	- HTTP validation & encoding
	- Forms authentication
	- ASP.NET MVC (Model-View-Controller) is a contemporary web application framework that uses more standardized HTTP communication
	- Based on OWASP Top 10
