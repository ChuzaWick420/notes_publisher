---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Program Flow
![[Pasted image 20240803221357.png]]

## CALL and RET
The `call` takes a `label` as `operand` just like `jmp` does.  
the `ret` takes no `operands` and returns the execution back to the statement followed by the `call` statement.

# Our First Subroutine

```asm
[org 0x0100]
jmp start

data: 
    dw 60, 55, 45, 50, 40, 35, 25, 30, 10, 0

swap: 
    db 0

bubblesort: 
    dec cx             ; last element not compared
    shl cx, 1          ; turn into byte count

mainloop: 
    mov si, 0          ; initialize array index to zero
    mov byte [swap], 0 ; reset swap flag to no swaps 

innerloop: 
    mov ax, [bx+si]    ; load number in ax
    cmp ax, [bx+si+2]  ; compare with next number
    jbe noswap         ; no swap if already in order

    mov dx, [bx+si+2]  ; load second element in dx
    mov [bx+si], dx    ; store first number in second
    mov [bx+si+2], ax  ; store second number in first
    mov byte [swap], 1 ; flag that a swap has been done

noswap: 
    add si, 2          ; advance si to next index
    cmp si, cx         ; are we at last index
    jne innerloop      ; if not compare next two

    cmp byte [swap], 1 ; check if a swap has been done
    je mainloop        ; if yes make another pass
    ret                ; go back to where we came from

start: 
    mov bx, data       ; send start of array in bx
    mov cx, 10         ; send count of elements in cx
    call bubblesort    ; call our subroutine
    mov ax, 0x4c00     ; terminate program
    int 0x21           ; interrupt to DOS

```

When the `call` instruction is encountered, the `0150` is stored inside #stack-pointer.  
This `0150` is composite of `0100` from the beginning of file and `0050` offset which is the address of statement next to `call` statement.

# Stack
The `8088` architecture uses a `decrementing stack` which means that as the elements are pushed on the stack, the stack decrements by `2` (a `word`), decreasing the address.  
For an `incrementing stack`, the case is opposite.  
We cannot push or pop `1 byte`.

There is another type of `RET` that is `ret n` where `n` represents the number that needs to be added to the #stack-pointer along with the default `2`.

```asm
[org 0x0100]
jmp start

data: 
    dw 60, 55, 45, 50, 40, 35, 25, 30, 10, 0

data2: 
    dw 328, 329, 898, 8923, 8293, 2345, 10, 877, 355, 98
    dw 888, 533, 2000, 1020, 30, 200, 761, 167, 90, 5

swapflag: 
    db 0

swap: 
    mov ax, [bx+si]      ; load first number in ax
    xchg ax, [bx+si+2]   ; exchange with second number
    mov [bx+si], ax      ; store second number in first
    ret                  ; go back to where we came from

bubblesort: 
    dec cx               ; last element not compared
    shl cx, 1            ; turn into byte count

mainloop: 
    mov si, 0            ; initialize array index to zero
    mov byte [swapflag], 0 ; reset swap flag to no swaps

innerloop: 
    mov ax, [bx+si]      ; load number in ax
    cmp ax, [bx+si+2]    ; compare with next number
    jbe noswap           ; no swap if already in order
    call swap            ; swaps two elements
    mov byte [swapflag], 1 ; flag that a swap has been done

noswap: 
    add si, 2            ; advance si to next index
    cmp si, cx           ; are we at last index
    jne innerloop        ; if not compare next two

    cmp byte [swapflag], 1 ; check if a swap has been done
    je mainloop          ; if yes make another pass
    ret                  ; go back to where we came from

start: 
    mov bx, data         ; send start of array in bx
    mov cx, 10           ; send count of elements in cx
    call bubblesort      ; call our subroutine
    mov bx, data2        ; send start of array in bx
    mov cx, 20           ; send count of elements in cx
    call bubblesort      ; call our subroutine again
    mov ax, 0x4c00       ; terminate program
    int 0x21             ; interrupt to DOS

```

The `xchg` swaps its `operands`.

# Saving and Restoring Registers

```asm
[org 0x0100]
jmp start

data: 
    dw 60, 55, 45, 50, 40, 35, 25, 30, 10, 0

data2: 
    dw 328, 329, 898, 8923, 8293, 2345, 10, 877, 355, 98
    dw 888, 533, 2000, 1020, 30, 200, 761, 167, 90, 5

swapflag: 
    db 0

swap: 
    push ax              ; save old value of ax
    mov ax, [bx+si]      ; load first number in ax
    xchg ax, [bx+si+2]   ; exchange with second number
    mov [bx+si], ax      ; store second number in first
    pop ax               ; restore old value of ax
    ret                  ; go back to where we came from

bubblesort: 
    push ax              ; save old value of ax
    push cx              ; save old value of cx
    push si              ; save old value of si
    dec cx               ; last element not compared
    shl cx, 1            ; turn into byte count

mainloop: 
    mov si, 0            ; initialize array index to zero
    mov byte [swapflag], 0 ; reset swap flag to no swaps

innerloop: 
    mov ax, [bx+si]      ; load number in ax
    cmp ax, [bx+si+2]    ; compare with next number
    jbe noswap           ; no swap if already in order
    call swap            ; swaps two elements
    mov byte [swapflag], 1 ; flag that a swap has been done

noswap: 
    add si, 2            ; advance si to next index
    cmp si, cx           ; are we at last index
    jne innerloop        ; if not compare next two

    cmp byte [swapflag], 1 ; check if a swap has been done
    je mainloop          ; if yes make another pass
    pop si               ; restore old value of si
    pop cx               ; restore old value of cx
    pop ax               ; restore old value of ax
    ret                  ; go back to where we came from

start: 
    mov bx, data         ; send start of array in bx
    mov cx, 10           ; send count of elements in cx
    call bubblesort      ; call our subroutine
    mov bx, data2        ; send start of array in bx
    mov cx, 20           ; send count of elements in cx
    call bubblesort      ; call our subroutine again
    mov ax, 0x4c00       ; terminate program
    int 0x21             ; interrupt to DOS
```

## PUSH
It takes the `operands` value (could be #register or memory) and places it on the top of the #stack, decrementing #stack-pointer by `2`.

## POP
This does the opposite of `push`

## CALL
It pushes the #instruction-pointer onto the #stack, storing its value inside #stack-pointer.

## RET
It does the opposite, pops #stack-pointer value into #instruction-pointer

# Parameters Passing through Stack
The maximum parameters a `sub routine` can accept is `7`.  
To pass the parameters:
1. push the arguments onto the #stack 
2. the `call` pushes the #instruction-pointer onto the #stack.
3. Then we push #base-pointer onto the #stack 
4. Then we move the return address, pointed by the #stack-pointer, into the #base-pointer 
5. Then we use `[bp + 2]` to get a `word` (2nd argument) which was pushed on the #stack and `[bp + 4` for (1st argument).

## Stack Clearing by Caller or Callee
Usually, it is done by `callee` by using `ret n` since it adds `n` values beyond `2` to the #stack-pointer and the values are not popped but rather discarded.

# Local Variables
We can make `local variables` by using the #stack.

```asm
push bp
mov bp, sp
sub sp, 2
```

We create the space using the `sub` operation and then peek through the stack using #base-pointer.

# Exercises
