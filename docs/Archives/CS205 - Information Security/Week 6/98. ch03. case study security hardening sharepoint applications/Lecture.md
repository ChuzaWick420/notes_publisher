---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-12-04
---

<span style="color: gray;">Dated: 04-12-2024</span>

# Ch03. case Study Security Hardening Sharepoint Applications

- SharePoint 2013 STIG
- DISA, Release 3
    - 22 April, 2016
- SharePoint server side configurations
- General Information:
    - Rule Title: For environments requiring an Internet-facing capability, the SharePoint application server upon which Central Administration is installed, must not be installed in the DMZ.
	- Vuln ID: V-599995
	- STIG ID: SP13-00-000155
	- Severity: CAT II
- Discussion:
    - Information flow control regulates where information is allowed to travel within an information system and between information systems (as opposed to who is allowed to access the information) and without explicit regard to subsequent accesses to the information.
	- SharePoint installed Central Administrator is a powerful management tool used to administer the farm. This server should be installed on a trusted network segment. This server should also be used to run services rather than user-oriented web applications.
- Check Content:
    - For environments requiring an Internet-facing capability, ensure the SharePoint Central Administration application server is not in the DMZ.
    - Inspect the logical location of the server farm web front end servers.
	- Verify the Central Administration site is not installed on a server located in a DMZ or other publicly accessible segment of the network.
	- If Central Administrator is installed on a publicly facing SharePoint server, this is a finding.
- Fix Text:
    - For environments requiring an Internet-facing capability, remove the SharePoint Central Administration application server upon which Central Administration is installed from the DMZ.
