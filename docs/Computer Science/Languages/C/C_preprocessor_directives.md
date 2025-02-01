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

/// caption  
main.c  
///

```bash
gcc -E main.c -o main.i
cat main.i
```

```
int main () {
	int x;
	int a = 5 * 5;
	int b = 5 + x * 5 + x; // (1)!
	int c = (5 + x) * (5 + x);
}
```

1. Problematic!

## References

[^1]: Read more about [[C_string_literals|strings]].