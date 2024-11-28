# Threads

```cpp
#include <thread>
```

The `#!cpp std::thread` object takes a `function pointer`[^1] as argument in its `constructor`.  
As soon as the `thread` object is created, it is executed.

```cpp
void hi () {
	std::cout << "hi" << std::endl;
}

int main () {
	std::thread thread_1(hi);  //hi() is immediately fired off
}
```

## References

[^1]: Read more about [[Function Pointers|function pointers]].