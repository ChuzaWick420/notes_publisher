# Lambda Expressions

`Lambda Expressions` are `closure`, encapsulating a small number of statements, passed to a `function`.

## Structure

```cpp
[] () mutable throw () -> int {
	// body
}
```

- `[]` is `capture clause` or `lambda introducer`, it is used to determine if the expression accesses outside `variables` by `value` or by `reference`.
- `()` is `parameter list` or `lambda declarator`.

> [!note] Optional and mandatory parts  
> Only `capture clause` and `body` are mandatory, rest are optional.

## Capture Clause

A `capture clause` introduces new variables inside the [body](#body) from the outside `scope`.

### Empty

Specifies that the [body](#body) accesses no `variables` from outside `scope`.

```cpp
[] {

}
```

### Value

Specifies that the `variables` being accessed are accessed by `value`.

```cpp
[x] {
	// x is accessed by value
	int local_var_to_lambda = x;
}
```

### Reference

Specifies that the `variables` being accessed are accessed by `reference`.

```cpp
[&x] {
	// x is accessed by reference
	x = 420;
}
```

### Default

We can specify a default behavior for identifiers inside the `capture clause`.  

```cpp
[=] {
	// all variables are accessed by value
}
```

```cpp
[&] {
	// all variables are accessed by reference
}
```

We can specify the exceptions for certain variables as well

```cpp
[&, x] {
	// Access all variables by reference
	// but x by value
}
```

```cpp
[=, &x] {
	// Access all variables by value
	// but x by reference
}
```

## Parameter List

Similar to parameter list for `functions`.

## Mutable Specification

Enables to modify `variables` that were captured by `value`.

## Exception Specification

We can optionally specify `#!cpp noexcept` if the expressions throws no `exception`.

```cpp
[] noexcept {

}
```

## Return Type

## Body

Similar to `function` body.

## Example

```{.cpp .copy .annotate}
#include <iostream>

void foo (float a) {
    std::cout << "Foo: " << a << std::endl;
}

int main () {
    int x = 65;
    int y = 2;

    foo(                                    // (1)!
        [&, y]                              // (2)!
        (float i)                           // (3)!
        -> int {                            // (4)!
            x++;                            // (5)!

            float value = x + y + i + 1;    // (6)!
            return value;
        }
        (0.4)                               // (7)!
    );

    std::cout << "x: " << x << std::endl;   // (8)!
    std::cout << "y: " << y << std::endl;   // (9)!
}
```

1. Calls `foo()`.
2. Captures all `variables` by reference except for `y`.
3. Takes a `float` parameter.
4. Converts the `return value` to `int`.
5. Increments `x` which was accessed by reference.
6. Compute a `float` value.
7. Invokes the expression with `0.4` as input.
8. Prints `x` to check value.
9. Prints `y` to check value.

## References

- [Lambda Expressions - Microsoft Learn](https://learn.microsoft.com/en-us/cpp/cpp/lambda-expressions-in-cpp?view=msvc-170).