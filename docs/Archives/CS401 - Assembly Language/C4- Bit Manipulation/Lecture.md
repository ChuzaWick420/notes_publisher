---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Multiplication Algorithm
![[Pasted image 20240803200608.png]]  
Imagine if `13` is `multiplicant` and `5` is `multiplier` then we take each `bit` from `mutliplier`, perform an #AND operation, shift the answer a little bit and repeat.

# Shifting and Rotations
There are different types of shifting algorithms

## Shift Logical Right (SHR)

![[Pasted image 20240803201028.png]]

The `0` is pushed from _left_ and all the #bits are moved to _right_ meanwhile the _right most_ `bit` is dropped into `carry flag`.

## Shift Logical Left (SHL) / Shift Arithmetic Left (SAL)
![[Pasted image 20240803201148.png]]  

Same logic as previous one, but the direction is reversed.

## Shift Arithmetic Right (SAR)

![[Pasted image 20240803201407.png]]

This one copies the _left most_ `bit` and pushes it.  
The _right most_ is dropped inside `carry flag`.

The `shift left` operations are basically `multiplication` with `2` and `shift right` operations are basically `division` by `2`.

## Rotate Right (ROR)

![[Pasted image 20240803201711.png]]

The _right most_ bit is copied to `carry flag` and then is pushed to the _left end_.

## Rotate Left (ROL)

![[Pasted image 20240803201730.png]]

Same logic as previous one but reversed.

## Rotate through Carry Right (RCR)

![[Pasted image 20240803201907.png]]

The value inside `carry flag` is copied to the _left end_ and then the _right most_ bit is copied into the `carry flag`.

## Rotate through Carry Left (RCL)
![[Pasted image 20240803202056.png]]

Same logic but direction is reversed.

# Multiplication in Assembly Language
The algorithm for previously discussed problem is:
1. Shift the `multiplier` to the _right_
2. If `CF = 1` add the `multiplicant` to the result
3. Shift the `multiplicant` to the _left_
4. Repeat the algorithm `4` times.

```asm
[org 0x100]
jmp start

multiplicant: db 13
multiplier: db 5
result: db 0

start:  mov cl, 4
		mov bl, [mutliplicant]
		mov dl, [multiplier]

checkbit:   shr dl, 1
			jnc skip
			add [result], bl

skip:   shl bl, 1
		dec cl
		jnz checkbit
		
		mov ax, 0x4c00
		int 0x21
```

# Extended Operations
Imagine we want to multiply 2 `16-bit` numbers.  
Imagine one of the numbers is `1001110001000000` and other is decimal `2`.  
The _left most_ bit is dropped into `carry bit` and hence we get data lose.

## Extended Shifting
We have to deal with the `32-bit` numbers #word by #word.  
We cannot shift the whole number because the operations are limited to the #word size.

```asm
num1:   dd 40000 
		shl word [num1], 1
		rcl word [num1+2], 1
```

the `dd` directive reserves `double word` or `2 words`.

Step 1 is using `shl` and Step 2 is using `rcl` .  
![[Pasted image 20240803212302.png]]

## Extended addition and Subtraction
There is a new operator called `Add With Carry` with mnemonic `ADC`.  
The normal `add` takes `2` operands but `adc` takes `3` operands, the `3rd` one being the `carry bit`.  
Consider an example statement:

```asm
add ax, bx
```

This instruction adds `bx` to `ax`.

```asm
adc ax, bx
```

This instruction adds `carry bit` to `ax` and then adds `bx` to `ax`.

```asm
dest: dd 40000 
src:  dd 80000

mov ax, [src] 
add word [dest], ax
mov ax, [src+2]
adc word [dest+2], ax
```

There is an alternate for `subtraction` as well.  
It is called `subtract with borrow` with mnemonic `SBB`.

## Extended Multiplication

```asm
[org 0x0100]
jmp start

multiplicant: dd 1300                     ;16 bit multiplicant in 32 bits
multiplier:   dw 500                      ;16 bit multiplier
result:       dd 0                        ;32 bit result

start:  mov cl, 16
		mov dx, [multiplier]

checkbit:   shr dx, 1                     ;move right most bit in carry
			jnc skip                      ;if it is zero then skip
			mov ax, [multiplicant]
			add [result], ax
			mov ax, [multiplicant + 2]
			adc [result + 2], ax

skip:   shl word [multiplicant], 1
		rcl word [multiplicant + 2], 1
		dec cl
		jnz checkbit
		
		mov ax, 0x4c00
		int 0x21
```

# Bitwise Logical Operations
These operators are `bitwise`.  
These operators store the result in the first `operand` or `destination`.

## AND Operation

| X   | Y   | X AND Y |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 1   | 0   | 0       |
| 0   | 1   | 0       |
| 1   | 1   | 1       |

```asm
and ax, bx
```

## OR Operation

| X   | Y   | X OR Y |
| --- | --- | ------ |
| 0   | 0   | 0      |
| 1   | 0   | 1      |
| 0   | 1   | 1      |
| 1   | 1   | 1      |

```asm
or ax, bx
```

## XOR Operation

| X   | Y   | X XOR Y |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 1       |
| 1   | 0   | 1       |
| 1   | 1   | 0       |

```asm
xor ax, bx
```

## NOT Operation

```asm
not ax
```

This operator takes one `operand` and flips all the bits.

# Masking Operations
## Selective Bit Clearing
We can use `AND` for this:

```
src  = 1011
mask = 0011
des  = mask and src
     = 0011
```

In the mask the bits which need to be cleared, are set to `0`.

## Selective Bit Setting
We can use `OR` for this:

```
src  = 0101
mask = 0010
des  = mask OR src
     = 0111
```

In the mask, the bits which need to be set to `1`, are set to `1`.

## Selective Bit Inversion
We can use `XOR` for this:

```
src  = 0101
mask = 0010
des  = mask XOR src
     = 0111
```

 In the mask, the bits which need to be flipped are set to `1`.

# Exercises
1. Write a program to swap every pair of bits in the `AX` register.
2. Give the value of the `AX` register and the carry flag after each of the following instructions

```asm
stc
mov ax, <roll num>
adc ah, <first character of your name>
cmc
xor ah, al
mov cl, 4
shr al, cl
rcr ah, cl
```

1. Write a program to swap the nibbles in each byte of the `AX` register.
2. Calculate the number of one bits in `BX` and complement an equal number of least significant bits in `AX`.
3. Write a program to multiply two 32bit numbers and store the answer in a 64bit location.
4. Declare a 32byte buffer containing random data. Consider for this problem that the bits in these 32 bytes are numbered from 0 to 255. Declare another byte that contains the starting bit number. Write a program to copy the byte starting at this starting bit number in the `AX` register. Be careful that the starting bit number may not be a multiple of 8 and therefore the bits of the desired byte will be split into two bytes.
5. `AX` contains a number between 0-15. Write code to complement the corresponding bit in BX. For example if AX contains 6; complement the 6th bit of `BX`.
6. `AX` contains a non-zero number. Count the number of ones in it and store the result back in `AX`. Repeat the process on the result (`AX`) until `AX` contains one. Calculate in `BX` the number of iterations it took to make `AX` one. For example `BX` should contain 2 in the following case:
	1. AX = 1100 0101 1010 0011 (input – 8 ones) 
	2. AX = 0000 0000 0000 1000 (after first iteration – 1 one) 
	3. AX = 0000 0000 0000 0001 (after second iteration – 1 one) STOP
