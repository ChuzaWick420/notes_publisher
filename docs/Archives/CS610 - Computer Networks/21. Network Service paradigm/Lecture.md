---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Virtual Private Networks
It combines public and private network.  
It is limited to single organization but they use public connection for connectivity.  
These connections are sometimes called `tunnels` or `connect sites`.  
Each site sees `tunnel` as `point-to-point` link.

# Guaranteeing Absolute Privacy
`VPNs` packets are encrypted so if an outsider does gets the packets, they will not be able to interpret information inside it.

# Service Paradigm
Each packet in a network needs to follow a format dictated by the hardware which is called `interface paradigms` or `service paradigms`  
There are 2 types of it:

## Connection Oriented Service
Similar to the telephone systems.  
End points maintain the connection as long as they are communicating.

One end point requests to communicate and the other one grants the access.

### Continuous and Burst Traffic
The connection does not disappear when data is not sent.  
The connection for audio and video is designed continuous meanwhile other networks might use `burst` traffic

### Simplex and Full Duplex Connection
Some connections are `full duplex`.  
To establish a `simplex` connection between 2 computers, there needs to be 2 connections established.  
one from computer `A` to `B` and other one from `B` to `A`.

### Connection Duration and Persistence
There are 2 types:

#### Switched Virtual Circuit
Computer maintains permanent connection to the network and network makes connections on demand.

#### Permanent Switched Circuit
These are originally hard wired and now configured at system unit time.

### Service Guarantees
Some connection-oriented networks might provide guarantees about the service that computer will receive.  
These can be in form of:
- Throughput rate
- Maximum packet loss rate
- ATM provides statistical guarantee about performance.

### Stream of Message Interface
Some provides streams where there is no boundary over data chunk size such as 60 characters.  
Others deliver message interface with same sized chunks.

## Connectionless Service
Similar to postal system.  
End points put data into packets which are sent to network for delivery.

### Interior and Exterior Service Paradigm
Sometimes, the network can use entirely different paradigm externally and internally.  
For example: `ARPANET` uses `connection-oriented` internally and `connection-less` externally

### Comparison
#### Connectionless
- It has fewer overheads
- It is easier to implement

#### Connection Oriented
- Accounting is easier 
- Application can learn of network problems immediately

![[Pasted image 20240726234846.png]]

# Address and Connection Identifiers
