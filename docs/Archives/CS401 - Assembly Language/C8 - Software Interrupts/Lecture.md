---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Interrupts
The `async` ones are outside the processor meanwhile the `sync` ones happen side by side with some activity within the processor.  
There are 2 types of interrupts.
1. Software
2. Hardware

the instruction used for interruption is `INT` and the routines which are triggered in response to this are called `interrupt service routines` (ISR) or `interrupt handler`.  
The `INT` instruction takes `byte` argument ranging from `0` to `255`.

`INT 0` is `divide by zero` interrupt.

The correlation between `interrupt number` and `interrupt handler` uses a table called `interrupt vector table`.  
Each entry in this table is `4 bytes` long consisting of `segment` and `offset` values with `offset` being the first `2 bytes` (`little endian`).  
The whole entry is called a `vector`.

The `IRET` instruction is used to return to the caller.

The operations done by `int` are following:
- `sp` <- `sp` - 2
- `[sp]` <- flag
- `sp` <- `sp` - 2
- `IF` <- 0
- `TF` <- 0
- `[SP]` <- CS
- `sp` <- `sp` - 2
- `[sp]` <- `IP`
- `IP` <- `[0:N * 4]`
- `CS` <- `[0:N * 4 + 2]`

The operations performed by `INT` are following
- `IP` <- `[SP]`
- `SP` <- `SP + 2`
- `CS` <- `[SP]`
- `SP` <- `SP` + 2
- flag <- `[SP]`
- `SP` <- `SP` + 2

The starting `256 * 4 bytes = KB` space is reserved for `Instruction Vector Table` (IVT).

- `INT 0` - Divide by zero
- `INT 1` - Trap, single step interrupt
- `INT 2` - Non Maskable interrupt
- `INT 3` - Debug interrupt
- `INT 4` - Arithmetic Overflow, change of sign bits

# Hooking an Interrupt

```asm
; Hooking divide by zero interrupt
[org 0x0100]
jmp start

message: db 'You divided something by zero.', 0

;;;;; COPY LINES 028-050 FROM EXAMPLE 7.4 (strlen) ;;;;;
;;;;; COPY LINES 005-024 FROM EXAMPLE 7.1 (clrscr) ;;;;;
;;;;; COPY LINES 050-090 FROM EXAMPLE 7.4 (printstr) ;;;;;

; Divide by zero interrupt handler
myisrfor0: 
    push ax ; Push all regs
    push bx
    push cx
    push dx
    push si
    push di
    push bp
    push ds
    push es

    push cs
    pop ds ; Point ds to our data segment

    call clrscr ; Clear the screen

    mov ax, 30
    push ax ; Push x position

    mov ax, 20
    push ax ; Push y position

    mov ax, 0x71 ; White on blue attribute
    push ax ; Push attribute

    mov ax, message
    push ax ; Push offset of message

    call printstr ; Print message

    pop es
    pop ds
    pop bp
    pop di
    pop si
    pop dx
    pop cx
    pop bx
    pop ax

    iret ; Return from interrupt

; Subroutine to generate a divide by zero interrupt
genint0: 
    mov ax, 0x8432 ; Load a big number in ax
    mov bl, 2 ; Use a very small divisor
    div bl ; Interrupt 0 will be generated
    ret

start: 
    xor ax, ax
    mov es, ax ; Load zero in es
    mov word [es:0*4], myisrfor0 ; Store offset at n*4
    mov [es:0*4+2], cs ; Store segment at n*4+2

    call genint0 ; Generate interrupt 0

    mov ax, 0x4c00 ; Terminate program
    int 0x21
```

# BIOS and DOS Interrupts
A software that is burnt into the `ROM` is called `firmware`.  
The interface to the hardware is called `BIOS` (Basic Input Output services)  
`BootStrap` means to load the `OS`.

The video services are accessible through `INT 10`.  
The keyboard services are accessible through `INT 16`.  
The parallel ports through `INT 17`.  
The `DOS` services are available through `INT 21`.

There can be different services related to video.  
To access each individual service, we do something like `INT 10 Service 1` etc.  
And these service number are usually given in `AH` register.  
The sub service numbers are stored in `AL` or `BL` registers.

```asm
; Print string using BIOS service
[org 0x0100]
jmp start

message: db 'Hello World'

start:
    mov ah, 0x13      ; Service 13 - print string
    mov al, 1         ; Subservice 01 – update cursor
    mov bh, 0         ; Output on page 0
    mov bl, 7         ; Normal attribute
    mov dx, 0x0A03    ; Row 10, column 3
    mov cx, 11        ; Length of string

    push cs
    pop es            ; Segment of string

    mov bp, message   ; Offset of string
    int 0x10          ; Call BIOS video service

    mov ax, 0x4c00    ; Terminate program
    int 0x21
```
