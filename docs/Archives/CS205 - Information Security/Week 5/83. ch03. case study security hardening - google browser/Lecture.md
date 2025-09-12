---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-12-02
---

<span style="color: gray;">Dated: 02-12-2024</span>

# Ch03. case Study Security Hardening - Google Browser

- Google Chrome
- DISA, Release 8
    - - 27 April, 2017  
![[Pasted image 20241202192337.png]]
- General Information:
    - Rule Title: Session only based cookies must be disabled.
	- Vuln ID: V-44799
	- STIG ID: DTBC-0045
	- Severity: CAT I
- Discussion:
    - Policy allows you to set a list of URL patterns that specify sites which are allowed to set session only cookies. If this policy is left not set the global default value will be used for all sites either from the `DefaultCookiesSetting` policy if it is set, or the user's personal configuration otherwise. If the `RestoreOnStartup` policy is set to restore URLs from previous sessions this policy will not be respected and cookies will be stored permanently for those sites
- Check Content:
    - Universal method:
        1. In the omnibox (address bar) type chrome://policy
        2. If the policy `CookiesSessionOnlyForUrls` exists, and has any defined values, this is a finding
    - Windows method:
        1. Start regedit
        2. Navigate to `HKLM\Software\Policies\Google\Google Chrome\Content Settings\CookiesSessionOnlyForUrls`
        3. If this key exists and has any defined values, this is a finding
- Fix Text:
    - Windows group policy:
        1. Open the group policy editor tool with gpedit.msc
        2. Navigate to Policy Path: `Computer Configuration\Administrative Templates\Google\Google Chrome\Content Settings`
		    - Policy Name: Allow session only cookies on these sites
		    - Policy State: Disabled
		    - Policy Value: N/A
- CCI (Control Correlation Identifier):
    - CCI-000166
    - The information system protects against an individual (or process acting on behalf of an individual) falsely denying having performed organization-defined actions to be covered by non-repudiation.
		- NIST SP 800-53 :: AU-10
		- NIST SP 800-53A :: AU-10.1
		- NIST SP 800-53 Revision 4 :: AU-10