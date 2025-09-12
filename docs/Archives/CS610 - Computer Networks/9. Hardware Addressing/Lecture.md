---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Hardware Addressing and Frame Type Identification
The sending computer identifies the type of data stored inside the frame.  
The sending computer also uses hardware address to identify the destination computer.

# Specifying a Destination
The hardware interface detects the frames and extracts the data from it.  
However, the data is sent to all the computers.  
There needs to be a way to specify the exact destination computer.

# Hardware Addressing
Each device has a hardware or physical address which is included in the transmitted frame.  
So if the address matches, the frame is received.  
Otherwise, it is ignored.

# LAN Hardware AND Packet Filtering
![[Pasted image 20240602194840.png]]

The #LAN interface does the following:
1. Adds hardware addresses and error detection codes to outgoing frames.
2. It obeys the `CMSA/CD` rules.
3. It analyzes the hardware address from incoming frames.
4. It also checks for error detection codes.
5. It may use #dynamic-memory-access to copy data from the main memory.
6. It may use #dynamic-memory-access to copy data to the main memory.

The frames which are not for the destination, are ignored.

# Format of Hardware Address
It consists of numeric value and its size is selected for specific network technology.  
The length is 1-6 bytes.

## Assigning Hardware Address
There are 3 types of addresses.

### Static
In this type, the manufacturer assigns a permanent hardware address to the interface and he is also responsible in keeping them unique.

### Configurable
These addresses can be set up by the end user either electronically by using some software or manually by using switches or jumpers.

### Dynamic
In this one, a new address is automatically assigned when the hardware turns on.

# Broadcasting
There is a special broadcast address as well which is captured by all the stations.
