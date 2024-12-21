# Google

## C++ Style Guide

- Use 2 spaces, not tabs, escaping the dependency over engineers' machine configuration, affecting how code looks to each individual.
- Use `#!cpp auto` to only make the code _safer_ or _clearer_, otherwise use explicit types.
- Don't use pointers, if you want to use them then use `#!cpp std::unique_ptr`
- Minimize the usage of `exceptions`
- Use `composition` or `interface inheritance` instead of `implementation inheritance`

## Examples

### Interface Inheritance

```cpp
class Animal {
	virtual void speak(); // (1)!
};
```

1. Ensures that the `class` is explicitly an `abstract class`, not possessing any implementations of the interfaces(`functions`).

## References

Read about [cpp style guide](https://google.github.io/styleguide/cppguide.html)