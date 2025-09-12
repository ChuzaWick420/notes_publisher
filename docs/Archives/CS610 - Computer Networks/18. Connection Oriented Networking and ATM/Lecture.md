---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Connection-Oriented Networking and ATM
`ATM` is the only technology which meets the common goal of #LAN and #WAN.  
It uses `connection oriented` networking.  
It provides universal service of audio, video to its customers.

# ATM Design and Cells
## Jitter
It means variance in transmission delays.

## Packet Sizes
Large packets cause fewer overheads because a very small portion is used for header information.

Optimum networks use 4 KB packet size.  
Larger ones cannot be used for audio.  
**Example:** If the speed is about  

$$s = \frac{125 \micro seconds}{sample}$$

Then to fill one `4 KB` packet (assuming each sample is of `8-bit`).  

$$\frac{125 \micro seconds}{sample} \times 8 \times 4 \times 1000 bits$$

$$\frac{125 \micro seconds}{sample} \times 4 \times 1000 \left(8 bits\right)$$

$$\frac{125 \micro seconds}{sample} \times 4 \times 1000 samples$$

$$0.5 seconds$$

## ATM Cells
Each cell has 53 octets.  
VPI/VCI fields identify the cells destination.  
ATM header is about 10% of the cell.  
Engineers sometimes call the ATM overhead as `cell tax`.  
![[Pasted image 20240603211649.png]]

# Connection-Oriented Service
This paradigm is similar to how telephones are used.  
In data communication, a binary connection identifier is given to both parties (caller and receiver) to identify the connection.

# Virtual Channel (or Circuits)
The connections in `ATM` are called `virtual circuits` since these are not physical connections but rather depend on the starting values in memory (tables).

The `VC` (`virtual channel`) is `24-bit` and consists of 2 parts:
1. `Virtual Path Identifier` (`VPI`, `8-bit`) which identifies a particular path through the network
2. `Virtual Channel Identifier` (`VCI`, `16-bit`) which identifies the channel in the virtual path being used by the connection.
