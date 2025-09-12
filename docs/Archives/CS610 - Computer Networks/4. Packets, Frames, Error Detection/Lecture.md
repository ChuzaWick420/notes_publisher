---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Packet
Computer networks divide the data into blocks or junks called #packets.  
These blocks are helpful for error detection.

## Problem with Sharing
There are many computers connected to a network and some applications require a lot of data transfer which takes a lot of time.  
Hence, it causes other applications to wait but some applications cannot wait for long periods of time.

## Solution for Fairness
To solve the above mentioned problem, the data is divided into #packets and then each computer takes turns to send the data over the shared network.  
This way, no computer has to experience delays.

# Packet and Time Division Multiplexing
![[Pasted image 20240528132153.png]]

# Packet and Frames
## Packet
A #packets is a generic term. Each hardware uses different formats of #packets.

## Frames
A #frame is defined to be a specific #packets format for a specific hardware technology.  
To define this standard, we attach a `start` and a `tail` header to the #frame.

## Problems
Frames also have some problems in transmission:
1. Missing the `end-of-tail` means computer has crashed.
2. Missing the `start-of-head` means computer missed beginning of the message.
3. Bad #frame is discarded.
