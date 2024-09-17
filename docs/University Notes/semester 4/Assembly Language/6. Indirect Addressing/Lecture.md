---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Size Mismatch

```asm
; a program to add three numbers accessed using a single label
[org 0x0100]
	 mov  ax, [num1]         ; load first number in ax
	 mov  bx, [num1+2]       ; load second number in bx
	 add  ax, bx             ; accumulate sum in ax
	 mov  bx, [num1+4]       ; load third number in bx
	 add  ax, bx             ; accumulate sum in ax
	 mov  [num1+6], ax       ; store sum at num1+6
	 mov  ax, 0x4c00         ; terminate program
	 int  0x21

num1: dw   5
      dw   10
      dw   15
      dw   0
```

if we change the `dw` to `db`, then that means when `mov ax, [num1]` is encountered, it stores `5` and `10` _both_ into the `ax` register because the #register is 16-bit.  
Therefore, it reads `2` bytes (`2` numbers) instead of `1`.

Similarly, `bx` does the same, it stores the 3rd and 4th number.  
rest of the code becomes useless because now `[num1+4]` is going to point beyond of what we have defined.

We can fix this by replacing the `AX` register by `AL`, `BX` with `BL` and the `[num1+2]` offsets to `[num1+1]` etc so the offset is of 1 byte this time, instead of 2.

```asm
; a program to add three numbers accessed using a single label
[org 0x0100]
	 mov  al, [num1]         ; load first number in ax
	 mov  bl, [num1+1]       ; load second number in bx
	 add  al, bl             ; accumulate sum in ax
	 mov  bl, [num1+2]       ; load third number in bx
	 add  al, bl             ; accumulate sum in ax
	 mov  [num1+3], al       ; store sum at num1+6
	 mov  al, 0x4c00         ; terminate program
	 int  0x21

num1: db   5
      db   10
      db   15
      db   0
```

If we try doing something like `mov ax, bl`, this would be illegal because `bl` is of `1` byte meanwhile `ax` is of `2` bytes.

If we do something like:

```asm
mov [num1], 5
```

Although it is a legal statement but the sizes are unknown this time.  
That is why we need

```asm
mov byte [num1], 5
mov word [num1], 5
```

# Register Indirect Addressing
Sometimes, we need to access data across 100 or more data elements.  
In that case, manually writing the memory addresses isn’t really possible.

```asm
[org 0x100]

	mov bx, num1  ;point bx to first number
	mov ax, [bx]  ;load first number in ax
	add bx, 2     ;advance bx to second number (2 bytes)
	add ax, [bx]  ;add second number to ax
	add bx, 2     ;advance bx to third number (2 bytes)
	add ax, [bx]  ;add third number to ax
	add bx, 2     ;advance bx to result (2 bytes)
	mov [bx], ax  ;store sum at num1+6
	mov ax, 0x4c00
	int 0x21
	
num1: dw 5, 10, 15, 0
```

Remember, a label is just a memory address.  
using `[]` means accessing the contents of that memory.

```asm
; a program to add ten numbers
[org 0x0100]
	mov bx,num1 ; point bx to first number
	mov cx,10 ; load count of numbers in cx
	mov ax,0 ; initialize sum to zero

	l1:add ax,[bx] ; add number to ax
	add bx,2 ; advance bx to next number
	sub cx,1 ; numbers to be added reduced
	jnz l1 ; if numbers remain add next

	mov [total],ax ; write back sum in memory

	mov ax,0x4c00 ; terminate program
	int 0x21

num1: dw 10,20,30,40,50,10,20,30,40,50
total: dw 0
```

The program is doing as follows:
1. store address `num1` into `bx`.
2. store `10` into `cx` (for counting).
3. store `0` in `ax`
4. set a label which adds contents of `bx` to `ax`.
5. Move the pointer `bx`.
6. Decrement the counter by 1.
7. Jump to `step 4` if `cx`(memory in preceding instruction) is not `0`.

>[!NOTE] JNZ stands for “jump if not zero”  
>The `memory` in the preceding instruction should be `zero` for the `zero flag` to be set so the jump instruction can stop but this flag is only set when the result in destination is `zero` by a Mathematical or Logical operation.  
>Meaning, doing `mov ax, 0` will not set the `zero flag` as it is not a math or logic operation

Since we are using a #register to access memory.  
Therefore, we call this sort of access as #register-indirect-memory-access.

If we use `BX` or `BP` then it is called #based-addressing.  
If we use `DI` or `SI` then it is called #indexed-addressing.
