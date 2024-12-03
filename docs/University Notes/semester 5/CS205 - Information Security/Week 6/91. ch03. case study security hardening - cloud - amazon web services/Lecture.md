---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-12-03
---

<span style="color: gray;">Dated: 03-12-2024</span>

# Ch03. case Study Security Hardening - Cloud - Amazon Web Services

- CIS Benchmarks case study (Cloud - Amazon Web Services Foundations)
- 1.14 Ensure hardware MFA is enabled for the "root" account (Scored)
- Profile applicability:
    - Level 2
- Description: The root account is the most privileged user in an AWS account. MFA adds an extra layer of protection on top of a user name and password. With MFA enabled, when a user signs in to an AWS website, they will be prompted for their user name and password as well as for an authentication code from their AWS MFA device. For Level 2, it is recommended that the root account be protected with a hardware MFA.
- Rationale:
    - A hardware MFA has a smaller attack surface than a virtual MFA. For example, a hardware MFA does not suffer the attack surface introduced by the mobile smartphone on which a virtual MFA resides;
	- Note: Using hardware MFA for many, many AWS accounts may create a logistical device management issue. If this is the case, consider implementing this Level 2 recommendation selectively to the highest security AWS accounts and the Level 1 recommendation applied to the remaining accounts.
- Audit: Perform the following to determine if the root account has a hardware MFA setup:
    - Run the following command to list all virtual MFA devices:

```
aws iam list-virtual-mfa-devices
```

	- If the output contains one MFA with the following Serial Number, it means the MFA is virtual, not hardware and the account is not compliant with this recommendation:

```json
"SerialNumber": "arn:aws:iam::<aws_account_number>:mfa/root-account-mfa-device"
```

- Remediation: `[8 step process… check the benchmark]`
- References:
    - http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html
    - http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_physical.html#enable-hw-mfa-for-root

> [!QUESTION]- Post Assessments
> 
> > [!QUESTION] A hardware MFA has a smaller attack surface than a _ MFA.  
> > - [x] Virtual  
> > - [ ] Previous  
> > - [ ] Actual  
> > - [ ] Next
> 
> > [!QUESTION] In the context of security hardening: NIFA stands for _  
> > - [x] Multi-Factor Authentication  
> > - [ ] Multi-Factor Attention  
> > - [ ] Multi-Factor Attribution  
> > - [ ] Multi-Factor Antivirus
