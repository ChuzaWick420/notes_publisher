---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Carrier Sense with Multiple Access(CSMA)
#CSMA is a coordinate technique which tells how the computers communicate over a shared medium.  
The computers _listen_ to the carrier (they read codes which define the status of the channel).  
When the carrier channel is idle, the computer starts to communicate.

# Collision Detection and Back off with CSMA/CD
## Collision Detection
The phenomena in which multiple frames interfere with each other, is called `collision`.

## Ethernet CD
For collision detection, Ethernet includes a hardware which detects transmission.  
It does the following operations:
1. It monitors outgoing signals
2. Grabbled signal is interpreted as a collision

## Recovery from Collision
When a collision is detected by a computer, it sends special signals to all other interfaces that a collision has happened.  
Then the computers wait for the channel to be idle.  
If the delay time (the waiting period) is _same_ for both computers, then they will transmit the frames at same time and a collision will happen again.  
To fix this problem, both the computers choose random delays.

## Exponential Backup
Due to busy medium, collisions might still happen.  
Therefore, the delays are doubled.  
It reduces the chances of collision.

# 802.11 Wireless LANs and CSMA/CA
The `IEEE 802.11 wireless LAN` standard uses radio signals at `2.4 GHz`.  
Its data rate is `11 Mbps`.  
The older device uses radio signals at `900 MHz` with data rate `2 Mbps`.

## Limited Connectivity With Wireless
Not all participants might be able to communicate with each other.  
Following are the reasons:
1. It has low signal strength.
2. The propagation is blocked by walls
3. It cannot use CD to avoid interference because not all participants may hear.

![[Pasted image 20240602181347.png]]  
Here `d` represents the maximum range of the signals.  
According to the figure, computer `2` can communicate with both, `1` and `3` but computer `1` cannot communicate with computer `3` and vise versa.

## CSMA/CA
The wireless #LAN uses `collision avoidance` instead of `collision detection`.  
The transmitter sends very short message to the receiver.  
Then the receiver broadcasts to all transmitters, a short message reserving slot for that transmitter.

## Collision
The receiver might get the request at same time.  
In this scenario, there is a collision at the receiver's side and no reservation is sent to the transmitters.  
The transmitters use backup and retry.  
When requests are received, the receiver selects one of them and reservation for that transmitter is sent.

# Local Talk
`Apple` invented the bus topology for the #LAN.  
The `Mac` computers have a default #LAN port.  
Its speed is about `230.4Kbps`.  
It uses `CSMA/CA`.

# Token Ring
![[Pasted image 20240602183148.png]]  
The sender holding token sends the message.  
It travels along the ring, passes through the computers.  
When it reaches the destination, the data is copied.

## Using the Token
The `token` is like a permit which allows a computer to send data.  
After the transmission is done, the `token` is also passed along the ring.

## Token and Synchronization
There is only 1 `token` within the whole ring.  
If the `token` is for some reason, lost, then it is re-generated by the hardware.  
The `token` gives power to a computer to transmit one frame.  
If all the computers are ready for transmission, then `round robin access` is enforced.

## IDM Token Ring
It uses a special cable to connect the computers to the ring interface.  
Its speed was originally `4 Mbps` but now it is up to `16 Mbps`.

# FDDI
`Fiber distributed data interconnect` is another `ring` #topology.  
It uses fiber optics and sends data at about `100 Mbps`.  
![[Pasted image 20240602184906.png]]

# ATM (Start Network)
`Asynchronous Transferred Mode` technology consists of electronic packet switches to which computers can connect  
![[Pasted image 20240602185140.png]]

## Details
1. It uses fiber optic cables.
2. It can transmit over `100 Mbps`.
3. The connection per computer uses 2 fiber optics.  
![[Pasted image 20240602185316.png]]