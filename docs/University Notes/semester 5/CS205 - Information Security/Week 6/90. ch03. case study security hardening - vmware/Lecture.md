---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-12-03
---

<span style="color: gray;">Dated: 03-12-2024</span>

# Ch03. case Study Security Hardening - Vmware

- CIS Benchmarks case study (Vmware ESXi 5.5)
- 5.1 Disable DCUI to prevent local administrative control (Scored)
- Profile applicability:
    - Level 2
- Description: The Direct Console User Interface (DCUI) can be disabled to prevent any local administration from the Host. Once the DCUI is disabled, any administration of the ESXi host will be done through vCenter.
- Rationale:
    - The DCUI allows for low-level host configuration such as configuring IP address, hostname and root password as well as diagnostic capabilities such as enabling the ESXi shell, viewing log files, restarting agents, and resetting configurations. Actions performed from the DCUI are not tracked by vCenter Server. Even if Lockdown Mode is enabled, users who are members of the DCUI.Access list can perform administrative tasks in the DCUI bypassing RBAC and auditing controls provided through vCenter. DCUI access can be disabled. Disabling it prevents all local activity and thus forces actions to be performed in vCenter Server where they can be centrally audited and monitored.
- Audit: Perform the following:
	- From the vSphere web client select the host.
	- Select "Manage" -> "Settings" -> "System" -> "Security Profile".
	- Scroll down to "Services".
	- Click "Edit…".
	- Select "Direct Console UI".
	- Verify the Startup Policy is set to "Start and Stop Manually"
- Additionally, the following `PowerCLI` command may be used:

```
List DCUI settings for all hosts Get-VMHost | Get-VMHostService | Where { $key -eq "DCUI" }
```

- Remediation: Perform the following:
	- From the vSphere web client select the host.
	- Select "Manage" -> "Settings" -> "System" -> "Security Profile".
	- Scroll down to "Services".
	- Click "Edit…".
	- Select "Direct Console UI".
	- Click "Stop".
	- Change the Startup Policy "Start and Stop Manually".
	- Click "OK".
- Impact:
    - Disabling the DCUI can create a potential "lock out" situation should the host become isolated from vCenter Server.
    - Recovering from a "lock out" scenario requires re-installing ESXi. Consider leaving DCUI enabled and instead enable lockdown mode and limit the users allowed to access the DCUI using the DCUI.Access list.
- Default Value:
    - The prescribed state is not the default state.
- References:
    - http://pubs.vmware.com/vsphere-55/topic/com.vmware.vsphere.security.doc/GUID-6779F098-48FE-4E22-B116-A8353D19FF56.html