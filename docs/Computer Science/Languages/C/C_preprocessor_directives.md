# Pre Processor Directives

## `#!cpp #include`

The `#!cpp #include "file"` looks for file, first in same directory as of the source file.  
If the file is not found there, then it is demoted to `#!cpp #include <file>` which looks for the file according to the rules defined by the implementation.

## `#!cpp #define`

This directive is used to define macros.

### Without Arguments

It is used to replace tokens by a replacement test.

```cpp
#define TOKEN replacement text
```

> [!info] Any of the following appearing in source code, won't be replaced
> - "TOKEN" (`token` appearing as a `string`[^1])
> - TOKENIZATION (`token` appear as part of some `identifier` or `keyword` etc)

The `replacement text` can be carried to multiple lines by using `\` in the end.

```cpp
#define TEST for (int i = 0; i < 5; i++) {\
	printf("hi\n");\
}

int main () {
	TEST
	return 0;
}
```

It prints

```
hi
hi
hi
hi
hi
```

### With Arguments

```cpp
#define MACRO(arg1, arg2) some replacement text using arg1 and arg2

int main () {
	MACRO(1, 2)
}
```

There are some problems with this though

```cpp
#define SQUARE1(x) x * x
#define SQUARE2(x) (x) * (x)

int main () {
	int x;
	int a = SQUARE1(5);
	int b = SQUARE1(5 + x);
	int c = SQUARE2(5 + x);
}
```

```bash
gcc -E main.c -o main.i
cat main.i
```

```cpp
int main () {
	int x;
	int a = 5 * 5;
	int b = 5 + x * 5 + x; // (1)!
	int c = (5 + x) * (5 + x);
}
```

1. Problematic!

We can also use `#` to have the replacement text wrapped around double quotes.

```cpp
#define MACRO(x) printf(#x)

int main () {
	MACRO(hello world); // (1)!
}
```

1. `#!cpp TOKEN(hello world)` will be replaced by `#!cpp printf("hello world")`.

We can use `##` to concatenate multiple arguments within the replacement text.

```cpp
#define MACRO1(x, y) x y
#define MACRO2(x, y) x ## y

int main () {
	MACRO1(1, 2) // (1)!
	MACRO2(1, 2) // (2)!
}
```

1. Gets replaced by `1 2`
2. Gets replaced by `12`

## `#!cpp #undef`

Removes the definition of a macro which was defined using `#!cpp #define`.

```cpp
#define MACRO 420
#undef MACRO

int main () {
	int x = MACRO; // (1)!
}
```

1. After being pre-processed, the `MACRO` is _not_ replaced by `420`

## `#!cpp #if`

Similar to `#!cpp if` statements.

## `#!cpp #elif`

Similar to `#!cpp else if` statements.

## `#!cpp #else`

Similar to `#!cpp else` statements.

## `#!cpp #endif`

Specifies the end of a block defined by `#!cpp #if` and `#!cpp #ifdef`.

```cpp
#if !defined(HDR) // (1)!
#define HDR

// file content
#endif
```

1. `#!cpp defined()` checks if a macro was defined or not.

## `#!cpp #ifdef`

Both `#!cpp #if defined(MACRO)` and `#!cpp #ifdef MACRO` are same.

## `#!cpp #ifndef`

Both `#!cpp #if !defined(MACRO)` and `#!cpp #ifndef MACRO` are same.

We can combine all these to conditionally include files too.

```cpp
#if SYSTEM == SYSV
	#define HDR "sysv.h"
#elif SYSTEM == BSD
	#define HDR "bsd.h"
#elif SYSTEM == MSDOS
	#define HDR "msdos.h"
#else
	#define HDR "default.h"

#include HDR // (1)!
```

1. The `HDR` symbol contains the appropriate file as replacement text according to what the `SYSTEM` symbol contains and then it is included.

## References

[^1]: Read more about [[C_string_literals|strings]].