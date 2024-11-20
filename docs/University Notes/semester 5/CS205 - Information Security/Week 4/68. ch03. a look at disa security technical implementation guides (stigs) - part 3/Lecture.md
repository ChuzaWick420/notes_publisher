---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-14
---

<span style="color: gray;">Dated: 14-11-2024</span>

# Ch03. a Look at Disa Security Technical Implementation Guides (stigs) - part 3

- Windows Server 2012 R2 Member Server
- Import STIG
- V1099 (Lockout duration)

![[Pasted image 20241115125816.png]]

- Rule Title:
    - The lockout duration must be configured to require an administrator to unlock an account
- Severity: CAT II
- Discussion:
    - The account lockout feature, when enabled, prevents brute-force password attacks on the system. This parameter specifies the period of time that an account will remain locked after the specified number
	- of failed logon attempts. A value of 0 will require an administrator to unlock the account.
- Check Content:
    - Verify the effective setting in Local Group Policy Editor.
    - Run "gpedit.msc"
    - Navigate to Local Computer Policy → Computer configuration → Windows settings → Security settings → Account Policies → Account lockout Policy.
	- If the "Account lockout duration" is not set to "0", requiring an administrator to unlock the account, this is a finding.
- Fix Text:
    - Configure the policy value for Computer Configuration -> Windows Settings -> Security Settings -> Account Policies -> Account Lockout Policy -> "Account lockout duration" to "0" minutes,
    - "Account is locked out until administrator unlocks it".
- CCI: NIST SP 800-53 Revision 4 :: AC-7 b

> [!QUESTION]- Post Assessment
> 
> > [!QUESTION]- The account lockout feature, when enabled, prevents _ password attacks.  
> > - [ ] Bright force  
> > - [x] Brute force  
> > - [ ] Blind force  
> > - [ ] Bridged force  
> 
> > [!QUESTION]- In DISA, configuring the lockout duration to require the administrator to unlock an account falls in severity of _  
> > - [ ] CAT 5  
> > - [ ] CAT 1  
> > - [x] CAT 2  
> > - [ ] CAT 3  
> 
> > [!QUESTION]- In the context of DISA STIGs, to set the policy that the account once locked remains locked until the administrator unlocks it by him/herself, you need to set the value as _ minutes.  
> > - [ ] 90  
> > - [ ] 33  
> > - [ ] 9  
> > - [x] 0  
