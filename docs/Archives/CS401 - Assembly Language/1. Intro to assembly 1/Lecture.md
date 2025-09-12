---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Introduction
#assembly language is used to directly talk to the computer.  
In terms of higher programming languages like #cpp or #python, the #compiler and #interpretor acts as a bridge between the programmer and the computer.

# Basic Computer Architecture
A computer consists of #processor, #memory and #I/O devices.  
There should be mechanisms to:
- Specify that data needs to be read.
- Specifies the precise location of the #memory.
- Transfer of data from #memory to #processor.

There are group of bits collectively called `buses`.  
There are 3 types:
1. **Address bus:** These bits are used to specify the memory location to be read or written to. These are _uni-directional_.
2. **Data bus:** These bits carry the data between #processor and #memory. These are _bi-directional_
3. **Control bus:** These bits carry control operations such as specifying if the data is to be read or written.  
![[Pasted image 20240519200845.png]]

The number of #bits in a cell is called `cell-width`.  
The width of #data-bus has to be equal to the `cell-width`.

The #control-bus has to synchronize the #processor and the #memory to establish the connection between them.

# Registers
These are temporary storage inside the #processor to hold data such as `operands` on which the operations are performed.  
These are named depending on the architecture, according to a nomenclature (rules of naming things).
