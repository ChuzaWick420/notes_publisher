---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-14
---

<span style="color: gray;">Dated: 15-11-2024</span>

# Ch03. a Look at Disa Security Technical Implementation Guides (stigs) - part 4

- Firewall Security Technical Implementation Guide
- Vulnerability ID: V-3967
- Rule name: The console port does not timeout after 10 mins

![[Pasted image 20241115130818.png]]

- General Information:
    - Rule Title: The network devices must time out access to the console port at 10 minutes or less of inactivity
    - STIG ID: NET1624
    - Severity: CAT II
- Discussion:
    - Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console
	- port that has been left unattended. In addition quickly terminating an idle session will also free up resources committed by the managed network device. Setting the timeout of the session to 10 minutes
	- or less increases the level of protection afforded critical network components
- Check Content:
    - Review the configuration and verify a session using the console port will time out after 10 mins or less of inactivity.
    - If console access is not configured to timeout at 10 minutes or less, this is a finding.
- Fix Text:
    - Configure the timeout for idle console connection to 10 minutes or less.

> [!QUESTION]- In the context of DISA STIGs, configuring the rule that the network devices must time out access to console port at 5 minutes of inactivity falls into _ category of severity.  
> - [x] CAT 2  
> - [ ] CAT 1  
> - [ ] CAT 5  
> - [ ] CAT 3