---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# String Processing
`string instructions` can do block worth of processing and hence are also called `block processing`.  
There are `5` _processing blocks_.  
There is a prefix which does the operation over a chunk of data instead of single memory cell called `REP`.  

The `DI` and `SI` are used in these instructions.  
When we need a source, the `DS:SI` holds the memory address pointer to it.  
When we need a destination, the `ES:DI` holds the memory address pointer to it.  
These instructions can work from _start_ of memory to the _end_ or from _end_ to the _start_.  
This direction is controlled by `Direction Flag`.

If this flag is `0` then we are in _auto increment_ mode and is done by `cld` statement (clear direction)  
If this flag is `1` then we are in _auto decrement mode and is done by `std` statement (set direction)

## STOS
Stands for `store string`.  
It is used to either transfer a `byte` from `AL` or a `word` from `AX` to the `ES:DI` and increments `DI` by `1` if `STOSB` was used or `2` if `STOSW` was used.  
If the `Direction Flag` is set, then it is decremented.

If `REP` is used, the instruction will be repeated `CX` times and it also decrements `CX` as well.

## LODS
Stands for `load string`.  
It stores the value from `DS:SI` into `AL` or `AX` and `SI` is incremented  
The `REP` prefix is not used since the previous values of `AX` would be overwritten and hence, useless.

## SCAS
Stands for `scan string`.  
It compares the `bytes` or `words` in `AL` or `AX` registers with the value stored in `ES:DI` and updates the flags.  
The prefixes `REPE` (repeat while equal) or `REPNE` (repeat while not equal) are used with it.

## MOVS
Stands for `move string`.  
This instruction transfer `byte` or `word` from `DS:SI` to `ES:DI`.

## CMPS
Stands for `compare string`.  
This subtracts `DS:SI` from `ES:DI`  
It also uses `REPE` and `REPNE` and repeats until the blocks of memory are either keep being equal or not equal depending on which one was used.

## REP Prefix
Repeats a string instruction `CX` times.

## REPE and REPNE Prefixes
`REPE` repeats a string instruction if the `zero flag` is `1`.  
`REPNE` repeats a string instruction if the `zero flag` is `0`.

# STOS Example - Clearing the Screen

```asm
[org 0x0100]
jmp start

; subroutine to clear the screen
clrscr: 
    push es
    push ax
    push cx
    push di
    mov ax, 0xb800
    mov es, ax        ; point es to video base
    xor di, di        ; point di to top left column
    mov ax, 0x0720    ; space char in normal attribute
    mov cx, 2000      ; number of screen locations
    cld               ; auto increment mode
    rep stosw         ; clear the whole screen
    pop di
    pop cx
    pop ax
    pop es
    ret

start: 
    call clrscr       ; call clrscr subroutine
    mov ax, 0x4c00    ; terminate program
    int 0x21          ; interrupt to DOS
```

# LODS Example - String Printing

```asm
[org 0x0100]
jmp start

message: 
    db 'hello world'  ; string to be printed
length: 
    dw 11             ; length of string

; subroutine to clear the screen
clrscr: 
    push es
    push ax
    push cx
    push di
    mov ax, 0xb800
    mov es, ax        ; point es to video base
    xor di, di        ; point di to top left column
    mov ax, 0x0720    ; space char in normal attribute
    mov cx, 2000      ; number of screen locations
    cld               ; auto increment mode
    rep stosw         ; clear the whole screen
    pop di
    pop cx
    pop ax
    pop es
    ret

; subroutine to print a string
; takes the x position, y position, attribute, address of string, and its length as parameters
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
    cld               ; auto increment mode
nextchar: 
    lodsb             ; load next char in al
    stosw             ; print char/attribute pair
    loop nextchar     ; repeat for the whole string
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

# SCAS Example - String Length

```asm
[org 0x0100]
jmp start

message: 
    db 'hello world', 0 ; null terminated string

; subroutine to clear the screen
clrscr: 
    push es
    push ax
    push cx
    push di
    mov ax, 0xb800
    mov es, ax        ; point es to video base
    xor di, di        ; point di to top left column
    mov ax, 0x0720    ; space char in normal attribute
    mov cx, 2000      ; number of screen locations
    cld               ; auto increment mode
    rep stosw         ; clear the whole screen
    pop di
    pop cx
    pop ax
    pop es
    ret

; subroutine to print a string
; takes the x position, y position, attribute, and address of a null
; terminated string as parameters
printstr: 
    push bp
    mov bp, sp
    push es
    push ax
    push cx
    push si
    push di
    push ds
    pop es            ; load ds in es
    mov di, [bp+4]    ; point di to string
    mov cx, 0xffff    ; load maximum number in cx
    xor al, al        ; load a zero in al
    repne scasb       ; find zero in the string
    mov ax, 0xffff    ; load maximum number in ax
    sub ax, cx        ; find change in cx
    dec ax            ; exclude null from length
    jz exit           ; no printing if string is empty
    mov cx, ax        ; load string length in cx
    mov ax, 0xb800
    mov es, ax        ; point es to video base
    mov al, 80        ; load al with columns per row
    mul byte [bp+8]   ; multiply with y position
    add ax, [bp+10]   ; add x position
    shl ax, 1         ; turn into byte offset
    mov di, ax        ; point di to required location
    mov si, [bp+4]    ; point si to string
    mov ah, [bp+6]    ; load attribute in ah
    cld               ; auto increment mode
nextchar: 
    lodsb             ; load next char in al
    stosw             ; print char/attribute pair
    loop nextchar     ; repeat for the whole string
exit: 
    pop di
    pop si
    pop cx
    pop ax
    pop es
    pop bp
    ret 8

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
    call printstr     ; call the printstr subroutine
    mov ax, 0x4c00    ; terminate program
    int 0x21          ; interrupt to DOS
```

## LES and LDS Instructions
`LES` loads `ES` register and `LDS` loads `DS` register into other registers from memory addresses.

```asm
ldi si, [bp + 4]
```

This snippet will load `SI` from `[bp + 4]` and `DS` from `[bp + 6]`.  
This is according to the fact that the `segment value` should be pushed on the #stack _first_ and `offset value` should be pushed on the #stack later.

# LES and LDS Example

```asm
[org 0x0100]
jmp start

message: 
    db 'hello world', 0 ; null terminated string

; subroutine to calculate the length of a string
; takes the segment and offset of a string as parameters
strlen: 
    push bp
    mov bp, sp
    push es
    push cx
    push di
    les di, [bp+4]    ; point es:di to string
    mov cx, 0xffff    ; load maximum number in cx
    xor al, al        ; load a zero in al
    repne scasb       ; find zero in the string
    mov ax, 0xffff    ; load maximum number in ax
    sub ax, cx        ; find change in cx
    dec ax            ; exclude null from length
    pop di
    pop cx
    pop es
    pop bp
    ret 4

; subroutine to print a string
; takes the x position, y position, attribute, and address of a null
; terminated string as parameters
printstr: 
    push bp
    mov bp, sp
    push es
    push ax
    push cx
    push si
    push di
    push ds           ; push segment of string
    mov ax, [bp+4]
    push ax           ; push offset of string
    call strlen       ; calculate string length 
    cmp ax, 0         ; is the string empty
    jz exit           ; no printing if string is empty
    mov cx, ax        ; save length in cx
    mov ax, 0xb800
    mov es, ax        ; point es to video base
    mov al, 80        ; load al with columns per row
    mul byte [bp+8]   ; multiply with y position
    add ax, [bp+10]   ; add x position
    shl ax, 1         ; turn into byte offset
    mov di, ax        ; point di to required location
    mov si, [bp+4]    ; point si to string
    mov ah, [bp+6]    ; load attribute in ah
    cld               ; auto increment mode
nextchar: 
    lodsb             ; load next char in al
    stosw             ; print char/attribute pair
    loop nextchar     ; repeat for the whole string
exit: 
    pop di
    pop si
    pop cx
    pop ax
    pop es
    pop bp
    ret 8

start: 
    call clrscr       ; call the clrscr subroutine
    mov ax, 30
    push ax           ; push x position
    mov ax, 20
    push ax           ; push y position
    mov ax, 0x71      ; blue on white attribute
    push ax           ; push attribute
    mov ax, message
    push ax           ; push address of message
    call printstr     ; call the printstr subroutine
    mov ax, 0x4c00    ; terminate program
    int 0x21          ; interrupt to DOS
```

# MOVS Example - Screen Scrolling

```asm
[org 0x0100]
jmp start

; subroutine to scroll up the screen
; takes the number of lines to scroll as parameter
scrollup: 
    push bp
    mov bp, sp
    push ax
    push cx
    push si
    push di
    push es
    push ds

    mov ax, 80         ; load chars per row in ax
    mul byte [bp+4]    ; calculate source position
    mov si, ax         ; load source position in si
    push si            ; save position for later use
    shl si, 1          ; convert to byte offset
    mov cx, 2000       ; number of screen locations
    sub cx, ax         ; count of words to move
    mov ax, 0xb800
    mov es, ax         ; point es to video base
    mov ds, ax         ; point ds to video base
    xor di, di         ; point di to top left column
    cld                ; set auto increment mode
    rep movsw          ; scroll up
    mov ax, 0x0720     ; space in normal attribute
    pop cx             ; count of positions to clear
    rep stosw          ; clear the scrolled space

    pop ds
    pop es
    pop di
    pop si
    pop cx
    pop ax
    pop bp
    ret 2

start: 
    mov ax, 5
    push ax            ; push number of lines to scroll
    call scrollup      ; call the scroll up subroutine
    mov ax, 0x4c00     ; terminate program
    int 0x21           ; interrupt to DOS
```

# CMPS Example - String Comparison

```asm
[org 0x0100]
jmp start

msg1: db 'hello world', 0
msg2: db 'hello WORLD', 0
msg3: db 'hello world', 0

; subroutine to compare two strings
; takes segment and offset pairs of two strings to compare
; returns 1 in ax if they match and 0 otherwise
strcmp: 
    push bp
    mov bp, sp
    push cx
    push si
    push di
    push es
    push ds

    lds si, [bp+4]    ; point ds:si to first string
    les di, [bp+8]    ; point es:di to second string

    push ds           ; push segment of first string
    push si           ; push offset of first string
    call strlen       ; calculate string length
    mov cx, ax        ; save length in cx

    push es           ; push segment of second string
    push di           ; push offset of second string
    call strlen       ; calculate string length
    cmp cx, ax        ; compare length of both strings
    jne exitfalse     ; return 0 if they are unequal

    mov ax, 1         ; store 1 in ax to be returned
    repe cmpsb       ; compare both strings
    jcxz exitsimple   ; are they successfully compared

exitfalse: 
    mov ax, 0         ; store 0 to mark unequal

exitsimple: 
    pop ds
    pop es
    pop di
    pop si
    pop cx
    pop bp
    ret 8

start: 
    push ds           ; push segment of first string
    mov ax, msg1
    push ax           ; push offset of first string
    push ds           ; push segment of second string
    mov ax, msg2
    push ax           ; push offset of second string
    call strcmp       ; call strcmp subroutine

    push ds           ; push segment of first string
    mov ax, msg1
    push ax           ; push offset of first string
    push ds           ; push segment of third string
    mov ax, msg3
    push ax           ; push offset of third string
    call strcmp       ; call strcmp subroutine

    mov ax, 0x4c00    ; terminate program
    int 0x21          ; interrupt to DOS
```

# Exercises
