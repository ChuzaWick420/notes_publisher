# Structures

A `#!cpp struct` is just a container, packaging different related variables.

```cpp
struct Rectangle { // (1)!
	int width = 10; // (2)!
	int length;
	char* label;
} rect1; // (3)!

int main () {
	struct Rectangle rect2; // (4)!
	return 0;
}
```

1. The name of the `#!cpp struct` (`Rectangle` in this case) is optional.
2. `#!cpp struct` is just a blueprint for defining a type, therefore the variables inside (called the `members`) do not allocate storage unless a variable of type `Rectangle` is declared. The `#!cpp struct` can be defined within a scope as well.
3. Defines a global variable `rect1` of type `#!cpp struct Rectangle`.
4. Defines a local variable `rect2` of type `#!cpp struct Rectangle`.

The `#!cpp struct` cannot contain itself but can contain pointer to it.

```cpp
struct Node {
	int value;
	struct Node* leftNode;
	struct Node* rightNode;
};
```

## Padding and Size

You can also use `#!cpp sizeof` operator to find out the size taken up by a `#!cpp struct`.

```cpp
struct Foo {
	char x;
	char y;
};

int main () {
	printf("%d\n", sizeof(Foo)); // (1)!
}
```

1. Outputs `2`.

```cpp
struct Foo {
	char x;
	int y;
};

int main () {
	printf("%d\n", sizeof(Foo)); // (1)!
}
```

1. Outputs `8`. Because the `#!cpp int` takes `4 bytes`, the compiler adds some `padding bytes` to the `#!cpp char` to make it aligned.

![[C_e_structure_padding.svg]]  
/// caption  
Each green block represents a `byte` for corresponding `type` within the `#!cpp`.  
///