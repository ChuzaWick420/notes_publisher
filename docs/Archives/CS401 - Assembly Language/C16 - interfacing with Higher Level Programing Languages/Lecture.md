---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Calling Conventions
There are certain rules to be followed to call the _assembly routines_ from higher level languages like `C`.  
These rules are called _calling conventions_.

## What is a Naming Convention
`C` puts an `underscore` before the _function_ or _variable_ names meanwhile PASCAL translates all characters to upper case.  
`C++` has weird naming mangling which is compiler dependent so to avoid it, we need to use `extern "C"` directive to force `C++` to use `C` naming style.

## How Are Parameters Passed to Routines
In `PASCAL`, the _first_ argument is passed from left.  
In `C`, the _first_ argument is passed from right.

## Which Registers Must Be Preserved
Both standards preserve:
- EBX
- ESI  
- EDI
- EBP
- ESP
- DS
- ES
- SS

## Which Registers Are Used as Scratch
Both standards do not guarantee values for:
- EAX
- ECX
- EDX
- FS
- GS
- EFLAGS and other registers

## Which Registers Holds the return Value
In both standards, the `32-bit` values are returned in `EAX` and `64-bit` ones in `EDX:EAX`

## Who is Responsible for Removing the Parameters
In `C`, the `caller` removes the parameters.  
In `PASCAL`, the `callee` removes the parameters.

# Calling C From Assembly
Imagine we have a function in `C`:

```c
int divide(int dividend, int divisor);
```

To call it from assembly:

```asm
push dword [mydivisor]
push dword [mydividend]
call _divide
add esp, 8
; EAX holds the answer
```

# Calling Assembly from C
Imagine we got an assembly program

```asm
[section .text]
global _swap

_swap:
    ; Copy parameter p1 to ecx
    mov ecx, [esp + 4]

    ; Copy parameter p2 to edx
    mov edx, [esp + 8]

    ; Copy *p1 into eax
    mov eax, [ecx]

    ; Exchange eax with *p2
    xchg eax, [edx]

    ; Copy eax into *p1
    mov [ecx], eax

    ; Return from this function
    ret

```

Then we use 

```PowerShell
nasm –f win32 swap.asm
```

and get `swap.obj` file.

Then in `C`

```c
#include <stdio.h>
void swap(int* p1, int* p2);

int main() {
	int a = 10, b = 20;
	printf("a=%d b=%d\n", a, b); 
	swap(&a, &b); 
	printf("a=%d b=%d\n", a, b); 
	
	system("PAUSE");
	return 0;
}
```

# Exercises
