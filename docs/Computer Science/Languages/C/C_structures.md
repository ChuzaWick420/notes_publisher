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