---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-12
---

<span style="color: gray;">Dated: 12-11-2024</span>

# Ch02 how is Dr Accommodated into the Enterprise Architecture - part 1

## Dr Considerations

- DR Plan
- RTO and RPO

### Dr Plan

- A disaster recovery policy statement, plan overview and main goals of the plan
- Key personnel and DR team contact information
- Description of emergency response actions immediately following an incident.
- A diagram of the entire network and recovery site.
- Directions for how to reach the recovery site.
- A list of software and systems that will be used in the recovery.
- Sample templates for a variety of technology recoveries, including technical documentation from vendors.
- Summary of insurance coverage.
- Proposed actions for dealing with financial and legal issues.
- Ready-to-use forms to help complete the plan.

![[Pasted image 20241112200218.png]]

### Rto

- Max amount of time, following a disaster, for an org to recover files from backup storage and resume normal operations; max amount of downtime an org can handle.
- If an organization has an RTO of two hours, it cannot be down for longer than that

### Rpo

- RPO is the max age of files that an organization must recover from backup storage for normal operations to resume after a disaster; determines the minimum frequency of backups  
- For example, if an organization has an RPO of four hours, the system must back up at least every four hours

> [!QUESTION]- Post Assessment
> 
> > [!QUESTION]- If an organization has an RPO of six hours then the system must back up at least every _ hours.  
> > - [ ] Twelve  
> > - [x] Four  
> > - [ ] Three  
> > - [ ] Six
> 
> > [!QUESTION]- Which of the following is the maximum down time an organization can handle.  
> > - [ ]MTIJ  
> > - [ ]RTT  
> > - [ ]RSA  
> > - [x]RTO
> 
> > [!QUESTION]- Which of the following is the max age of files that an organization must recover from backup storage for normal operations to resume after a disaster.  
> > - [ ] MTIJ  
> > - [ ] RTT  
> > - [x] RPO  
> > - [ ] RTO
