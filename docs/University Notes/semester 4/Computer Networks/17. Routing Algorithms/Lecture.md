---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Building Routing Table
There are 2 methods of building `routing tables`.
1. Manually
2. Software

There are then further 2 methods of computing these.

## Static Routing
It is not flexible.  
It is done at boot time  
It has small network overhead.

## Dynamic Routing
It can work around network failures automatically.  
It allows automatic updates by the programmers.

# Computing Shortest Path in a Graph
![[Pasted image 20240603182614.png]]

We use Djikstra's [^1] algorithm to compute the shortest path.  

# Distributed Route Computation
If a node fails then the `switch` updates its routing table information to avoid the failed hardware.

# Distance Vector Routing
The `switches` periodically broadcast #topology information throughout the network.  
Then other `switches` update their routing tables according to the information received.

## Vector - Distance Algorithm
# Link-State Routing
The network #topology is separated from route computations.  
`switches` send `link-state` information about local connections and then they build their routing tables

## Comparison
### Distance Vector Routing
- Simple to implement
- `switch` updates its own routing table first
- It is used in `RIP`.

### Link State Algorithm
- Complex to implement
- `switch` performs independent computations.
- it is used in `OSPF`.

# Example of WAN Technologies
## ARPANET
Began in 1960s, it was funded by Advanced Research Project Agency, which is an organization of US defense department.

## X.25
This was standard for connection-oriented networking.  
It began from IFU which was originally CCITT.

## Frame Relay
It is used for Telco service for delivering blocks of data.  
It is connection based service and requests Telco to establish the circuit between 2 end points.  
Its speeds are following:
- 56 Kbps
- 1.5 Mbps
- 100 Mbps  

## SMDS
`Switched Multi megabit Data Service` is also a Telco service.  
This one is connection less and speed ranges from 1.5 Mbps to 1000 Mbps.

## ATM
`Asynchronous transfer mode` was designed for lower `jitter`, high capacity, audio, video and data.  
It uses fixed size 48 octets data and 5 octets header.

[^ 1]: Read more about [[Djikstra's Algorithm]].
