---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Interface Hardware
The #LAN transmission speed is faster than the CPU speeds.

# Network Interface Hardware
Since CPU cannot keep up with the network speeds, we need #network-interface-card or `network-adaptor-card` (NIC).  
It connects to the physical network.

## NIC and Network Hardware
NICs cannot be used for different network hardware.  
**Example:** An NIC made for `Ethernet` won't work with a `Token Ring`.

## NIC and CPU Processing
Some NICs contain their own `micro-processors`.  
The system CPU sends instructions to NIC to transmit data.

# Connection between NIC and Physical Network
1. The NIC contains all the circuitry to connect to the physical medium.
2. The NIC has a wire which connects to additional circuitry which connects to the physical medium.

The `Thin Ethernet` and `10 Base-T Ethernet` are both `Ethernet`.

# Thick Ethernet Wiring
The `thick ethernet` uses coaxial cable, connected by transceivers which are connected to NICs through AUI cable (also known as drop cable).  
Which carries digital and control signals to the transceivers.  
Which generate analogue signals.  
Which are terminated by the `terminators` to avoid signal reflections.  
![[Pasted image 20240603120513.png]]

# Connection Multiplexing
![[Pasted image 20240603120832.png]]

# Thin Ethernet Wiring
The transceivers are built directly into the NIC which use `BNC-T` connectors.  
![[Pasted image 20240603121638.png]]
