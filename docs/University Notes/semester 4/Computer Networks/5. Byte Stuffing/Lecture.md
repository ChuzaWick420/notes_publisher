---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Byte Stuffing
Sometimes when a #frame is read, the `start-of-head` or `end-of-tail` may appear in the #frame data itself. 

>[!NOTE] The bytes similar to `start-of-head` and `end-of-tail` appearing within the #frame can confuse the receiver for the actual #frame headers.

The solution for this problem is called #byte-stuffing.

To distinguish between the data being sent and the control information such as #frame delimiters, the data that is being sent is modified. This technique is called `data-stuffing`.

## Types
There are `2` types of `data-stuffing`:
1. #byte-stuffing 
2. `bit-stuffing`

### Byte Stuffing
Each one of the reserved bytes (which indicates the #frame headers) are replaced by 2 unreserved bytes, one of them acts as a prefix.

Note: `soh` stands for `start-of-head`, `eot` stands for `end-of-tail`.

| Original Data | Modified Data |
| ------------- | ------------- |
| soh           | esc x         |
| eot           | esc y         |
| esc           | esc z         |

![[Pasted image 20240528171941.png]]

### Bit Stuffing
This refers to bit oriented hardware, as opposed to #byte-stuffing which is byte oriented hardware.

# Transmission Error
These may occur due to power surges or interference due to which the bytes or bits get corrupted.

# Error Detection and Correction
#frame includes additional information which is added by the sender for error detection and correction.  
The incorrect data is either rejected or it is corrected first and then accepted.

# Parity Checking
This is one of the error detection schemes.

## Even Parity
The number of `1`s in the data should be even.

## Odd Parity
The number of `1`s in the data should be odd.

## Parity Bit
This is that extra bit that is transmitted along with the data so we can use #even-parity or #odd-parity.

## Limitations of Parity Checking
The error detection offered by it is very limited.  
Imagine the original data:  
101<span style="color: green;">10</span>1.  
Due to noise, it gets corrupted to:  
101<span style="color: red;">01</span>1.

>[!NOTE] The total number of bits _before_ or _after_ the corruption are still even.

# Alternative Error Detection Schemes
There are other techniques as well but they differ from each other in following aspects:
1. The size of additional information (transmission overhead).
2. Computational complexity of the algorithms (computational overhead).
3. The number of bit errors which can be detected.

# Checksum
In this technique, the data is treated as integers and its arithmetic sum is computed.  
Then on the receiving end, same thing is done and if the results match then there is no errors.

## Limitations
It also has limitations.  
![[Pasted image 20240528181235.png]]

See how the corrupted data is not detected because the checksum turns out to be same for both.

# Cyclic Redundancy Check
The message data is treated as co-efficient of a polynomial.  
Then this set of co-efficient is divided by a known polynomial and the remainder of this division is sent to the receiver for checking.

## Hardware Components Used in CRC
There are 2 hardware components it uses.
1. Shift register
2. XOR gate
