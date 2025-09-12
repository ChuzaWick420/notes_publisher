---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Reference Variable
`&variable` returns the `address` of the `variable`.

There are 3 types of calls.
1. Call by Value
2. Call by Pointer
3. Call by Reference

## Call by Value

```cpp
int main () {
	int val = 5;
	func(val);
	return 0;
}

void func (int para_var) {
	para_var++;
}
```

## Call by Pointer

```cpp
int main () {
	int val = 5;
	func(&val);
	return 0;
}

void func (int *para_var) {
	*(para_var)++;
}
```

## Call by Reference

```cpp
int main () {
	int val = 5;
	func(val);
	return 0;
}

void func (int &para_var) {
	para_var++;
}
```
