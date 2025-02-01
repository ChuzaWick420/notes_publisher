# Register

The `#!cpp register` keyword is used to specify that a certain variable is going to be used a lot frequently and should be placed in a `cpu register`.

```cpp
void foo (register int var) {
	register int test;
}
```

Both `var` and `test` are supposed to be placed in `cpu registers` but there is no surety that they will be placed in `cpu registers` or not.  
This is because the excessive use of the keyword is ignored and it is also ignored due to disallowed declarations.  
The keyword has been deprecated since `c++17`.