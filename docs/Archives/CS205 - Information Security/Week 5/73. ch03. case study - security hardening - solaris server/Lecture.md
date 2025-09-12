---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-15
---


<span style="color: gray;">Dated: 15-11-2024</span>

# Ch03. case Study - Security Hardening - Solaris Server

- Solaris 10 X86
- DISA, Release 18
    - 28 April 2017

![[Pasted image 20241115145620.png]]

- General Information:
    - Rule Title: All shell files must have mode 0755 or less permissive
    - STIG ID: GEN002220
    - Severity: CAT I
- Discussion:
    - Shells with world/group-write permissions give the ability to maliciously modify the shell to obtain unauthorized access.
- Check Content:
    - If /etc/shells exists, check the group ownership of each shell referenced.

```bash
cat /etc/shells | xargs -n1 ls -lL
```

    - Otherwise, check any shells found on the system.

```bash
find / -name "*.sh" | xargs -n1 ls -lL
```

	- If a shell has a mode more permissive than 0755, this is a finding

- Fix Text:
    - Change the mode of the shell

```bash
chmod 0755 <shell>
```

- CCI (Control Correlation Identifier):
    - CCI-000225
    - The organization employs the concept of least privilege, allowing only authorized accesses for users (and processes acting on behalf of users) which are necessary to accomplish assigned tasks in accordance with organizational missions and business functions.
	- NIST SP 800-53 :: AC-6
	- NIST SP 800-53A :: AC-6.1
	- NIST SP 800-53 Revision 4 :: AC-6