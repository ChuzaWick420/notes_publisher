---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-12-04
---

<span style="color: gray;">Dated: 04-12-2024</span>

# Ch03. case Study Security Hardening - Mobile Devices - Ios

- CIS Benchmarks case study (Apple iOS 10)
- 3.2.1.12 (L2) Ensure 'Allow modifying cellular data app settings' is set to 'Disabled' (Not Scored)
- Profile applicability:
    - Level 2 - Institutionally Owned Devices
- Description: This recommendation pertains to modifying the use of cellular data by apps.
- Rationale:
    - It is appropriate for an institution to have remote locating and erasure capability with their devices. Forcing cellular data to remain active is a means of supporting this goal.
- Audit:
    - From the Configuration Profile:
        1. Open Apple Configurator
        2. Open the Configuration Profile
        3. In the left windowpane, click on the Restrictions tab.
        4. In the right windowpane, verify that under the tab Functionality, that the checkbox for Allow modifying cellular data app settings is unchecked.
	- Or, from the device:
	    - Tap Settings.
	    - Tap General.
	    - Tap Profile.
	    - Tap `<_Profile Name_>`.
	    - Tap Restrictions.
	    - Confirm Changing app cellular data usage not allowed is displayed.
- Remediation:
    - Open Apple Configurator.
    - Open the Configuration Profile.
    - In the left windowpane, click on the Restrictions tab;
	- In the right windowpane, under the tab Functionality, uncheck the checkbox for Allow modifying cellular data app settings.
	- Deploy the Configuration Profile.
- CIS Controls:
    - 5.1 Minimize And Sparingly Use Administrative Privileges Minimize administrative privileges and only use administrative accounts when they are required.
	- Implement focused auditing on the use of administrative privileged functions and monitor for anomalous behavior