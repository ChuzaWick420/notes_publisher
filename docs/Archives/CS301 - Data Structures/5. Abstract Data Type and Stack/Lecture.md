---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

An #abstract-data-type is a mathematical construct which is a set of values along with operations defined for those values.  
The `list` is an #abstract-data-type, we can change how it internally behaves and it doesn't affects the applications using that `data type` because the _interface_ is exactly the same.

# Stack

| Method Name | Description                                                |
| ----------- | ---------------------------------------------------------- |
| push(x)     | Insert x as the top element of the stack                   |
| pop()       | Remove the top element of the stack and return it.         |
| top()       | Return the top element without removing it from the stack. |

Assume the #stack is implemented using an array.

## Worst Case (start of the array)
`push()`: the whole array will need to be pushed towards right direction.  
`pop()`: the whole array will need to be pushed towards left direction.

## Best Case (end of the array)
`pop()` or `push()` won't cause any performance issues because there are no shifts involved, since the elements are added or removed from end (right side).

## Pop()

```cpp
int pop() {
	//return the current element and then decrement current.
	return array_name[current--];
}
```

## Push()

```cpp
void push(int value) {
	//current is incremented, then the new value is placed there
	array_name[++current] = value;
}
```

## top()

```cpp
int top() {
	return array_name[current];
}
```

## isEmpty()

```cpp
int isEmpty() {
	//when last element is poped, current goes from 0 to -1
	return (current == -1);
}
```

## isFull()

```cpp
int isFull() {
	return (current == size - 1);
}
```

## Class Implementation

```cpp
class Stack {
    public:
        Stack() { size = 10; current = -1;}    //constructor
        // The pop function   
        int pop(){ return A[current--];}           
        // The push function
        void push(int x){A[++current] = x;}
        // The top function
        int top(){ return A[current];}
        // Will return true when stack is empty
        int isEmpty(){return ( current == -1 );}
        // Will return true when stack is full
        int isFull(){ return ( current == size-1);}
     private:
       // The data element
       int object;
       // Index of the array
       int current;
       // max size of the array
       int size;
       // Array of 10 elements   
       int A[10];
};
```
