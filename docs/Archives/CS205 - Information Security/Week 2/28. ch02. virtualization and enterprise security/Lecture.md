---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-11
---

<span style="color: gray;">Dated: 11-11-2024</span>

# Ch02. Virtualization and Enterprise Security

- Cloud Security Alliance: "Best Practices For Mitigating Risks In Virtual Environments" (PDF)
- Virtualization security classified into three areas:
    - Architectural
    - Hypervisor software
    - Configuration

## Risks

- VM Sprawl
- Sensitive data within VM
- Security of offline and dormant VMs
- Security of Pre-configured (Golden Image) VMs
- Lack of visibility into virtual networks

## Vm Sprawl

- Impact: VMs can be created quickly, self-provisioned, or moved between physical servers, avoiding conventional change management process
- Proliferation of VMs causing performance and security risks
- Controls: Policies, procedures and governance of VM lifecycle management
- Control creation, storage and use of VM images with a formal change management process
- Discover VMs & apply security controls
- Controls: Keep a small number of identified, good and patched images of a guest operating system separately for fast recovery & restoration of systems

## Sensitive Data within Vm

- Impact: VM images and snapshots can be copied easily via USB or console of hypervisor installed elsewhere
- Controls: Encrypt data stored on virtual and cloud servers
- Policies to restrict storage of VM images and snapshots
- Image change management process with approvals
- Logging & monitoring

> [!QUESTION]- Post Assessment
> 
> > [!QUESTION]- In terms of virtualization environment: VIVI stands for  
> > - [ ] Video Machine  
> > - [ ] Voice Machine  
> > - [x] Virtual Machine  
> > - [ ] Virtual Map
> 
> > [!QUESTION]- Virtualization security classified into following areas.  
> > - [ ] four  
> > - [x] three  
> > - [ ] five  
> > - [ ] one
