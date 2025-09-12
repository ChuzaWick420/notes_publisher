---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-12-02
---

<span style="color: gray;">Dated: 02-12-2024</span>

# Ch03. case Study Security Hardening - Network Routers

- CIS Benchmarks case study (Cisco IOS 15)
- For Cisco routers running IOS 15M
- 3.3.2.2 Set `ip ospf message-digest-key md5` (Scored)
- Profile applicability:
    - Level 2
- Description: Enable Open Shortest Path First (OSPF) Message Digest 5 (MD5) authentication.
- Rationale: This is part of the OSPF authentication setup
- Audit: Verify the appropriate md5 key is defined on the appropriate interface(s)

```
hostname#sh run int {interface}
```

- Remediation:  

```
hostname(config)#interface {interface_name} hostname(config-if)#ip ospf message-digest-key {ospf_mds_key-id} md5 {ospf_md5_key}
```

- Impact:
    - Organizations should plan and implement enterprise security policies that require rigorous authentication methods for routing protocols. Configuring the proper interface(s) for `ip ospf message-digest-key md5` enforces these policies by restricting exchanges between network devices.
- Default value: not set