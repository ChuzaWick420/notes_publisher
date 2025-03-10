# File Access

The `stdio.h` contains a `#!cpp typedef`[^1] of a `#!cpp struct`[^2] called `#!cpp FILE`.  
The `#!cpp fopen(const char*, const char*)` `function` takes two arguments. 

1. Name of the file to be opened.
2. The mode in which file needs to be opened in.
	- `r` for read.
	- `w` for write.
	- `a` for append.

If there is any error while opening the file, `#!cpp fopen(const char*, const char*)` returns `#!cpp NULL`.  
There are two other `functions` as well.

```cpp
int getc(FILE* file_ptr); // (1)!
int putc(char c, FILE* file_ptr); // (2)!
```

1. Gets a `#!cpp char` and moves the pointer one character ahead in the buffer in which file's contents exist.
2. Writes a `#!cpp char` to the buffer containing file's contents.

There are 3 `#!cpp const` file pointers which are opened by the `Operating System` when a `C` program is ran.

- `stdin`
- `stdout`
- `stderr`

Then, `#!cpp fclose(FILE*)` is used to disconnect the program from the file.

## References

[^1]: Read more about [[C_typedef|typedef]].
[^2]: Read more about [[C_structures|structs]].