---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# 10 Base - T
It is also called `twisted wire pair` or `TP Ethernet`.  
![[Pasted image 20240603122935.png]]

## Hubs
These are extension of connections with multiplexing concept.  
They are sometimes called `Ethernet-in-a-box`

# Protocol Software and Ethernet Wiring
All wiring technologies use identical Ethernet specifications.  
Which means they use same frame formats.  
They use same `CSMA/CD` algorithms.  
![[Pasted image 20240603123413.png]]

# Comparison of Wiring Scheme
The `transceivers` allow computers to be powered off or disconnected from the network without disrupting it.

## Topologies and Network Technologies
The `twisted wire pair` is physically a `star` #topology but logically, it is a `bus` #topology.  
 The `token ring` is physically a `star` #topology but logically, it is a `ring` #topology.
 
## Filtering Incoming Frames
The analyzers use filters to capture certain frames which match the filtering criteria and ignores the rest.

# Advantages and Disadvantages of Wiring Schemes
![[Pasted image 20240603124555.png]]  
The figure contains 3 schemes as follows:
1. Thin
2. Thick
3. Twisted pair

## Reliable
The connections which use `transceivers` allow the computers to be disconnected without disturbing the whole network.

## Cost
The `twisted wire pair` is cheapest.  
The `Thicknet` is the most expensive and is no longer used.

# The Topology Paradox
## Logical Topology
It is defined by specific network technology.

## Physical Topology
It is defined by wiring scheme.

# Network Interface Card and Wiring Schemes

The cable used for wiring should match the following:
1. The intended data rate
2. The distance between devices
3. The amount of em-noise
4. Anticipated future needs
5. Cost

![[Pasted image 20240603125813.png]]

# Wiring Schemes and other Network Technologies
- The `local talk` technology uses hubs (physically star) to implement a logically `bus` #topology.
- The `IBM's Token Ring` technology uses hubs (physically star) to implement a logically `ring` #topology.
