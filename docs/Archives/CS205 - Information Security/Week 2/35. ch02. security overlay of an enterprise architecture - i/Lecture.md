---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-12
---

<span style="color: gray;">Dated: 12-11-2024</span>

# Ch02. Security Overlay of an Enterprise Architecture - 1

- How is the enterprise secured with the help of various components and security design?

![[Pasted image 20241112142101.png]]

| **Security Challenge**                      | **Location/Device**                  | **Security Solution**                         |
| ------------------------------------------- | ------------------------------------ | --------------------------------------------- |
| Perimeter Filtering                         | Edge Router                          | Access Lists & Various RFCs                   |
| DDOS Attack                                 | Edge Router/DDOS Protection Solution | DDOS Protection                               |
| Zero-Day Attack / APT Attack                | Edge Device / Edge NGN FW            | Zero-Day/APT Attack Prevention                |
| Web Server Attacks                          | DMZ / Web Application FW             | Web Application Attack Prevention             |
| Email SPAM &                                | DMZ / Email                          | Email Security                                |
| Security Challenge                          | Location/Device                      | Security Solution                             |
| Web-based User Attacks                      | DMZ / Web Security GW                | Web Filtering & Malware Protection            |
| System Malware                              | System                               | AV                                            |
| User Network Access Control                 | At Aggregation Point Of User Access  | Network Admission Control (NAC)               |
| User Controls For USB/Media, HDD Encrypt    | System                               | Data Loss Prevention (DPL) - System Level     |
| Remote Branch Connectivity/ Malware         | Intranet-Extranet Edge / UTM         | Unified Threat Management (UTM) Solution      |
| Security Challenge                          | Location/Device                      | Security Solution                             |
| Unauthorized Access / Malware               | Data Center FW                       | Data Center FW Filtering & Malware Protection |
| Data Exfiltration                           | Edge / Network DLP                   | Network DLP Solution                          |
| Event Monitoring & Detection                | Data Center / SIEM                   | Security Info. & Event Management             |
| Unpatched Systems                           | Data Center / VM                     | Vulnerability Scanner                         |
| Server Integrity Monitoring & IPS Filtering | Data Center / HIPS                   | Host Intrusion Prevention System (HIPS)       |
