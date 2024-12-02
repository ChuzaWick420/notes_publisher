---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-12-02
---

<span style="color: gray;">Dated: 02-12-2024</span>

# Ch03. case Study Security Hardening - Ms Internet Explorer Browser

- CIS Benchmarks case study (MS Internet Explorer 11)
- 1.5 Configure 'Do not allow users to enable or disable add-ons' (Not Scored)
- Profile applicability:
    - Level 1
- Description: This policy setting allows you to manage whether users have the ability to allow or deny add-ons through Add-On Manager. If you enable this policy setting, users cannot enable or disable add-ons through Add-On Manager. The only exception occurs if an add-on has been specifically entered into the 'Add-On List' policy setting in such a way as to allow users to continue to manage the add-on. In this case, the user can still manage the add-on through the Add-On Manager. If you disable or do not configure this policy setting, the appropriate controls in the Add-On. Manager will be available to the user. Configure this setting in a manner that is consistent with security and operational requirements of your organization.
- Rationale: Users often choose to install add-ons that are not permitted by an organization's security policy. Such add-ons can pose a significant security and privacy risk to your network.
- Audit: Navigate to the UI Path articulated in the Remediation section and confirm it is set as prescribed. This group policy setting is backed by the following registry location:

```
HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Internet Explorer\Restrictions\NoExtensionManagement
```

- Remediation: To establish the recommended configuration via Group Policy, set the following UI path to Not Configured.  

```
Computer Configuration\Administrative Templates\Windows Components\Internet Explorer\Do not allow users to enable or disable add-ons
```

- Impact: When the Do not allow users to enable or disable add-ons setting is enabled, users will not be able to enable or disable their own Internet Explorer add-ons. If your organization uses add-ons, this configuration may affect their ability to work.
- 1.5 Configure 'Do not allow users to enable or disable add-ons' (Not Scored)
    - Default Value: Disabled