---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-12
---

<span style="color: gray;">Dated: 12-11-2024</span>

# Ch02. how is Site Redundancy Incorporated into Enterprise Network Design

## Types

### Hot Site

- Mirror of primary data center
- Populated with servers, cooling, power, and office space
- Running concurrently with main/primary data center (synching)
- Minimal impact

### Cold Site

- Office or data center space without any server related equipment installed
- Power, cooling and office space
- Servers/equipment migrated in event of primary site failure

### Warm Site

- Middle ground between hot site and cold site
- Some pre-installed server hardware (ready for installation of production environments)
- Requires engineering support to activate

### Rto

- Max amount of time, following a disaster, for an organization to recover files from backup storage and resume normal operations (max amount of downtime an organization can handle)

### Rpo

- Max age of files that an organization must recover from backup storage for normal operations to resume after a disaster (minimum frequency of backups)

### Example

- If an organization has an RTO of two hours, it cannot be down for longer than that.
- if an organization has an RPO of four hours, the system must back up at least every four hours.

> [!QUESTION]- Post Assessments
> 
> > [!QUESTION]- Which of the following is the cheapest type of redundant site models
> > - [ ] Warm Site  
> > - [x] Cold Site  
> > - [ ] Hot Site  
> > - [ ] Moderate Site
> 
> > [!QUESTION]- Which one of the following is NOT a type of redundant site models?  
> > - [ ] Warm Site  
> > - [ ] Hot Site  
> > - [x] Thunder Site  
> > - [ ] cold Site
> 
> > [!QUESTION]- In the context of Site Redundancy, if an organization has an _ of two hours then it cannot be down for longer than that.  
> > - [ ] RPO  
> > - [x] RTO  
> > - [ ] RSA  
> > - [ ] RTT
> 
> > [!QUESTION]- which of the following redundant site model is considered as an expensive model.  
> > - [ ] Moderate Site  
> > - [x] Hot Site  
> > - [ ] Warm Site  
> > - [ ] Cold Site  
> 
> > [!QUESTION]- In the context of Site Redundancy, if an organization has an RPO of four hours then the system must back up at least every _ hours.  
> > - [ ] Eight  
> > - [ ] two  
> > - [ ] Three  
> > - [x] four
