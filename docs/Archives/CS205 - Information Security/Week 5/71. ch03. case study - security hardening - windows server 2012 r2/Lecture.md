---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-15
---

<span style="color: gray;">Dated: 15-11-2024</span>

# Ch03. case Study - Security Hardening - Windows Server 2012 R2

- Windows Server 2012 R2
- DISA, Release 8
    - 28 April 2017
- Domain Controller  
![[Pasted image 20241115142351.png]]
- General Information:
    - Rule Title: Autoplay must be disabled for all drives
    - STIG ID: WN12-CC-000074
    - Severity: CAT I
- Discussion:
    - Allowing Autoplay to execute may introduce malicious code to a system. Autoplay begins reading from a drive as soon media is inserted into the drive. As a result, the setup file of programs or 
	- music on audio media may start. By default, Autoplay is disabled on removable drives, such as the floppy disk drive (but not the CD-ROM drive) and on network drives.
	- Enabling this policy disables Autoplay on all drives.
- Check Content:
    - If the following registry value does not exist or is not configured as specified, this is a finding:
    - Registry Hive: HKEY_LOCAL_MACHINE
	- Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\policies\Explorer
	- Value Name: NoDriveTypeAutoRun
	- Type: REG_DWORD
	- Value: 0x000000ff (255)
- Fix Text:
    - Configure the policy value for Computer Configuration -> Administrative Templates -> Windows Components -> AutoPlay Policies -> "Turn off AutoPlay" to "Enabled:All Drives".
- CCI (Control Correlation Identifier):
    - CCI: CCI-001764
    - The information system prevents program execution in accordance with organization-defined policies regarding software program usage and restrictions and/or rules authorizing the terms and conditions of software program usage.
	- NIST SP 800-53
	- Revision 4 :: CM-7 (2)
