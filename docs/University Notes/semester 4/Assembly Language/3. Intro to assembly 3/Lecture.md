---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Introduction
This lecture is about the intel 8088 architecture.

# Intel Iapx88
The word `IAPX88` stands for `Intel Advanced Processor Extensions 88` which is a 16-bit #processor. The 386 on the other hand is 32-bit #processor.

# Register Architecture
There are 14 #register it uses.  
![[Pasted image 20240520204828.png]]

# General Register (AX, BX, CX, DX)
These #register have `X` in the end which stands for `extended`.  
Meaning, these #register are composite of their lower and upper parts.  
**Example:** `AX` (16-bit) consists of `AL`(8-bit) which is its lower part and `AH`(8-bit) which is its upper part.  
Now looking at the first characters of it.
1. A: #accumulator, because it does mathematical and logical operations.
2. B: base, used for memory addressing
3. C: counter, certain operations work with counting.
4. D: destination, act as destination in I/O operations.

# Index Registers (SI and DI)
`SI` stands for `source-index` and `DI` stands for `destination-index`.  
They are used in a special class of instructions called `string instructions`.  
These are 16-bit and are not composite of other parts.

# Instruction Pointer
The Program Control instructions change this #register and it is very dangerous to play around with it.

# Stack Pointer
This is a memory related pointer.

# Base Pointer
This pointer is used to store memory location in a #stack.

# Flags Register
The bits of this #register are expressed as follows:  
![[Pasted image 20240520210529.png]]

| C   | Carry           | When two 16bit numbers are added the answer can be 17 bits long or when two 8bit numbers are added the answer can be 9 bits long. This extra bit that won’t fit in the target register is placed in the carry flag where it can be used and tested.                                                                                                                                                                                                    |
| --- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| P   | Parity          | Parity is the number of “one” bits in a binary number. Parity is either odd or even. This information is normally used in communications to verify the integrity of data sent from the sender to the receiver.                                                                                                                                                                                                                                         |
| A   | Auxiliary Carry | A number in base 16 is called a hex number and can be represented by 4 bits. The collection of 4 bits is called a nibble. During addition or subtraction if a carry goes from one nibble to the next this flag is set. Carry flag is for the carry from the whole addition while auxiliary carry is the carry from the first nibble to the second.                                                                                                     |
| Z   | Zero Flag       | The Zero flag is set if the last mathematical or logical instruction has produced a zero in its destination.                                                                                                                                                                                                                                                                                                                                           |
| S   | Sign Flag       | A signed number is represented in its two’s complement form in the computer. The most significant bit (MSB) of a negative number in this representation is 1 and for a positive number it is zero. The sign bit of the last mathematical or logical operation’s destination is copied into the sign flag.                                                                                                                                              |
| T   | Trap Flag       | The trap flag has a special role in debugging which will be discussed later.                                                                                                                                                                                                                                                                                                                                                                           |
| I   | Interrupt Flag  | It tells whether the processor can be interrupted from outside or not. Sometimes the programmer doesn’t want a particular task to be interrupted so the Interrupt flag can be zeroed for this time. The programmer rather than the processor sets this flag since the programmer knows when interruption is okay and when it is not. Interruption can be disabled or enabled by making this bit zero or one, respectively, using special instructions. |
| D   | Direction Flag  | Specifically related to string instructions, this flag tells whether the current operation has to be done from bottom to top of the block (D=0) or from top to bottom of the block (D=1).                                                                                                                                                                                                                                                              |
| O   | Overflow Flag   | The overflow flag is set during signed arithmetic, e.g. addition or subtraction, when the sign of the destination changes unexpectedly. The actual process sets the overflow flag whenever the carry into the MSB is different from the carry out of the MSB                                                                                                                                                                                           |

# Segment Registers(CS, DS, SS, ES)
Code, Data, Stack and Extra segment #register are related to Intel Segmented memory model.

# Our First Program
We will write our 1st program which adds 3 numbers.

# English Language Version

```
move 5 to ax  
move 10 to bx  
add bx to ax  
move 15 to bx  
add bx to ax
```

# Assembly Language Version

```
operation destination, source
operation destination
operation source
operation
```

These are the four variants.

```
[org 0x0100]
	mov ax, 5    ;load 5 into ax register
	mov bx, 10   ;load 10 into bx register
	add ax, bx   ;add ax and bx and store it in ax
	mov bx, 15   ;load 15 into bx register
	add ax, bx   ;add ax and bx and store it in ax
	mov ax, 0x4c00    ;terminate the program
	int 0x21
```

# Assembler, Linker, Debugger

```
nasm ex01.asm –o ex01.com –l ex01.lst
```

This takes `ex01.asm` file, assembles into `ex01.com` executable and makes a `ex01.lst` listing file which contains the code without comments.

```
00000000:B80500          mov ax, 5
00000003:BB0A00          mov bx, 10
00000006:01D8            add ax, bx
00000008:BB0F00          mov bx, 15
0000000B:01D8            add ax, bx
0000000D:B8004C          mov ax, 0x4C00
00000010:CD21            int 0x21
```

The first column is the `offset` of listed instructions in the output file.  
Next column is the #opcode, `B8` is the instruction adding something to `AX` but it is immediately followed by `0500` which makes it called `immediate operand`.

A `hex` digit requires `4` bits to be represented.  
`2` `hex` digits will require `8` or in simple terms, a `byte`.  
`4` `hex` digits will require `2 bytes` or a `word`.

There are 2 types of ordering the `hex` digits in the memory.  
**Big-endian:** Most significant figure, followed by lesser significant figure, followed by less significant figure, followed by least significant figure. This is used by `Motorola`.  
**Little-endian:** Least significant, followed by less significant, followed by lesser significant, followed by most significant letter. This is used by `Intel`.

The `0500` suggests there are `2` `bytes`, those are: `05` and `00`.  
Since it is `little-endian` so the number `0005` is shown as `0500`.  
Since the instruction itself was `3` bytes long, the offset is shown to be `3` as well.
