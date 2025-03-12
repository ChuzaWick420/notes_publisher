# Unix Interface

`UNIX` provides `functions` which can be used by the program. These functions are defined in `#!cpp "syscalls.h"`.

## File System

In a file system, even the peripheral devices are treated as files. This allows handling of different resources, either peripherals or files through a homogeneous interface.

## File Descriptors

If a program wants access to a file then it has to let the `operating system` know about the intent. This could be in the form of either

- Writing to a file
- Reading from a file

etc

When the file is opened, it returns a non zero integer called the `file descriptor`. Whenever an input or output operation on this file needs to be done, it will be done using the `file descriptor`.  
When the `shell` runs the program, it opens three `file descriptors`.

- `0` - `stdin`
- `1` - `stdout`
- `2` - `stderr`

By default, `stdin` is associated with the keyboard and `stdout` is associated with screen usually.  
The direction of `stdin` can be redirected using `<` and `stdout` can be redirected using `>`.

```ps
program1 < input_file // (1)!
program2 > output_file // (2)!
```

Assume `program1` takes input from the `keyboard`, using `<`, the input is now taken from the `input_file` instead.  
Similarly, assume `program2` outputs characters to the `screen`. Using `>`, we are making sure that it outputs the characters to a `output_file` instead.

## `#!cpp read()` And `#!cpp write()`

```cpp
read(int file_descriptor, char* buffer, int size);
write(int file_descriptor, char* buffer, int size);
```

## `#!cpp open()`

```cpp
int open(char* file_name, int flags, int perms); // returns a file descriptor
```

The `flags` determine how the file should be opened.

- `O_RDONLY` for reading files
- `O_WROLY` for writing files
- `O_RDWR` for both writing and reading files

These constants are defined in

- `#!cpp <fcntl.h>` on `System V UNIX` systems.
- `#!cpp <sys/file.h>` on `Berkeley (BSD)` versions.

The `perms` is always `#!cpp 0` for `#!cpp open()`.

## `#!cpp creat()`

```cpp
int creat(char* name, int perms); // (1)!
```

1. Returns a [file descriptor](#file-descriptor) if it was able to create a file. Otherwise, it returns `#!cpp -1`.

If the file already exists, the previous contents are discarded.  
In `UNIX`, there are `9 bits` of permission information associated with the files. These are usually passed in `octal notation`.

## `#!cpp close()`

```cpp
close(int file_descriptor); // disconnects the file from the program
```

## `#!cpp unlink()`

```cpp
unlink(char* file_name); // (1)!
```

1. It removes the filename from the `file system`. Equivalent to the library `function` `#!cpp remove()`. 

## Random Access

```cpp
long lseek(int file_descriptor, long offset, int origin); // (1)!
```

1. Sets the position for `#!cpp read()` and `#!cpp write()` relative to `origin`.
