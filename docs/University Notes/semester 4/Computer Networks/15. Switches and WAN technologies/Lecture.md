---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Switching
![[Pasted image 20240603145332.png]]  
A `hub` simulates a shared medium meanwhile a `switch` simulates a bridged #LAN while each segment contains 1 computer only.

When a `hub` is used, only 1 pair of computers can talk at a time.  
When a `switch` is used, any number of pairs of computers can talk at the same time.

# Combining Switches and Hubs
To reduce the cost, a number of computers can be connected to distributed `hubs` which later can be connected to a `switch`.

# Bridging and Switching with other Technologies
These devices are also available for other technologies like:
- `FDDI`
- `Token Ring`

# WAN Technologies and Routing
The #LAN cannot be arbitrarily expanded.  
We need other technologies to overcome the distances.

# Characterization of Networks
There are 3 characteristics of a network:

## Local Area Network
It is used in single building.

## Metropolitan Area Network
it is used in single city

## Wide Area Network
It is used over country or even continental levels.

# Packet Switches
A `packet switch` consists of:
1. Network Interfaces
2. Memory
3. Program dedicated for function switching

![[Pasted image 20240603151823.png]]

`Packet Switches` can connect to other `Packet Switches` or computers.  
The speed between the `switches` is faster as compared to connections between a `packet switch` and a computer.

# Packet Switches as a Building Blocks
Many `packet switches` can be connected together to form a #WAN.  
![[Pasted image 20240603153333.png]]

# Store and Forward
The `packet switch` contains memory which holds data on queue in case there is traffic.  
After the traffic is low, it then forwards data to other `packet switches` or computers.

# Physical Addressing in a WAN
1. The data is transmitted in packets equivalent to frames.
2. Each packet has a format with header.
3. The packet header includes destination and source addresses.
4. Many WANs use hierarchical addressing for efficiency. One part of address identifies destination switch. Other part of address identifies port on switch.  
![[Pasted image 20240603154508.png]]

# Next Hop Forwarding
1. If the destination is local computer, packet switch delivers computer port.
2. If the destination is attached to another switch, this packet switch forwards to next hop through connection to another switch.
3. The choice of another switch is based on destination address in packet.
