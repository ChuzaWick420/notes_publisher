---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-15
---

<span style="color: gray;">Dated: 15-11-2024</span>

# Ch03. case Study - Security Hardening - Oracle Solaris Server

- Oracle Database 12c
- DISA, Release 18
    - 28 April 2017

![[Pasted image 20241115151904.png]]

- General Information:
    - Rule Title: The Oracle Listener must be configured to require administration authentication
    - STIG ID: 0121-BP-022700
    - Severity: CAT I
- Discussion:
    - Oracle listener authentication helps prevent unauthorized administration of the Oracle listener.
    - Unauthorized administration of the listener could lead to DoS exploits;  
	- loss of connection audit data, unauthorized reconfiguration or other unauthorized access. This is a Category I finding because privileged access to the listener is not restricted to authorized users.
	- Unauthorized access can result in stopping of the listener (DoS) and overwriting of listener audit logs.
- Check Content:
    - If a listener is not running on the local database host server, this check is not a finding.
	- For Windows hosts, view all Windows services with TNSListener embedded in the service name.
	- The service name format is: `Oracle[ORACLE_HOME_NAME]TNSListener`
	- View the STIGVIEWER for Unix hosts
- Fix Text:
    - By default, Oracle Net Listener permits only local administration for security reasons. As a policy, the listener can be administered only by the user who started it. This is enforced through local operating system authentication.
	- For example, if user1 starts the listener, then only user1 can administer it. Any other user trying to administer the listener gets an error. The super user is the only exception.
	- Remote administ. of the listener must not be permitted. If listener administ. from a remote system is required, granting secure remote access to the Oracle DBMS server and performing local administration is preferred.
- CCI (Control Correlation Identifier):
    - CCI: CCI-000366
    - The organization implements the security configuration settings.
	- NIST SP 800-53 :: CM-6 b
	- NIST SP 800-53A :: CM-6.1 (iv)
	- NIST SP 800-53 Revision 4 :: CM-6 b