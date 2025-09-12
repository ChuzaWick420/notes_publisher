---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-15
---

<span style="color: gray;">Dated: 15-11-2024</span>

# Ch03. case Study - Security Hardening Oracle Db Server

- Oracle database 11.2g
- DISA, Release 11
    - 28 April 2017

![[Pasted image 20241115153504.png]]

- General Information:
    - Rule Title: The Oracle REMOTE_OS_ROLES parameter must be set to FALSE.
    - STIG ID: 0112-BP-022000
    - Severity: CAT I
- Discussion:
    - Setting REMOTE_OS_ROLES to TRUE allows operating system groups to control Oracle roles. The default value of FALSE causes roles to be identified and managed by the database If REMOTE_OS_ROLES is set to TRUE, a remote user could impersonate another operating system user over a network connection.
- Check Content:
    - From SQL\*Plus:  

```sql
select value from v$parameter where name = 'remote_os_roles';
```

    - If the returned value is not FALSE or not documented in the System Security Plan as required, this is a Finding

- Fix Text:
    - Document remote OS roles in the System Security Plan.
    - If not required, disable use of remote OS roles.
    - From SQL\*Plus:  

```sql
alter system set remote_os_roles = FALSE scope = spfile;
```

	- The above SQL\*Plus command will set the parameter to take effect at next system startup
- CCI (Control Correlation Identifier):
    - CCI: CCI-000366
    - The org implements the security configuration settings.
    - NIST SP 800-53 :: CM-6 b
    - NIST SP 800-53A :: CM-6.1 (iv)
    - NIST SP 800-53 Revision 4 :: CM-6 b