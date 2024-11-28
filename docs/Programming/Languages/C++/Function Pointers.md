# Function Pointers

A `pointer` to a `function` can be used to:

- Invoke the `function` it is pointing to.
- Pass the `function` it is pointing to, to another `function` as a parameter.

> [!info] Getting Address  
> To return address of `foo()`, we can use either `foo` or `&foo`.  
> Both are valid.

> [!info] Calling `foo()`  
> Assuming `ptr` points to `foo()`, we can invoke `foo()` by
> 
> - `ptr()`
> - `(*ptr)()`  
> 
> Both are valid.

```cpp
void foo () {
	std::cout << "Hello World!" << std::endl;
}

int main () {
	// &foo or foo, both return foo's address
	void (*ptr_1)() = foo;
	void (*ptr_2)() = &foo;

	// both of the following are valid to call foo.
	ptr_1();
	(*ptr_2)();
}
```

Output:

```
Hello World!
Hello World!
```

> [!info] `foo()` with parameters  
> Assume that the `function` takes 2 `int` parameters and returns a `char`, i.e. `char foo(int a, int b)`.  
> In this case, the `function pointer` will look like `char (*ptr)(int, int) = foo`

```cpp
char foo(int a, int b) {
	char c = a + b;
	return c;
}

int main () {
	char (*ptr)(int, int) = foo;
	std::cout << ptr(65, 1) << std::endl;
}
```

Output:

```
B
```

## Passing `Functions` as Parameters

```cpp
int foo(int a, int b) {
    return a + b;
}

void sum(int (*fuzz)(int, int), int x, int y) {
    std::cout << fuzz(x, y) << std::endl;
}

int main () {
    sum(foo, 4, 5);
}
```

Output

```cpp
9
```

## Array of `Functions`

Using the `[]` in the `pointer` declaration, we can have an `array` of `functions`.

```cpp
int sum(int a, int b) {
    return a + b;
}

int sub(int a, int b) {
    return a - b;
}

int mul(int a, int b) {
    return a * b;
}

int main () {
    int (*ptr[])(int, int) = {sum, sub, mul};

    std::cout << ptr[0](5, 4) << std::endl;  // sum
    std::cout << ptr[1](5, 4) << std::endl;  // sub
    std::cout << ptr[2](5, 4) << std::endl;  // mul
}
```