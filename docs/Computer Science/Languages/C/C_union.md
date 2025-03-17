# Unions

```cpp
union label {
	int x;
	char y;
};
```

It is similar to a `#!cpp struct`[^1] in spirit but difference is that, all the members share same overlapping memory.  
The size of the `#!cpp union` is determined by the size of the largest member it contains.

![[C_e_union_alignment.svg]]  
/// caption  
The `#!cpp union` shown above has size of `4 bytes`.  
///

## References

[^1]: Read more about [[C_structures|structs]].