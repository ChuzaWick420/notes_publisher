---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Startup and Steady State
## Startup
When the `bridge` boots up, its address list is empty.  
This state is called `startup` state.

## Steady State
When the `bridge` has received at least one `frame` from every computer, its address list is built.  
This state is called `steady state`.

# Planning a Bridge
Since `bridges` are used to divide #LAN into segments, the computers who communicate frequently can be placed into same segment.  
This improves the performance of the network because traffic on one segment does not affects the traffic on other segment.

# Bridging between Building
![[Pasted image 20240603143646.png]]

## Advantages
1. The `fiber optic` connecting both buildings doesn't need to be disturbed while connecting or disconnecting computers to the network.
2. Traffic at one building doesn't affects the other building.

# Building across Longer Distance
![[Pasted image 20240603144047.png]]

Since the `bandwidth` is very low, the `bridge` has to store data into its memory and wait till it can be send to the satellite for communication but it may run out of memory.  
Therefore, the communication software waits for a response after sending few frames.

# A Cycle Bridges
![[Pasted image 20240603144518.png]]

Sometimes, a network can become cyclic as such:  
![[Pasted image 20240603144625.png]]

Problem here is that if a `broadcast` signal is sent, it never terminates and keeps looping around, causing infinite copies.

# Distributed Spanning Tree
In this cyclic case, the `bridges` communicate with each other and automatically decide through `DST` algorithm that which `bridge` will not forward the broadcast frames and which one will do.
