---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-15
---

<span style="color: gray;">Dated: 15-11-2024</span>

# Ch03. case Study - Security Hardening - Apache Server

- CIS Benchmarks case study (Apache Tomcat 7)
- 7.7 (page 65): Configure log file size limit (Scored)
- Profile applicability:
    - Level 2
	- Description: By default, the logging.properties file will have no defined limit for the log file size. This is a potential denial of service attack as it would be possible to fill a drive or partition containing the log files
	- Rationale: Establishing a maximum log size that is smaller than the partition size will help mitigate the risk of an attacker maliciously exhausting disk space
	- Audit: Validate the max file limit is not greater than the size of the partition where the log files are stored.
	- Remediation: Create the following entry in your logging.properties file. This field is specified in bytes:

```
java.util.logging.FileHandler.limit=10000
```
