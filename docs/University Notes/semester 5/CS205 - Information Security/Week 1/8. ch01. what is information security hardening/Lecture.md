---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-10-31
---

<span style="color: gray;">Dated: 2024-10-31</span>

# Ch01. what is the Information Security Hardening

## It Assets

(network, systems, application, databases, mobile, physical security) come with default settings which are not suitable for security.

## Security Hardening

`Security hardening` is the process of configuring IT assets to maximize security of the IT asset and minimize security risks.

## Security in the "Trenches"

- Security at the most fundamental operational layer
- Security where it matters most
- Usually (but not always) involves junior staff who need extra guidance, training, and scrutiny.

## Steps to Information Hardening

1. Identify critical assets (& asset owner)
2. Research on applicable security controls
3. Checklist of applicable controls
4. Document controls into SOP
5. Implement controls on test setup
6. Validation of control implementation
7. Change management process for PROD
8. Implement on PROD & monitor

## Why is Security Hardening, the First step in the Security Transformation Model

- Most basic security settings
- If not adequately addressed here, rest of the security measures hardly matter

## Example of Cisco Router Security Hardening

- Remote access through SSH and not through telnet
- Turn off all unused services
- Session timeout and password retry lockout

http://www.cisco.com/c/en/us/support/docs/ip/access-lists/13608-21.html

> [!question]-
> 
> > [!question]- In terms of security hardening, SSH stands for  
> > - [ ]Small Shell  
> > - [ ]Select Shell  
> > - [x]Secure Shell  
> > - [ ]Smart Shell  
> 
> > [!question]- Which of the following is the process of configuring IT assets to maximize security of the IT asset and minimize security risks  
> > - [ ] Security test  
> > - [ ] Security breach  
> > - [ ] Security guide  
> > - [x] Security hardening
