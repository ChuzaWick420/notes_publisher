---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-12-02
---

<span style="color: gray;">Dated: 02-12-2024</span>

# Ch03. case Study Security Hardening - Network Fw

- Firewall STIG
- DISA, Release 22
    - 28 April, 2017  
![[Pasted image 20241202194243.png]]
- General Information:
    - Rule Title: The device must be configured to protect the network against denial of service attacks such as Ping of Death, TCP SYN floods, etc.
	- Vuln ID: V-3156
	- STIG ID: NET0375
	- Severity: CAT II
- Discussion:
    - A SYN-flood attack is a denial-of-service attack where the attacker sends a huge amount of please-start-a-connection packets and then nothing else. This causes the device being attacked to be overloaded with the open sessions and eventually crash.
	- A ping sweep (also known as an ICMP sweep) is a basic network scanning technique used to determine which of a range of IP addresses map to live hosts (computers)
- Check Content:
    - Review the device configurations to determine if denial of service attacks guarded against.
    - If the device is not configured to mitigate denial of service attacks, this is a finding.
- Fix Text:
    - If the firewall support SYN-flood or ping sweep protection then enable these features. If the firewall does not support these features, enable the security features on the router to protect the network from these attacks.
- CCI (Control Correlation Identifier):
    - (Misc info)