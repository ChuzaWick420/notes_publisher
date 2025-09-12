---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-12-03
---

<span style="color: gray;">Dated: 03-12-2024</span>

# Ch03. case Study Security Hardening - Network Layer 3 Switch

- Infrastructure Layer 3 Switch STIG
- DISA, Release 22
    - - 28 April, 2017

- General Information:
    - Rule Title: The administrator must ensure that all L2TPv3 sessions are authenticated prior to transporting traffic.
	- Vuln ID: V-30744
	- STIG ID: NET-TUNL-034
	- Severity: CAT II
- Discussion:
	- L2TPv3 sessions can be used to transport layer-2 protocols across an IP backbone. These protocols were intended for link-local scope only and are therefore less defended and not as well-known.
	- As stated in DoD IPv6 IA Guidance for MO3 (S4-C7-1), the L2TP tunnels can also carry IP packets that are very difficult to filter because of the additional encapsulation.  
	- Hence, it is imperative that L2TP sessions are authenticated prior to transporting traffic.
- Check Content:
	- Review the router or multi-layer switch configuration and determine if L2TPv3 has been configured to provide transport across an IP network. If it has been configured, verify that the L2TPv3 session requires authentication.
	- See details explanation in Check Content (Configurations)
- Fix Text:
    - Configure L2TPv3 to use authentication for any peering sessions.