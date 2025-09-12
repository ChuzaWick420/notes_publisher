---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Templates
Since there are different #data-types and we use same structure for those #data-types, that is why, we can use #templates.

```cpp
template <class T>
class Stack {

	public:
		Stack();
		// 1=true, 0=false
		int empty(void);              
		// 1=successful,0=stack overflow
		int push(T &);
		T pop(void);
		T peek(void);
		~Stack();
		
	private:
		int top;
		T* nodes;
};
```

Here `T` is our _generic_ #data-type.

```cpp
#include <iostream.h>
#include <stdlib.h>
#include "Stack.h"
#define MAXSTACKSIZE 50

template <class T>
Stack<T>::Stack() {
	top = -1;
	nodes = new T[MAXSTACKSIZE];
}

template <class T>
Stack<T>::~Stack() {
	delete nodes;
}

template <class T>
int Stack<T>::empty(void) {
	if( top < 0 ) return 1;
	return 0;
}

template <class T>
int Stack<T>::push(T& x) {
	if( top < MAXSTACKSIZE ) {
		nodes[++top] = x;
		return 1;
	}
	
	cout << "stack overflow in push.\n";
	return 0;
}

template <class T>
T Stack<T>::pop(void) {
	T x;
	if( !empty() ) {
		x = nodes[top--];
		return x;
	}
	
	cout << "stack underflow in pop.\n";
	return x;
}
```

The `constructor` allocates the memory for the stack.  
The `destructor` destroys all the memory allocated by the `constructor`.  
The `empty` function returns `1` if the #stack is empty, otherwise `0`.  
The `push` function returns `1` after moving the `top` tracker above and placing the value `x` in it.  
The `pop` function does the opposite.

# Call Stack
![[Pasted image 20240501145957.png]]  
the `return address` refers to the location where control returns after function has done executing.

```cpp
int i_avg(int a, int b) {
	return (a + b) / 2;
}
```

The #assembly code it generates is:

```asm
globl _i_avg
	_i_avg:
		movl 4(%esp), %eax
		addl 8(%esp), %eax    # Add the args
		sarl $1, %eax         # Divide by 2
		ret                   # Return value is in %eax
```

Following line says that `i_avg` is a `global function`.

```asm
globl _i_avg
```

Following line means that we move 4 bytes (because argument is an `integer`) from the #stack-pointer(`%esp`) and place the result into register `%eax`.

```asm
movl 4(%esp), %eax
```

The next line means that an offset of `8` lines is taken and is added to the register `%eax`.

```asm
addl 8(%esp), %eax    # Add the args
```

This line divides the `%eax` by `2` .

```asm
sarl $1, %eax         # Divide by 2
```

Then we just `return`.

```asm
ret
```

This whole process of using `stacks` for function calling is called #run-time-environment.
