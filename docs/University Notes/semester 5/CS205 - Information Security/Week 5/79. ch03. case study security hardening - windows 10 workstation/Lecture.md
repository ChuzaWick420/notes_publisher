---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-12-02
---

<span style="color: gray;">Dated: 02-12-2024</span>

# Ch03. case Study Security Hardening - Windows 10 Workstation

- Windows 10
- DISA, Release 9
    - 28 April 2017

![[Pasted image 20241202083526.png]]

- General Information:
    - Rule Title: The antivirus program must be configured to update signature files on a daily basis.
    - STIG ID: WN10-00-000046
    - Severity: CAT I
- Discussion:
    - Virus scan programs are a primary line of defense against the introduction of viruses and malicious code that can destroy data and even render a computer inoperable. Using a virus scan program provides the ability to detect malicious code before extensive damage occurs. Updated virus scan data files help  protect a system, as constantly changing malware is identified by the antivirus software vendors
- Check Content:
    - This requirement is NA if McAfee VirusScan Enterprise (VSE) is used. It will be addressed with the corresponding McAfee VSE STIG.
    - Configurations will vary depending on the product.
- Fix Text:
    - Configure the antivirus program to update signature files at least daily. Ensure the updates are occurring on a timely basis and are not more than a week old.
- CCI (Control Correlation Identifier):
    - CCI: 000366
    - The org implements the security config settings.
    - NIST SP 800-53 :: CM-6 b
    - NIST SP 800-53A :: CM-6.1 (iv)
    - NIST SP 800-53 Revision 4 :: CM-6