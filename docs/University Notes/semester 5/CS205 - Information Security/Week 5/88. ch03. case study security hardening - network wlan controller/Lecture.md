---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-12-02
---

<span style="color: gray;">Dated: 02-12-2024</span>

# Ch03. case Study Security Hardening - Network Wlan Controller

- WLAN Controller STIG
- DISA, Release 12
    - - 28 Oct, 2016  
![[Pasted image 20241202210502.png]]
- General Information:
    - Rule Title: WLAN must use EAP-TLS
	- Vuln ID: V-3692
	- STIG ID: WIR0115-01
	- Severity: CAT II
- Discussion:
    - EAP-TLS provides strong cryptographic mutual authentication and key distribution services not found in other EAP methods, and thus provides significantly more protection against attacks than other methods. Additionally, EAP-TLS supports two-factor user authentication on the WLAN client, which provides significantly more protection than methods that rely on a password or certificate alone.
	- EAP-TLS also can leverage DoD CAC in its authentication services, providing additional security and convenience.
- Check Content:
    - NOTE: If the equipment is WPA2 certified, then it is capable of supporting this requirement.
    - Review the WLAN equipment configuration to check EAP-TLS is actively used and no other methods are enabled.
	- Mark as a finding if either EAP-TLS is not used or if the WLAN system allows users to connect with other methods.
- Fix Text:
    - Change the WLAN configuration so it supports EAP-TLS, implementing supporting PKI and AAA infrastructure as necessary.
	- If the WLAN equipment is not capable of supporting EAP-TLS, procure new equipment capable of such support.