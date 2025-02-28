# Typedef

`#!cpp typedef` is used to define types.

```cpp
typedef struct {
	int r;
	int g;
	int b;
} Color; // (1)!

typedef int Number; // (2)!
```

1. Uses a `#!cpp struct`[^1] to define `Color`.
2. Uses an `#!cpp int` to define `Number`.

## References

1. Read more about [[C_structures|structs]].