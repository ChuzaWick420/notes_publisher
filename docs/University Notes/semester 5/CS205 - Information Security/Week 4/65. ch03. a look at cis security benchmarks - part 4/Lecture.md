---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-14
---

<span style="color: gray;">Dated: 14-11-2024</span>

# Ch03. a Look at Cis Security Benchmarks - part 4

- CIS Benchmarks example (Operating Systems)
    - MS Windows Server 2012-R2
- Profile applicability:
    - Level 1 domain controller
    - Level 1 member server
    - Level 2 domain controller
    - Level 2 member server
- Level 1: Items in this profile intend to:
    - be practical and prudent;
    - provide a clear security benefit; and
    - not inhibit the utility of the technology beyond acceptable means
- Level 2: extends the Level 1 - profile
    - intended for environments or use cases where security is paramount
    - acts as defense in depth measure
    - may negatively inhibit the utility or performance of the technology
- Control content:
    - Profile applicability (ASA 8.X, ASA 9.X)
    - Description
    - Rationale
    - Audit
    - Remediation
    - Impact
    - Default value
    - References
- 1.1.2 [L1]: Ensure 'Maximum password age' is set to '60 or fewer days, but not 0' (Scored)
    - Profile applicability: Level 1 Domain Controller, Level 1 Member Server
- 1.1.2 [L1] Description:
    - This policy setting defines how long a user can use their password before it expires.
    - Values for this policy setting range from 0 to 999 days. If you set the value to 0, the password will never expire.
- 1.1.2 [L1] Audit:
    - Navigate to the UI Path articulated in the Remediation section and confirm it is set as prescribed.

![[Pasted image 20241114145638.png]]

- 1.1.2 [L1] Default Value: 42 days
- 1.1.2 [L1] Reference: CCE-37167-4
    - Common Configuration Enumeration (Unique identifiers for common system config issues)

> [!QUESTION]- Post Assessment
> 
> > [!QUESTION]- In the context of CIS Microsoft Server 2012 R2 benchmark, to implement the policy that how long a user can use his/her password before it expires, if you set the value to _ then the password will never expire.  
> > - [ ] 999  
> > - [ ] 100  
> > - [ ] 555  
> > - [x] 0  
> 
> > [!QUESTION]- In the context of CIS Microsoft Server 2012 R2 benchmark, to implement the policy that how long a user can use his/her password before it expires, the valid range is _ days.  
> > - [ ] 1 to 1000  
> > - [ ] 0 to 999  
> > - [x] 1 to 100  
> > - [ ] 0 to 990  
