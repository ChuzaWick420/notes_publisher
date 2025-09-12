---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-12-04
---

<span style="color: gray;">Dated: 04-12-2024</span>

# Ch03. case Study Security Hardening - Mobile Devices - Android

- CIS Benchmarks case study (Google Android 7)
- 1.15 Ensure Android Device Manager is set to Enabled (Not Scored)
- Profile applicability:
    - Level 2
- Description: Setup Android Device Manager as a Device Administrator.
- Rationale:
    - If you lose your Android device, you could use Android Device Manager to find your device and also ring, lock, or erase your device data remotely.
- Audit: Follow the below steps to verify that Android Device Manager is enabled:
    - Tap the System Settings Gear Icon.
    - Scroll to Personal.
    - Tap Security.
    - Scroll to Device administration;
	- Tap Device administrators.
	- Verify that Android Device Manager is enabled.
- Remediation: Follow the below steps to enable Android Device Manager:
    - Tap the System Settings Gear Icon.
    - Scroll to Personal.
    - Tap Security.
    - Scroll to Device administration;
	- Tap Device administrators.
	- Tap Android Device Manager.
	- Tap Activate this device administrator.
- Impact:
    - Google may track your device location anytime.
- Default Value:
    - By default, Android Device Manager is not enabled.
- References:
    - https://support.google.com/pixelphone/answer/3265955