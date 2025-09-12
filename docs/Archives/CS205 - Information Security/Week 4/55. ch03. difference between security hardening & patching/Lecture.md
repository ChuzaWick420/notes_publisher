---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-14
---

<span style="color: gray;">Dated: 14-11-2024</span>

# Ch03. Difference between Security Hardening and Patching

- Security Transformation Stage
    - 1: Security Hardening of IT Assets

## Security Hardening

- IT assets such as hardware and software come with default (insecure) configurations which become the basis for attacks
- Typical case in point: username and password: "admin, admin"
- Process of securing a system by reducing its surface of vulnerability, which is larger when a system performs more functions; in principle a single-function system is more secure than a multipurpose one (Wikipedia)

## Patching

- Fixing vulnerabilities (which may be exploited by malware or attackers) in software or firmware with vendor released patches (auto or manual updates)
- Patches are also called fixes

### Patching Considerations

- Vendors release patch when they become aware of a vulnerability
- Patches may be rolled up into a release
- Off-the shelf software works well but testing required for customized instances

## Hardening

- Includes additional steps beyond patching to limit the ways a hacker or malware could gain entry.
- Accomplished by turning on only the ports and services required, secure configuration of services & additional steps to limit system access

---

- Note that both hardening & patching are required
    - Hardening prevents existing and future vulnerabilities by tightening configuration
    - Patching is more of a vendor driven process but essential nonetheless
