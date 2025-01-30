# String Literals

When we write a `string literal`, an `array` of `characters` is initialized with `\0` appended at the end.

```cpp
void foo (const char* character) {
    char c;
    int index = 0;
    while (
        (
            c = ( // (1)!
	            * ( // (2)!
		            character // (3)!
		            + sizeof(char) // (4)!
		            * index  // (5)!
				)
            )
        )
        != '\0' // (6)!
    ) {
        std::cout << c;
        index++;
    }
    std::cout << std::endl;
}

int main () {
    foo("hi"); // (7)!
    return 0;
}
```

1. Assignment expression evaluates to `rvalue`.
2. `Dereferencing` the `pointer` to access the `character` stored at the memory location.
3. The `#!cpp const char*` `pointer` acting as a reference point.
4. The size of the offset in `bytes` (for `pointer arithmetic`).
5. An indexed multiplier to iteratively increase the total offset (the `character` to read) relative to the reference point(the `pointer`).
6. Condition to exit the loop, that the `character` indicates end of a `string`.
7. `#!cpp "hi"` results into an `array` of `characters`(h, i, `\0`) initialized in memory.
