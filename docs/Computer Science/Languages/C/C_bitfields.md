# Bit Fields

A `bit field` is a set of `bits` aligned within a single implementation defined storage unit called a `word`.  
Everything about `bit fields` is implementation dependent.

```cpp
struct {
	unsigned int is_keyword : 0;
	unsigned int is_literal : 0;
	unsigned int is_identifier : 0;
} text;
```

This `#!cpp struct`[^1] contains 3 `bits` called `is_keyword`, `is_literal` and `is_identifier`. However, due to padding, the size of this `#!cpp struct`[^1] is still 4.

## References

[^1]: Read more about [[C_structures|struct]].