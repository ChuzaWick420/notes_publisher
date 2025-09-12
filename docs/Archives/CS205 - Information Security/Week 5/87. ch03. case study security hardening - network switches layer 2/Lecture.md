---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-12-02
---

<span style="color: gray;">Dated: 02-12-2024</span>

# Ch03. case Study Security Hardening - Network Switches Layer 2

- Layer 2 Switch STIG
- DISA, Release 20
    - 28 Oct, 2016  
![[Pasted image 20241202205037.png]]
- General Information:
    - Rule Title: The IAO to that all switchports configured using MAC port security will shutdown upon receiving a frame with a different layer 2 source address than what has been configured or learned for port security
	- Vuln ID: V-18565
	- STIG ID: NET-NAC-032
	- Severity: CAT III
- Discussion:
    - The Port Security feature remembers the Ethernet MAC address connected to the switch port and allows only that MAC address to communicate on that port. If any other MAC address tries to communicate through the port, port security will disable the port.
- Check Content:
    - A shutdown action puts the interface into the error-disabled state immediately and sends an SNMP trap notification if it receives a frame with a different layer 2 source address that what has been configured or learned for port security. The following Catalyst IOS interface command will shutdown the interface when such an event occurs:

```
switchport port-security violation shutdown
```

- Fix Text:
    - Configure the port to shutdown when insecure hosts are connected to the wall jack.