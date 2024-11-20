---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-15
---

<span style="color: gray;">Dated: 15-11-2024</span>

# Ch03. case Study - Security Hardening - Linux Server

- CIS Benchmarks case study (Red Hat Enterprise Linux 7)
- 5.2.2 (page 258): Ensure SSH Protocol is set to 2 (Scored)
- Profile applicability:
    - Level 1, Server
    - Level 1, Workstation
- Description: SSH supports 2 different and incompatible protocols: SSH1 and SSH2. SSH1 was the original protocol & was subject to security issues. SSH2 is more advanced and secure.
- Rationale: SSH v1 suffers from insecurities that do not affect SSH v2.
- Audit: Run the following command and verify that output matches:

```bash
grep "^Protocol" /etc/ssh/sshd_config
```

```
Protocol 2
```

- Remediation: Edit the `/etc/ssh/sshd_config` file to set the parameter as follows:

```
Protocol 2
```

- Critical Controls: 3.4
    - Use Only Secure Channels For Remote System Administration