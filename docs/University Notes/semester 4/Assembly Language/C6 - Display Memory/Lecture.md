---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# ASCII Code
The ASCII is defined as `7-bit` meanwhile the extended version is `8-bit`.  
We can add `0x30` to the numbers to represent their ASCII form (since the numbers themselves lie in range 30-39)

# Display Memory Formation
We can send `ASCII` codes to `VGA` to print specific characters.  
The screen has `80` rows and `25` columns.  
Each `character` needs `1 word`, first `byte` being the character code and 2nd one being the `attribute byte`.

## Display Memory Base Address
The display video memory starts from `B8000`

## Attribute Byte
This holds the `foreground` and `background` color for the character and is also called `video attribute`.

![[Pasted image 20240804010346.png]]

1. Blue component of foreground color
2. Green component of foreground color
3. Red component of foreground color
4. Intensity component of foreground color
5. Blue component of background color
6. Green component of background color
7. Red component of background color
8. Blinking of foreground character

## Display Examples
We can use `DS` or `ES` but to keep semantic separation, we use `DS` for data and `ES` for video.  
Also, we cannot directly load an address into `segment registers`.  
Therefore, we use `AX` as such:

```asm
mov ax, 0xb800 
mov es, ax
```

```as
mov word [es:0], 0x0741
```

the `41` indicates it is character `A` and `07` is the attribute byte suggesting a white foreground (since all the RGB channels are ON).

```asm
mov word [es:160], 0x1230
```

This is displayed at the 2nd row, 1st column.  

```asm
[org 0x0100]

mov ax, 0xb800       ; load video base in ax
mov es, ax           ; point es to video base
mov di, 0            ; point di to top left column

nextchar: 
    mov word [es:di], 0x0720 ; clear next char on screen
    add di, 2                ; move to next screen location
    cmp di, 4000             ; has the whole screen cleared
    jne nextchar             ; if no clear next position

mov ax, 0x4c00       ; terminate program
int 0x21             ; interrupt to DOS
```

# Hello World in Assembly
We can define the characters as such:

```
db 0x61, 0x62, 0x63 
db 'a', 'b', 'c' 
db 'abc'
```

```asm
[org 0x0100]
jmp start

message: 
    db 'hello world'  ; string to be printed
length: 
    dw 11             ; length of the string

; subroutine to clear the screen
clrscr: 
    push es
    push ax
    push di
    mov ax, 0xb800
    mov es, ax        ; point es to video base
    mov di, 0         ; point di to top left column
nextloc: 
    mov word [es:di], 0x0720 ; clear next char on screen
    add di, 2               ; move to next screen location
    cmp di, 4000            ; has the whole screen cleared
    jne nextloc             ; if no, clear next position
    pop di
    pop ax
    pop es
    ret

; subroutine to print a string at top left of screen
; takes address of string and its length as parameters
printstr: 
    push bp
    mov bp, sp
    push es
    push ax
    push cx
    push si
    push di
    mov ax, 0xb800
    mov es, ax             ; point es to video base
    mov di, 0              ; point di to top left column
    mov si, [bp+6]         ; point si to string
    mov cx, [bp+4]         ; load length of string in cx
    mov ah, 0x07           ; normal attribute fixed in al
nextchar: 
    mov al, [si]           ; load next char of string
    mov [es:di], ax        ; show this char on screen
    add di, 2              ; move to next screen location
    add si, 1              ; move to next char in string
    loop nextchar          ; repeat the operation cx times
    pop di
    pop si
    pop cx
    pop ax
    pop es
    pop bp
    ret 4

start: 
    call clrscr            ; call the clrscr subroutine
    mov ax, message
    push ax                ; push address of message
    push word [length]     ; push message length
    call printstr          ; call the printstr subroutine
    mov ax, 0x4c00         ; terminate program
    int 0x21               ; interrupt to DOS
```

# Number Printing in Assembly
A problem is that the number `10` has its own `ASCII` code.  
You cannot add the codes of `1` and `0`.

## Number Printing Algorithm
The algorithm is pretty simple:
- Divide the number by base (10 in case of decimal)
- The remainder is its right most digit
- Convert the digit to its ASCII representation (Add 0x30 to the remainder in case of decimal)
- Save this digit on stack
- If the quotient is non-zero repeat the whole process to get the next digit, otherwise stop
- Pop digits one by one and print on screen left to right

## DIV Instruction
This is an `integer` division instruction.  
There are 2 forms of it.
1. The first form divides a `32-bit` number in `DX:AX` by its `16-bit` operand and puts the `remainder` in `DX` and `quotient` in `AX`.
2. The second form divides a `16-bit` number in `AX` by its `8-bit` operand and puts `remainder` in `AH` and `quotient` in `AL`.

If the `quotient` exceeds the size of destination register then a `type 0` interrupt is generated which is same for `divide by zero`.

## Number Printing Example

```asm
[org 0x0100]
jmp start

;;;;; COPY LINES 008-025 FROM EXAMPLE 6.2 (clrscr) ;;;;;
; subroutine to clear the screen
clrscr: 
    push es
    push ax
    push di
    mov ax, 0xb800
    mov es, ax        ; point es to video base
    mov di, 0         ; point di to top left column
nextloc: 
    mov word [es:di], 0x0720 ; clear next char on screen
    add di, 2               ; move to next screen location
    cmp di, 4000            ; has the whole screen cleared
    jne nextloc             ; if no, clear next position
    pop di
    pop ax
    pop es
    ret

; subroutine to print a number at top left of screen
; takes the number to be printed as its parameter
printnum: 
    push bp
    mov bp, sp
    push es
    push ax
    push bx
    push cx
    push dx
    push di
    mov ax, 0xb800
    mov es, ax             ; point es to video base
    mov ax, [bp+4]         ; load number in ax
    mov bx, 10             ; use base 10 for division
    mov cx, 0              ; initialize count of digits
nextdigit: 
    mov dx, 0              ; zero upper half of dividend
    div bx                 ; divide by 10
    add dl, 0x30           ; convert digit into ascii value
    push dx                ; save ascii value on stack
    inc cx                 ; increment count of values
    cmp ax, 0              ; is the quotient zero
    jnz nextdigit          ; if no, divide it again
    mov di, 0              ; point di to top left column 
nextpos: 
    pop dx                 ; remove a digit from the stack
    mov dh, 0x07           ; use normal attribute
    mov [es:di], dx        ; print char on screen
    add di, 2              ; move to next screen location
    loop nextpos           ; repeat for all digits on stack
    pop di
    pop dx
    pop cx
    pop bx
    pop ax
    pop es
    pop bp
    ret 2

start: 
    call clrscr            ; call the clrscr subroutine
    mov ax, 4529
    push ax                ; place number on stack
    call printnum          ; call the printnum subroutine
    mov ax, 0x4c00         ; terminate program
    int 0x21               ; interrupt to DOS
```

# Screen Location Calculation

$$location = \left((row \times 80) + column\right) \times 2$$

The `2` is there due to `word` being used for a `character`.

## MUL Instruction
It is `unsigned multiplication`.  
If the operand is a `byte` then it is multiplied by `AL` and result is stored in `AH` and `AL`.  
If it is a `word` then it is multiplied by `AX` and result is stored in `DX` and `AX`.

## String Printing at Desired Location

```asm
[org 0x0100]
jmp start

message: 
    db 'hello world'  ; string to be printed
length: 
    dw 11             ; length of the string

; subroutine to clear the screen
clrscr: 
    push es
    push ax
    push di
    mov ax, 0xb800
    mov es, ax        ; point es to video base
    mov di, 0         ; point di to top left column
nextloc: 
    mov word [es:di], 0x0720 ; clear next char on screen
    add di, 2               ; move to next screen location
    cmp di, 4000            ; has the whole screen cleared
    jne nextloc             ; if no, clear next position
    pop di
    pop ax
    pop es
    ret

; subroutine to print a string at desired screen location
; takes x position, y position, string attribute, address of string
; and its length as parameters
printstr: 
    push bp
    mov bp, sp
    push es
    push ax
    push cx
    push si
    push di
    mov ax, 0xb800
    mov es, ax        ; point es to video base
    mov al, 80        ; load al with columns per row
    mul byte [bp+10]  ; multiply with y position
    add ax, [bp+12]   ; add x position
    shl ax, 1         ; turn into byte offset
    mov di, ax        ; point di to required location
    mov si, [bp+6]    ; point si to string
    mov cx, [bp+4]    ; load length of string in cx
    mov ah, [bp+8]    ; load attribute in ah
nextchar: 
    mov al, [si]      ; load next char of string
    mov [es:di], ax   ; show this char on screen
    add di, 2         ; move to next screen location
    add si, 1         ; move to next char in string
    loop nextchar     ; repeat the operation cx times
    pop di
    pop si
    pop cx
    pop ax
    pop es
    pop bp
    ret 10

start: 
    call clrscr       ; call the clrscr subroutine
    mov ax, 30
    push ax           ; push x position
    mov ax, 20
    push ax           ; push y position
    mov ax, 1         ; blue on black attribute
    push ax           ; push attribute
    mov ax, message
    push ax           ; push address of message
    push word [length] ; push message length
    call printstr     ; call the printstr subroutine
    mov ax, 0x4c00    ; terminate program
    int 0x21          ; interrupt to DOS
```

# Exercises
