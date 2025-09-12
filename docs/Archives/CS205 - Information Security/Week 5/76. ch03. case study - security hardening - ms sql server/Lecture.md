---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-15
---

<span style="color: gray;">Dated: 15-11-2024</span>

# Ch03. case Study - Security Hardening - Ms Sql Server

- 2.14 Ensure 'sa' Login Account has been renamed (Scored)
- Profile applicability:
    - Level 1 database engine
- Description: The sa account is a widely known and often widely used SQL Server account with sysadmin privileges.
- Rationale: It is more difficult to launch password-guessing and brute-force attacks against the sa account if the username is not known.
- Audit: Use the following syntax to determine if the sa account is renamed

```sql
SELECT name FROM sys.server_principals WHERE sid=0x01;
```

- Audit: A name of sa indicates the account has not been renamed
- Remediation: Replace the different_user value within the below syntax and execute rename the sa login:

```sql
ALTER LOGIN sa WITH NAME = <different_user>;
```

- Impact: It is not a good security practice to code applications or scripts to use the sa account
- Impact: … However, if this has been done renaming the sa account will prevent scripts and applications for authenticating to the database server and executing required tasks or functions.
- Default Value: By default, the 'sa' account name is 'sa'
- References:
	- https://msdn.microsoft.com/en-us/library/ms144284(v=sql.110).aspx
	- (Choose An Authentication Mode)