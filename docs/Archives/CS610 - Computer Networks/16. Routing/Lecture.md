---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Source Independence
The `next hop` destination does not depend upon the source of the packet.  
This phenomena is called `source independence`  
The packet only have destination information for the `next hop`, this means even if the network topology changes without notifying the network, it would still work.  
Hence, increasing the dynamic robustness.

# Hierarchical Addressing and Routing
The process of forwarding packets, is called #routing.  
The information about destinations is kept in routing tables.  
![[Pasted image 20240603171538.png]]  
Figure `b` represents the routing table of `switch 2`.

# Routing in a WAN
There are 2 types of `switch` according to attached computers.

## Interior Switch
This `switch` has no computers attached to it.

## Exterior Switch
This `switch` has computers attached to it.

Both of these `switches` need routing tables which need 2 things.

## Universal Routing
The table should have `next hop` for each possible destination.

## Optimal Routes
The table should have `next hop` for shortest path possible.

## Modeling a WAN
We can model a WAN by representing `switches` as `nodes` and `direct connections` as `edges`.  
![[Pasted image 20240603175610.png]]

## Route Computation with a Graph
![[Pasted image 20240603180415.png]]

# Redundant and Routing Information
Notice how the above figure shows same `next hop` for `node 1`. We can collapse the table as such:  
![[Pasted image 20240603181818.png]]
