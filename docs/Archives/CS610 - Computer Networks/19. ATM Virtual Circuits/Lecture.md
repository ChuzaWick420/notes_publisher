---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Label Switching
As the cells arrive at the ATM, their `VPI/VCI` is modified by a forwarding table and the `VPI/VCI` is changed for the cell's trip.

## Label Writing
The above mentioned process is called `rewriting`. ATM, therefore, is called a `label writing` or `label switching` system.

![[Pasted image 20240726183445.png]]

# An Example ATM Network
![[Pasted image 20240726183732.png]]

# Permanent Virtual Circuits
ATMs can provide customers with virtual circuits that look like traditional leased digital circuits.  
Such `Parmanent Virtual Circuits` last as long as the customer pays periodic fee for em.  
The forwarding table entries are _statically_ configured and are automatically restored after the power of equipment fails. The term used for this is called `provisioning`.  
`Provisioning` requires 2 steps:
1. To determine each `switch` that will be taken in the complete path.
2. To choose appropriate `VPI/VCI` for each step of the path.

# Switched Virtual Circuits
## Establishing an SVC
The computer sends a connection request to the switch it is attached to, which later finds a network path to `destination` and sends along the connection request.  
Each `switch` in the path chooses a `VPI/VCI` to establish a path to the destination and after that, a message is sent back to the original PC indicating that the `SVC` is ready.  
If any of the `switches` fails, an error message is sent back to the original PC.

## Signaling
The networking is not only used for data communication but there is also control messages communicated. The term used for such communication is called `signaling`.

# Quality of Service
## Providing Desired QoS
These are specified at the time of connection setup.  
The `switches` then reserve resources and hence are never altered.  
If a `switch` fails to reserve resources, an error message is sent back.

## ATM QoS Specification
There are 3 types of these:

### Constant Bit Rate
Used in audio and video since they have predefined maximum data rates.

### Variable Bit Rate
Used in compressed audio and video because the data rates depends on the level of compression being used

### Available Bit Rate
Used in typical applications where data rate is unknown and whatever is available at the time, is used.
