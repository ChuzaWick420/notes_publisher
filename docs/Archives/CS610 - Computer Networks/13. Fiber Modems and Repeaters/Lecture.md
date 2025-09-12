---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Distance Limitation and LAN Design
The electrical signals get weaker as they travel through the cable and the delays must be short to enable the `CSMA/CS` and `token passing` etc.  
But usually, there is a need of extension beyond the normal length limit.

## LAN Extension
Most techniques use hardware is used to extend the diameter of the #LAN medium.

# Fiber Optic Extension
![[Pasted image 20240603131401.png]]  
The `fiber modems` are responsible for conversions between light and digital signals.  
The `fiber optic` spans over kilometers with minimal delay and maximum bandwidth.

# Repeaters
![[Pasted image 20240603131706.png]]  
As the signals travel, they get weakened.  
Therefore, #repeaters re-transmit the signal.

As the figure suggests, 1 #repeaters _doubles_ the max length meanwhile 2 #repeaters _triples_ the max length.

Although infinite length can be achieved but it introduces delay which disturbs the `CSMA/CD`.  
Therefore, the `Ethernet` standard specifies that no more than `4` #repeaters should be used to connect 2 stations.

## Disadvantage
#repeaters only amplify and re-transmit.  
This also includes collision errors etc.

# Bridges
These consist of following components:
1. 2 NICs
2. CPU
3. Memory
4. ROM

It runs the code stored in its `ROM`.  
It connects 2 #LAN segments, listens to all the traffic and transmits only valid frames unlike #repeaters.

# Frame Filtering
![[Pasted image 20240603132910.png]]

Most bridges are self learning.  
They automatically add addresses of computers to their address list.
