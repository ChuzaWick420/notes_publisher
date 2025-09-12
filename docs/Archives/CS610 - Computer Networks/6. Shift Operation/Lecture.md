---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Shift Operation
This operation shifts all the bits to the left by one position.  
**Example:**  
![[Pasted image 20240601182341.png]]  
This figure represents a `16-bit` CRC hardware which uses 3 `shift registers` and 3 `XOR` units.

# Types of Errors
CRC can check following errors better than checksum.

## Vertical Errors
These occur due to hardware failure.  
**Example:** 2nd bit of each character is damaged.

## Burst Errors
These occur when a small set of bits changes due to some external interference like lightning or an electric motor starting nearby.

# Frame Format and Error Detection
![[Pasted image 20240601183052.png]]  
If there is an error in the frame, it is rejected by the receiver.

# LAN Technology and Network Topology
## Introduction
In a shared medium, hardware devices need to take turns in able to communicate.

## Direct Point-to-Point Communication
In this mode, each `channel` connects exactly 2 devices.  
![[Pasted image 20240601183507.png]]

## Advantages
1. The connection type of individual connections can be different. 
2. Individual connections can choose a different frame format and error detection mechanism etc. 
3. It is easy to enforce security and privacy

## Disadvantages
1. The no. of connections grow more rapidly than the no. of computers.  
2. For ‘n’ computers connections = (n^2 – n)/2.  
3. Most computers use the same physical path.  
4. Direct point-to-point communication is expensive due to a no. of connections.  
5. Another disadvantage is that adding a new computer to the network requires N-1 new connections as shown in the above figure.
