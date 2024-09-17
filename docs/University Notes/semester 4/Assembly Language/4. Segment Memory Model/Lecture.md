---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Rationale
The `8080` and `8085` both are linear models (meaning, an array) but due to 16-bit `address bus`, it can only target `2^16 = 64k` memory locations.  
Then #segmented-memory-model (used by `8085`) was introduced to extend this limit.

There are `3` sections of program.
1. Code
2. Data
3. Program’s Stack  
These `3` sections are not distinguishable in the `linear model` but they _are_ in #segmented-memory-model.

# Mechanism
There are multiple windows, each for a specific section.  
The memory size of `8088` is `1MB` which can be addressed by 20-bit address bus.  
These memory windows are assigned to each segment.  
`extra segment` can be used when we need to access `2` different areas of memory but cannot be accessed from same window (meaning, both areas are from separate windows).  
It can be used as an extra `data segment`.

Segment #register tells where to open the _window_ of size 64KB.  
The `Base` and `offset` are used as variables.  
The segment tells the `base` meanwhile `offset` is added to it.

The #instruction-pointer cannot work alone.  
Firstly, a _window_ of 64KB is opened by `code segment` #register which stores the `base`.  
The #instruction-pointer uses this base as a reference of starting and then moves using the `offsets`.  
Since it is 16-bit in itself as well, it cannot move outside that `64Kb` window.  
When the CS #register changes the base, the window is moved and #instruction-pointer also behaves relatively.  
![[Pasted image 20240521165648.png]]

# Physical Address Calculator
The `code segment` #register and `offset` both are 16-bit in size.  
However, we need 20-bit address to address `1MB` memory.  
There should be a way for both of these `16-bit` registers to make up a `20-bit` address.

![[Pasted image 20240521170745.png]]  
The `code segment` gets 4 `zeros` appended to the right.  
The `offset` gets 4 `zeros` appended to the left.  
Then these are added together.  
![[Pasted image 20240521171002.png]]  
There _maybe_ a `carry` bit which gets generated but it is not stored.  
This whole phenomena is called `address wraparound`.

# Paragraph Boundaries
The `segment` value itself is a 16-bit number in a 20-bit physical address.  
This 16-bit boundary is called `paragraph boundaries`.

# Overlapping Segments
Segments can also overlap.  
Means if the `CS`, `DS`, `SS` and `ES` all have the same values, they (segments or windows) all are overlapping.

The partially overlapping segments can also point to the same exact physical memory location.  
Consider this example:  
![[Pasted image 20240521180939.png]]  
The segment pointed by `CS` #register is `1DDD:0100`.  
Where `1DDD` is the `base` of the `code segment` and `0100` is the `offset`.  
Then we append `4` bits (1 `hex` digit) for addition (to figure out the physical address).  
The result of that addition is `1DED0`.

Now, we can also open a segment pointed by `DS` #register at `1DED` with `offset` `0000` which when added, results into `1DED0`.

Hence this proves that even the partially overlapping segments can point to same memory address.

This pair of `segment:offset` is called #logical-address.

# Exercises
1. How the processor uses the address bus, the data bus, and the control bus to communicate with the system memory?
2. Which of the following are unidirectional and which are bidirectional?
	1. Address Bus
	2. Control Bus
	3. Data Bus
3. What are registers and what are the specific features of the accumulator, index registers, program counter, and program status word?
4. What is the size of the accumulator of a 64bit processor?
5. What is the difference between an instruction mnemonic and its opcode?
6. How are instructions classified into groups?  
7. A combination of 8bits is called a byte. What is the name for 4bits and for 16bits?
8. What is the maximum memory 8088 can access?
9. List down the 14 registers of the 8088 architecture and briefly describe their uses.
10. What flags are defined in the 8088 FLAGS register? Describe the function of the zero flag, the carry flag, the sign flag, and the overflow flag.
11. Give the value of the zero flag, the carry flag, the sign flag, and the overflow flag after each of the following instructions if AX is initialized with 0x1254 and BX is initialized with 0x0FFF.
	1. add ax, 0xEDAB
	2. add ax, bx
	3. add ax, bxp
12. What is the difference between little endian and big endian formats? Which format is used by the Intel 8088 microprocessor?  
13. For each of the following words identify the byte that is stored at lower memory address and the byte that is stored at higher memory address in a little endian computer.
	1. 1234
	2. ABFC
	3. B100
	4. B800
14. What are the contents of memory locations 200, 201, 202, and 203 if the word 1234 is stored at offset 200 and the word 5678 is stored at offset 202?
15. What is the offset at which the first executable instruction of a COM file must be placed?
16. Why was segmentation originally introduced in 8088 architecture?
17. Why a segment start cannot start from the physical address 55555.
18. Calculate the physical memory address generated by the following segment offset pairs.
	1. 1DDD:0436
	2. 1234:7920
	3. 74F0:2123
	4. 0000:6727
	5. FFFF:4336
	6. 1080:0100
	7. AB01:FFFF  
19. What are the first and the last physical memory addresses accessible using the following segment values?
	1. 1000
	2. 0FFF
	3. 1002
	4. 0001
	5. E000
20. Write instructions that perform the following operations.
	1. Copy BL into CL
	2. Copy DX into AX
	3. Store 0x12 into AL
	4. Store 0x1234 into AX
	5. Store 0xFFFF into AX
21. Write a program in assembly language that calculates the square of six by adding six to the accumulator six times.
