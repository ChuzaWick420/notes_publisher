---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-12-02
---

<span style="color: gray;">Dated: 02-12-2024</span>

# Ch03. case Study Security Hardening - Mozilla Firefox

- CIS Benchmarks case study (Mozilla Firefox)
- 3.5 (L2) Enable IDN Show Punycode (Scored)
- Profile applicability:
    - Level 2
- Description: This feature determines whether all Internationalized Domain Names (IDNs) displayed in the browser are displayed as Punycode or as Unicode.
- Rationale: IDNs displayed in Punycode are easier to identify and therefore help mitigate the risk of accessing spoofed web pages.
- Audit: Perform the following procedure:
    1. Type `about:config` in the address bar
    2. Type `network.IDN_show_punycode` in the filter
    3. Ensure the preferences listed are set to the values specified below

```
network.IDN_show_punycode=true
```

- 3.5 (L2) Enable IDN Show Punycode (Scored)
    - Remediation:
        1. Open the `mozilla.cfg` file in the installation directory with a text editor
        2. Add the following lines to `mozilla.cfg`:  

```
lockPref("network.IDN_show_punycode", true);
```

- Default value: false