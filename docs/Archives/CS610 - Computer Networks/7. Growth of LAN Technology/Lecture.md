---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Shared Communication Channels
The development started in early 1960 and 1970s.  
For the short distances, the LAN is used because it uses a shared medium which reduces the number of connections, has becoming a cheaper solution.  
But due to this shared medium, the computers compete against each other to use the channel because they have to wait for their turns.  
For long distances, the #point-to-point approach is used.

# Locality of Reference Principle
This principle helps to predict the communication patterns.  
There are 2 patterns:

## Spatial
In this pattern, computers which are located nearby are likely to communicate with each other.

## Temporal
In this pattern, the computers are likely to communicate repeatedly to the same computers.

#LAN is effective due to `spatial locality of reference`.
# LAN Topologies
There are 3 popular #LAN topologies:

## Star
In this #topology, the devices are attached to the central device called the `hub`.  
![[Pasted image 20240601195755.png]]

## Ring
In this #topology, the computers are connected to each other in a closed loop.  
One computer sends message to 2nd one, the 2nd one sends to 3rd one and so on.  
![[Pasted image 20240601200005.png]]

## Bus
In this #topology, all the computers are connected to same back-bone cable.  
The computers have to coordinate to wait for their turns.  
![[Pasted image 20240601200137.png]]

# Ethernet
It was invented in 1970s.  
Intel and others defined it in a standard called `DIX` standard.  
It is now managed by `IEEE` under standard `802.3` which defines the length and voltages etc.  
It uses bus #topology and is also called as a `segment` which is limited to 500 meters in length.  
The minimum separation between connections is 3 meters.

## Ethernet Speeds
- Originally, it was 3 Mbps.
- Standard now a days is 10 Mbps
- The fast ethernet operates at 100 Mbps ones
- But there are also which touches Giga bits per second.

## Encoding Used in Ethernet
The encoding technique used in it is called `manchester`.  
![[Pasted image 20240601201323.png]]

- `0` is represented by voltage drop.
- `1` is represented by voltage increase.
