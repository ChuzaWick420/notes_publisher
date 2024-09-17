---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Resource Sharing
`Resource sharing` means to share resources between different users.  
**Example:** In an office, it would be expensive to give printer to each user.  
Instead, it would be better to have one printer, shared across different users.

## Goal of Resource Sharing
Main goal is to make the resource available to any user regardless of the place of the resource or the user.

# Tools for Probing the Internet
Now a days, there are millions of computers connected to the internet.  
To check if a computer is online or not, we use tools for _probing_.

## Ping
This tool sends packets to our target and receives them as well.  
It also tells us the #ip-address of the target computer.

### Problems with Ping
`ping` sometimes fail and we cannot tell for sure what exactly was the root cause of it since there are multiple possibilities for it to fail.  
These possibilities are as follows:
1. Remote computer might have a problem.
2. Local computer might have a problem.
3. Ping sometimes fails because of congestion.
4. Some networks reject these packets to save themselves from `denial of service` attacks.

## Trace Route
This is another tool which provides more details.  
This tool shows all the computers from _source_ to _destination_.
