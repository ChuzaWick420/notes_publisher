# Arguments List with Variable Size

The declaration `...` indicates an unnamed list of arguments with unknown types.

```cpp
#include <stdarg.h>

void foo(int arg1, ...) { // (1)!
	va_list arg_ptr; // (2)!
	va_start(arg_ptr, arg1); // (3)!
	
	int a = va_arg(arg_ptr, int); // (4)!
	int b = va_arg(arg_ptr, double); 

	// use a and b

	va_end(arg_ptr); // (5)!
}
```

1. The `function` should have at least one _named_ parameter and the `...` must be declared in the end.
2. `#!cpp va_list` declares a `pointer` `arg_ptr` which is supposed to point to each argument in the list, at a time.
3. `#!cpp va_start()` sets the starting point, relative to the `arg1`. It is important to do before using the list.
4. `#!cpp va_arg()` returns the argument, converted into the specified type.
5. `#!cpp va_end()` is necessary for cleanup.

```cpp
int main () {
	foo(0, 400, 23.89); // (1)!
}
```

1. `0` is `arg1`, `400` is `a` and `23.89` is `b`.

## Flexibility

Notice the way `#!cpp foo()` is written, the list becomes very rigid, defeating the whole purpose. 

1. The number of arguments which can be passed to `#!cpp foo()` is specified.
2. The order in which the arguments can be passed to `#!cpp foo()` is also specified.

To remove these restrictions, we can craft `#!cpp foo()` in such a way that the order and amount of arguments depends on the first named argument. This is how `#!cpp printf()` does it too. Using a `#!cpp const char*` opens gates for it to specify the order and amount of arguments which are now dependent on the first named argument instead of the implementation within the `function`.