---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Hardware Interrupts
Programmable interrupt controller (PIC) is a device which interfaces between the `INT` pin of `CPU` and the interrupt signals generated by the devices.  
It has `8` input and `1` output signals.  
These `8` inputs are called `Interrupt Requests` (IRQ)

- `IRQ 0` is for Timer devices
- `IRQ 1` is for Keyboards
- `IRQ 2` is for cascading interrupts
- `IRQ 3` is connected to serial port `COM 2`
- `IRQ 4` is connected to serial port `COM 1`
- `IRQ 5` is used for sound cards, network cards or modems
- `IRQ 6` is used for floppy disks
- `IRQ 7` is used for parallel ports

The `IRQ 0` is mapped to `INT 8` and linearly `IRQ 7` is mapped to `INT F`

The `I/O` ports of the `interrupt handler` send a signal called `End of Interrupt` (EOI) to the `PIC`.

# I/O Ports
CPU can either do _read_ or _write_.  
There is a special pin on the intel's control bus which determines if the instruction is from memory space or peripherical space.

## IN and OUT Instructions
Both of these have a `byte` form and a `word` form.  
The _source_ register for `OUT` and _destination_ register for `IN` is `AL` or `AX` depending on which form was used.

The port number `20` is for PIC `60` to `64` for keyboards  
The port number `21` is for PIC `378` for parallel ports.

```asm
in al, 0x21
mov dx, 0x378
in al, dx
out 0x21, al
mov dx, 0x378
out dx, al
```

## PIC Ports
The port `20` is for control port  
The port `21` is for enabling or disabling interrupts.  
Each bit on port `21` corresponds to `IRQ` lines.

```asm
; Disable keyboard interrupt in PIC mask register
[org 0x0100]

in al, 0x21      ; Read interrupt mask register
or al, 2         ; Set bit for IRQ2
out 0x21, al     ; Write back mask register

mov ax, 0x4c00   ; Terminate program
int 0x21

```

## Keyboard Controller
Each key on the keyboard corresponds to a `scan code` which tells the CPU which key has been pressed.  
The `scan code` is 1 `byte` long with _first_ bit indicating the status of the `key` and remaining `bits` indicating the `key` itself.  
If it is set to `0` then it means the key is pressed.  
If it is set to `1` then it means the key is released.

```asm
; Differentiate left and right shift keys with scancodes
[org 0x0100]
jmp start

; Keyboard interrupt service routine
kbisr: 
    push ax
    push es

    mov ax, 0xb800
    mov es, ax        ; Point es to video memory

    in al, 0x60       ; Read a char from keyboard port

    cmp al, 0x2a      ; Is the key left shift?
    jne nextcmp       ; No, try next comparison

    mov byte [es:0], 'L' ; Yes, print L at top left
    jmp nomatch       ; Leave interrupt routine

nextcmp: 
    cmp al, 0x36      ; Is the key right shift?
    jne nomatch       ; No, leave interrupt routine

    mov byte [es:0], 'R' ; Yes, print R at top left

nomatch: 
    mov al, 0x20
    out 0x20, al      ; Send EOI to PIC

    pop es
    pop ax
    iret 

start: 
    xor ax, ax
    mov es, ax        ; Point es to IVT base

    cli               ; Disable interrupts
    mov word [es:9*4], kbisr ; Store offset at n*4
    mov [es:9*4+2], cs       ; Store segment at n*4+2
    sti               ; Enable interrupts
```

## Interrupt Chaining

```asm
; Another attempt to terminate program with Esc that hooks
; keyboard interrupt
[org 0x100]
jmp start

oldisr: dd 0 ; Space for saving old ISR

; Keyboard interrupt service routine
kbisr: 
    push ax
    push es

    mov ax, 0xb800
    mov es, ax        ; Point es to video memory

    in al, 0x60       ; Read a char from keyboard port

    cmp al, 0x2a      ; Is the key left shift?
    jne nextcmp       ; No, try next comparison

    mov byte [es:0], 'L' ; Yes, print L at top left
    jmp nomatch       ; Leave interrupt routine

nextcmp: 
    cmp al, 0x36      ; Is the key right shift?
    jne nomatch       ; No, leave interrupt routine

    mov byte [es:0], 'R' ; Yes, print R at top left

nomatch: 
    ; mov al, 0x20
    ; out 0x20, al
    pop es
    pop ax

    jmp far [cs:oldisr] ; Call the original ISR
    ; iret

start: 
    xor ax, ax
    mov es, ax         ; Point es to IVT base

    mov ax, [es:9*4]
    mov [oldisr], ax   ; Save offset of old routine

    mov ax, [es:9*4+2]
    mov [oldisr+2], ax ; Save segment of old routine

    cli                ; Disable interrupts
    mov word [es:9*4], kbisr ; Store offset at n*4
    mov [es:9*4+2], cs       ; Store segment at n*4+2
    sti                ; Enable interrupts

l1: 
    mov ah, 0          ; Service 0 – get keystroke
    int 0x16           ; Call BIOS keyboard service

    cmp al, 27         ; Is the Esc key pressed?
    jne l1             ; If no, check for next key

    mov ax, 0x4c00     ; Terminate program
    int 0x21

```

## Unhooking Interrupt

```asm
; Terminate program with Esc that hooks keyboard interrupt
[org 0x100]
jmp start

oldisr: dd 0 ; Space for saving old ISR

;;;;; COPY LINES 005-029 FROM EXAMPLE 9.4 (kbisr) ;;;;;

start: 
    xor ax, ax
    mov es, ax        ; Point es to IVT base

    mov ax, [es:9*4]
    mov [oldisr], ax  ; Save offset of old routine

    mov ax, [es:9*4+2]
    mov [oldisr+2], ax ; Save segment of old routine

    cli               ; Disable interrupts
    mov word [es:9*4], kbisr ; Store offset at n*4
    mov [es:9*4+2], cs       ; Store segment at n*4+2
    sti               ; Enable interrupts

l1: 
    mov ah, 0         ; Service 0 – get keystroke
    int 0x16          ; Call BIOS keyboard service

    cmp al, 27        ; Is the Esc key pressed?
    jne l1            ; If no, check for next key

    mov ax, [oldisr]  ; Read old offset in ax
    mov bx, [oldisr+2] ; Read old segment in bx

    cli               ; Disable interrupts
    mov [es:9*4], ax  ; Restore old offset from ax
    mov [es:9*4+2], bx ; Restore old segment from bx
    sti               ; Enable interrupts

    mov ax, 0x4c00    ; Terminate program
    int 0x21
```

# Terminate and Stay Resident
![[Pasted image 20240804052425.png]]

The number of `paragraphs` is given in `DX` register and since of each is `16-bits`

```asm
mem /c
```

# Programmable Interval Timer
The frequency of this chip is `1.19318 MHz`  
Inside the chip, there is a `16-bit` divisor which divides this frequency and connects the result to `IQR 0`.  
The default is:  

$$\frac{1193180}{65536} = \frac{18.2 times}{second}$$

This is called `Timer Tick`.

```asm
; Display a tick count on the top right of screen
[org 0x0100]
jmp start

tickcount: dw 0

; Subroutine to print a number at top left of screen
; Takes the number to be printed as its parameter
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
    mov es, ax         ; Point es to video base

    mov ax, [bp+4]     ; Load number in ax
    mov bx, 10         ; Use base 10 for division
    mov cx, 0          ; Initialize count of digits

nextdigit: 
    mov dx, 0          ; Zero upper half of dividend
    div bx             ; Divide by 10
    add dl, 0x30       ; Convert digit into ASCII value
    push dx            ; Save ASCII value on stack
    inc cx             ; Increment count of values
    cmp ax, 0          ; Is the quotient zero?
    jnz nextdigit      ; If no, divide it again

    mov di, 140        ; Point di to 70th column

nextpos: 
    pop dx             ; Remove a digit from the stack
    mov dh, 0x07       ; Use normal attribute
    mov [es:di], dx    ; Print char on screen
    add di, 2          ; Move to next screen location
    loop nextpos       ; Repeat for all digits on stack

    pop di
    pop dx
    pop cx
    pop bx
    pop ax 
    pop es
    pop bp
    ret 2

; Timer interrupt service routine
timer: 
    push ax
    inc word [cs:tickcount] ; Increment tick count
    push word [cs:tickcount]
    call printnum            ; Print tick count
    mov al, 0x20
    out 0x20, al             ; End of interrupt
    pop ax
    iret                     ; Return from interrupt

start: 
    xor ax, ax
    mov es, ax               ; Point es to IVT base
    cli                      ; Disable interrupts
    mov word [es:8*4], timer ; Store offset at n*4
    mov [es:8*4+2], cs       ; Store segment at n*4+2
    sti                      ; Enable interrupts

    mov dx, start            ; End of resident portion
    add dx, 15               ; Round up to next para
    mov cl, 4
    shr dx, cl               ; Number of paras
    mov ax, 0x3100           ; Terminate and stay resident
    int 0x21
```

# Parallel Port
The parallel port connector is a `25 pin` connector called `DB-25`  
- Pin `2` to `9` takes data from processor to the device.
- Pin 10, the ACK pin used by printers shows willingness that it is ready to accept for data.
- Pin `18` to `25` are ground

```asm
; Show scancode on external LEDs connected through parallel port
[org 0x0100]
jmp start

oldisr: dd 0 ; Space for saving old ISR

; Keyboard interrupt service routine
kbisr: 
    push ax
    push dx

    in al, 0x60       ; Read char from keyboard port
    mov dx, 0x378
    out dx, al        ; Write char to parallel port

    pop ax
    pop dx

    jmp far [cs:oldisr] ; Call original ISR

start: 
    xor ax, ax
    mov es, ax        ; Point es to IVT base

    mov ax, [es:9*4]
    mov [oldisr], ax  ; Save offset of old routine

    mov ax, [es:9*4+2]
    mov [oldisr+2], ax ; Save segment of old routine

    cli               ; Disable interrupts
    mov word [es:9*4], kbisr ; Store offset at n*4
    mov [es:9*4+2], cs       ; Store segment at n*4+2
    sti               ; Enable interrupts

    mov dx, start     ; End of resident portion
    add dx, 15        ; Round up to next para
    mov cl, 4
    shr dx, cl        ; Number of paras

    mov ax, 0x3100    ; Terminate and stay resident
    int 0x21
```

This program prints `scancode` of keystrokes on the connected LED circuit.