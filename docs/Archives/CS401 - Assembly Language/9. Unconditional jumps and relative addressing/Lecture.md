---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Unconditional Jump

```asm
; a program to add ten numbers without a separate counter
[org 0x0100]
	jmp start ; unconditionally jump over data

num1: dw 10, 20, 30, 40, 50, 10, 20, 30, 40, 50
total: dw 0

start: mov bx, 0 ; initialize array index to zero
	   mov ax, 0 ; initialize sum to zero

l1: add ax, [num1+bx] ; add number to ax
	add bx, 2 ; advance bx to next index
	cmp bx, 20 ; are we beyond the last index
	jne l1 ; if not add next number
	mov [total], ax ; write back sum in memory

	mov ax, 0x4c00 ; terminate program
	int 0x21
```

We can move our `data declaration` at the top but then the interpreter will start to interpret the `data` as the #opcode.  
Therefore, we use an _unconditional jump_ instruction called `JMP`.

# Relative Addressing
The listing file generated is as follows:

```
     1        ; a program to add ten numbers without a separate counter
     2        [org 0x0100]
     3 00000000 E91600    jmp start ; unconditionally jump over data
     4          
     5 00000003 0A0014001E00280032- num1: dw 10, 20, 30, 40, 50, 10, 20, 30, 40, 50
     6 0000000C 000A0014001E002800-
     7 00000015 3200        
     8 00000017 0000       total: dw 0
     9          
    10 00000019 BB0000     start: mov bx, 0 ; initialize array index to zero
    11 0000001C B80000        mov ax, 0 ; initialize sum to zero
    12          
    13 0000001F 0387[0300] l1: add ax, [num1+bx] ; add number to ax
    14 00000023 81C30200      add bx, 2 ; advance bx to next index
    15 00000027 81FB1400      cmp bx, 20 ; are we beyond the last index
    16 0000002B 75F2          jne l1 ; if not add next number
    17 0000002D A3[1700]      mov [total], ax ; write back sum in memory
    18          
    19 00000030 B8004C        mov ax, 0x4c00 ; terminate program
    20 00000033 CD21          int 0x21

```

Pay attention to `line 3`, the `E9` is the operand for the jump but it takes `1600` which translates to `0016` (because of `little endian` format).  
This is a _relative address_ because due to first instruction, the #instruction-pointer was moved to location `0100`.  
Then, It was pointing to `0103` (because of the 3 bytes `offset`, `E9`, `16`, `00`)  
So, `0103 + 0016 = 0119`.

>[!NOTE] `0119` is composite of `0019` and `0100`  
>The `0019` is the `offset` value of our first instruction of the program meanwhile the `0100` is the `offset` created by the first statement `[org 0x0100]`

# Types of Jumps
There are 3 types of jumps.

![[Pasted image 20240606135146.png]]

## Short
If the _relative address_ stored with the instruction is within `8-bits` (or `1 byte`) then it is called `short jump`.

## Near
If the _relative address_ stored with the instruction is within `16-bits` (or `2 bytes`) then it is called `near jump`.

## Far
This jump does not work with _relative addressing_ but works with _absolute addressing_ instead.  
This jump can be used to jump from one code segment to another.  
We need to provide it both `offset` and `segment` values (both `2 bytes` long).  
It uses `CS` #register for the `segment` part and #instruction-pointer for the `offset` part.

The following jump instructions have a `far` variant:
1. JMP
2. CALL
3. RET

>[!NOTE] Conditional Jumps can only be of `short jump` type

# Sorting Example
We will discuss about `bubble sort` [^1] algorithm.

```asm
[org 0x0100]
	jmp start

data: dw 60,55,45,50,40,35,25,30,10,0

swap: db 0

start: mov bx,0              ; initialize array index to zero
		mov byte [swap],0     ; reset swap flag to no swaps

loop1: mov ax,[data+bx]      ; load number in ax
		cmp ax,[data+bx+2]    ; compare with next number
		jbe noswap            ; no swap if already in order
		mov dx,[data+bx+2]    ; load second element in dx
		mov [data+bx+2],ax    ; store first number in second
		mov [data+bx],dx      ; store second number in first
		mov byte [swap],1     ; flag that a swap has been done

noswap: add bx,2              ; advance bx to next index
		cmp bx,18             ; are we at last index
		jne loop1             ; if not compare next two
		cmp byte [swap],1     ; check if a swap has been done
		je start              ; if yes make another pass

	mov ax,0x4c00         ; terminate program
	int 0x21

```

[^1]: Read about [[Bubble Sort]].
