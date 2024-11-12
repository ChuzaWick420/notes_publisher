---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-12
---

<span style="color: gray;">Dated: 12-11-2024</span>

# Ch02. Security Overlay of an Enterprise Architecture - 3 (general Security design)

## General Security Design Principles

![[Pasted image 20241112152537.png]]

1. Block unauthorized traffic at edge (direct public www traffic to DMZ web server)
2. Edge malware protection & DMZ
3. Web & email are important vectors to secure against malware and attacks
4. NGN-FW (may be found in a UTM as well)
5. Web security GW and email anti-spam GW solutions
6. Granular access list filtering in edge and data center FWs (source, destination, and traffic type/port)
7. A good AV solution, and keep virus definitions updated
8. Monthly VM scans

## More Advanced Security

- APT & zero-day attack prevention
- SIEM solution
- Network DLP and system DLP
- Network admission control (NAC)
- Server HIPS
- Web application FW (WAF)

## Even More Advanced Security

- Network forensics
- Host-based APT / IoC solution
- Identity & access management (IAM)
- Privileged identity management (PIM)
- Database security solution

## Guidelines for Strong Security Controls

- CIS 20 critical security controls

![[Pasted image 20241112152506.png]]