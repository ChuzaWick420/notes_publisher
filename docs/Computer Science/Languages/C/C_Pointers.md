# Pointers

`Pointers` are special variables which hold addresses to `objects` and `variables`.

```cpp
int x = 69;
int y = 420;

int* ptr1 = &x; // (1)!
int *ptr2 = &y; // (2)!

int* temp = NULL; // (3)!

printf("x: %d", *ptr1); // (4)!
printf("y: %d", *ptr2);

// swap the addresses
temp = ptr1;
ptr1 = ptr2;
ptr2 = temp;

printf("y: %d", *ptr1); // (5)!
printf("x: %d", *ptr2); // (6)!
```

1. Both `#!cpp int* ptr1` and `#!cpp int *ptr1` are valid ways to declare [pointers](#pointers).
2. `&` followed by an `object` or a `variable` returns the memory address for it.
3. `#!cpp NULL` is a `macro`[^1] which is defined using the `#!cpp #define` `preprocessor directive`[^1] as a [void pointer](#void-pointer) (`#!cpp #define NULL (void*)0`).
4. `#!cpp *ptr1` means _go to the memory location, stored inside `ptr1`_. This processing of accessing the memory location is called `dereferencing` or `indirection`.
5. `ptr1` was pointing to `x` before, now it points to `y`.
6. `ptr2` was pointing to `y` before, now it points to `x`.

## Void Pointer

There is another type of `pointer` called the `void pointer` (`#!cpp void*`) which is not supposed to be accessed. Trying to doing so will result into a compilation error.

## Pointer Arithmetic

```cpp
int x = 420;
int* ptr = &x; // (1)!
ptr++; // (2)!
ptr--; // (3)!
ptr = ptr + 1; // (2)!
ptr = ptr - 1; // (3)!
```

1. Points `ptr` to `x`.
2. Increments `ptr` by adding `4 bytes` to it (the offset decided by its type which is `#!cpp int` in this case).
3. decrements `ptr` by subtracting `4 bytes` to it (the offset decided by its type which is `#!cpp int` in this case).

## Pointers and Arrays

```cpp
int arr[] = {1, 2, 3, 4}; // (1)!
int *ptr = arr; //(2)!
ptr = ptr + 2; // (3)!
printf("%d\n", ptr[1]); // (4)!
printf("%d\n", ptr[-1]); // (5)!
```

1. `arr` in itself is just a memory address, it is not a variable.
2. `ptr` is assigned the value `arr` which is the start of the memory block represented by the `array` `arr`.
3. Move 2 offsets and points to `3`.
4. `#!cpp ptr[1]` is same as `#!cpp *(ptr + 1)`.
5. `#!cpp ptr[-1]` is same as `#!cpp *(ptr - 1)`. You can have negative indices for the subscript for [pointers](#pointers) but not for the `array` `arr`.

## References

1. Read more about [[C_preprocessor_directives|macros]].