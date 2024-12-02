---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-12-02
---

<span style="color: gray;">Dated: 02-12-2024</span>

# Ch03. case Study Security Hardening Active Directory (ad)

- Active Directory Domain
- DISA, Release 8
    - - 27 January, 2017
![[Pasted image 20241202190409.png]]
- General Information:
    - Rule Title: Membership to the Domain Admins group must be restricted to accounts used only to manage the Active Dir domain and domain controllers
    - STID ID: AD.0002
    - Severity: CAT I
- Discussion:
    - The Domain Admins group is a highly privileged group. Personnel who are system administrators must log on to Active Directory systems only using accounts with the level of authority necessary.
    - Only system administrator accounts used exclusively to manage an Active Directory domain and domain controllers may be members of the Domain Admins group. A separation of administrator responsibilities helps mitigate the risk of privilege escalation resulting from credential theft attacks.
- Check Content:
    - Review the Domain Admins group in Active Directory Users and Computers. Each Domain Administrator must have a separate unique account specifically for managing the Active Directory domain and domain controllers.
	- If any account listed in the Domain Admins group is a member of other administrator groups including the Enterprise Admins group, domain member server administrators groups, or domain workstation administrators groups, this is a finding.
- Fix Text:
    - Create the necessary documentation that identifies the members of the Domain Admins group. Ensure that each member has a separate unique account that can only be used to manage the Active Directory domain and domain controllers. Remove any Domain Admin accounts from other administrator groups.
- CCI (Control Correlation Identifier):
    - CCI-000366
    - The organization implements the security configuration settings.
    - NIST SP 800-53 :: CM-6 b
    - NIST SP 800-53A :: CM-6.1 (iv)
    - NIST SP 800-53 Revision 4 :: CM-6 b
    - Revision 4 :: CM-6 b
