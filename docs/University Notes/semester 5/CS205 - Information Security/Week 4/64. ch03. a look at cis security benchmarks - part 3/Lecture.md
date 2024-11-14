---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-14
---

<span style="color: gray;">Dated: 14-11-2024</span>

# Ch03. a Look at Cis Security Benchmarks - part 3

- CIS Benchmarks example (Network Devices)  
![[Pasted image 20241114141902.png]]

- Control content:
    - Profile applicability (ASA 8.X, ASA 9.X)
    - Description
    - Rationale
    - Audit
    - Remediation
    - Default value
    - References

- 1.8 (page 88); Session Timeout
    - Profile applicability: Level 1, Cisco ASA9.X
    - Description: Sets the idle timeout for a console session before the security appliance terminates it.
    - Rationale: Limiting session timeout prevents unauthorized users from using abandoned sessions to perform malicious activities.
    - Default Value: The default timeout is 0, which means the console session will not time out.
	- Reference: CLI Book 1: Cisco ASA Series General Operations CLI Configuration Guide, 9.1

![[Pasted image 20241114141923.png]]  
![[Pasted image 20241114141928.png]]