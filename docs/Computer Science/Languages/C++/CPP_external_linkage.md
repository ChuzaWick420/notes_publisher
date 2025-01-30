# External Linkage

The `#!cpp extern` `keyword` is used to declare that the symbol is external to current source file.

Imagine `source1.cpp`:

```cpp
int value = 100;
```

Imagine `source2.cpp`

```cpp
void foo () {
	extern int value; // (1)!
	value++;          // (2)!
}
```

1. Find the `value` variable outside of `source2.cpp`.
2. Uses the `value` variable.

These can be defined within the same source file too.

```cpp
int value = 100;

void foo () {
	// extern int value;
	value++;
}
```

The `#!cpp extern` declaration in this case becomes optional.