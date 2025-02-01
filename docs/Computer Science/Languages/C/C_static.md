# Static

The `#!cpp static` keyword is used for following

## Hiding a Global Variable within a File Scope

```c
extern int var; // (1)!

int main () {
	printf("%d", var);
}
```

/// caption  
main.c  
///

1. `#!cpp extern`[^1] ensures that `#!cpp printf` uses `var` defined inside some _other_ source file.

```c
static int var = 6; // (1)!
```

/// caption  
definition.c  
///

1. `#!cpp static` ensures that the `var` variable is only accessible inside `definition.c`. If `#!cpp static` is removed, we will not get a linker error while trying to compile.

Attempting to compile will cause a linker error.

```bash
gcc main.c definition.c -o main.exe
```

```
main.c:(.rdata$.refptr.var[.refptr.var]+0x0): undefined reference to `var'
collect2.exe: error: ld returned 1 exit status
```

## `#!cpp Static` Variables within `Functions`[^2]

```cpp
void foo () {
	static int var = 420;
	var++;
	printf("%d", var);
}

int main () {
	foo(); // (1)!
	foo(); // (2)!
}
```

1. Since the declaration is encountered first time, `var` is created with value `420`, incremented to `421` and used. After the `function`[^2] returns though, the `var` remains alive within memory.
2. Next time when `#!cpp foo()` is called, the declaration of `var` is skipped and the value `421`(from previous call to `#!cpp foo()`) is incremented to `422`.

## References

[^1]: Read more about [[CPP_external_linkage|extern]].
[^2]: Read more about [[M_Function|functions]].