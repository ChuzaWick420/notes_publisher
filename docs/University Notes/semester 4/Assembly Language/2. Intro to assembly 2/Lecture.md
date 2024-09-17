---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Introduction
There are 8-bit #register such as `AH`, `AL`, `BH`, `BL` etc.  
Then there are 16-bit #register such as `AX`, `BX`, `CX` etc.

# Accumulator
There is a central #register in a #processor which is used to perform Mathematical and Logical operations, which is called #accumulator.  
The `word-size` of a #processor is equal to the memory width of the #accumulator, which is normally 32-bits.

# Pointer, Index, Base Registers
These #register are not used to store data but to store the address of the data.  
Take an example where a #for-loop is used to iterate over an array.  
We store the `index` of array in the register which behaves as a navigation point.  
Therefore, we generally use these #register when the memory addresses are unknown before the #run-time-environment has been triggered.

# Flag Registers or Program Status Registers
These #register are also 32-bit or 16-bit in size.  
However, unlike the #accumulator, the whole group of bits in meaningless as a unit.  
Rather, its value lies inside individual bits.

# Program Counter or Instruction Pointer
Our program consists of instructions which need to be executed in sequence, one after the other.  
This #register stores the address of the next instruction to be executed.  
Our instructions like “add“ need to be translated into _numbers_ for the computer to understand.  
This _number_ is called an #opcode.  
But remembering these #opcode is difficult.  
Therefore, we map symbols to them, called #instructions-mnemonics through a program called the #assembler.

# Instruction Groups
The #instructions-mnemonics depend on the manufacturer.  
Looking at the group of these #instructions-mnemonics alone tells a lot about the underlying architecture.  
These groups are called #instruction-set.

# Data Movement Instructions

```asm
mov ax, bx
lda  1234
```

# Arithmetic and Logic Instructions

```asm
add ax, 1234
add bx, 0534
add bx, [1200]
```

The brackets `[]` indicate a memory location.

# Program Control Instructions

```asm
cmp ax, 0  
jne 1234
```

Sometimes we want to manipulate the basic behavior of the #instruction-pointer to jump to some other part of code execution.  
In the above code block, we are comparing if `ax` is equal to `0`, if it is, then we jump to memory location `1234`.

# Special Instructions
There are some special ones as well like:

```asm
cli
sli
```

To simply put, `cli` stops the #processor from listening to external things (could be done to make the #processor perform the important task at hand).  
`sli` command restores the normal functionality of the #processor.
