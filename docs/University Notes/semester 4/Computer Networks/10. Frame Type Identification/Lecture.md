---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Multicasting
There are problems with broadcasting.  
It wastes CPU time to discard the frames for the computers who didn't need the message.

In `multicast`, the interface hardware is programmed in a way to accept multicast address.  
The frames are not directly forwarded to the CPU.

There are 3 types of frames the interface hardware now deals with:
1. `Multicast` frames.
2. Broadcast frames.
3. Frames that were directly destined to the stations (through physical address).

# Multicast Addressing
**Example:** imagine 2 computers running an audio application.  
Their interface is programmed to accept the audio frames.  
Other computers will ignore the frames, who are not running that audio application.

# Identifying Packet Contents
There needs to be a way for destination to know how to interpret the incoming frames.

## Explicit Frame Type
In this type, the identifying value is included with the frame which describes the frame data.

## Implicit Frame Type
In this type, the frame data has to be read and its type is deduced from that data.

# Header Frame Format
![[Pasted image 20240603094710.png]]  
This figures shows the Ethernet frame format  
Those numbers represent `bytes`.

| Fields              | Purpose                           |
| ------------------- | --------------------------------- |
| Preamble            | Receiver Synchronization          |
| Destination Address | Identifies intended receiver      |
| Source Address      | Hardware address of sender        |
| Frame Type          | Type of data carried in the frame |
| Data                | Frame Payload                     |
| CRC                 | 32-bit CRC code                   |

# Frame without Type Fields
Some #LAN technologies do not use the `frame type` field.  
This causes all the computers in the network to agree upon using one single data format.

## Encoding Data Type
The data type is encoded within the frame data.  
![[Pasted image 20240603095551.png]]

## IEEE 802.2 LLC
This standard uses `Logical Link Control Sub Network Attached Point` header.  
![[Pasted image 20240603095857.png]]  
`OUI` stands for `organizationally unique identifier`.

## Unknown Types
Some computers might not have the protocol type installed which makes them blind to the type of frame they are receiving.  
Hence, they discard it.

# Network Analyzers
A `network analyzer` is also called `network monitor` or `network sniffer`.  
It is used to analyze the performance of a network or debug it.  
It shows information like capacity utilization, frame distribution size, collision rates, token circulation time etc.

A computer can be configured as `promiscuous mode` which allows it to see all frames (for analysis).
