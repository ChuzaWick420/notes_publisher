---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Stack Implementation Using Linked List
`Stack` with `array` implementation has `size` limitation.  
To make the `stack` dynamically grow, we can implement it using `linked list`.

## Worst case
- Removing a `node` from the _end_ of the list would require us to transverse the whole list from `head` to the `node` before `current`.

## Best case
- `nodes` can be added at the _start_ using `head`.
- `nodes` can be added at the _end_ using `current`.

![[Pasted image 20240425103651.png]]

## pop()
![[Pasted image 20240425104409.png]]

```cpp
int value = head->get();
Node* p = head;
```

![[Pasted image 20240425104537.png]]

```cpp
head = head->getNext();
```

![[Pasted image 20240425104628.png]]

```cpp
delete p;
return value;
```

![[Pasted image 20240425104821.png]]

```cpp
int pop () {
	int value = head->get();
	Node* p = head;
	head = head->getNext();
	delete p;
	return value;
}
```

## push()
![[Pasted image 20240425104821.png]]

```cpp
Node* newNode = new Node();
```

![[Pasted image 20240425105448.png]]

```cpp
newNode->set(value);
newNode->setNext(head);
```

![[Pasted image 20240425105459.png]]

```cpp
head = newNode;
```

![[Pasted image 20240425105509.png]]

```cpp
void push(int value) {
	Node* newNode = new Node();
	newNode->set(value);
	newNode->setNext(head);
	head = newNode;
}
```

Other methods:

```cpp
int top () {
	return head->get();
}
```

```cpp
int isEmpty () {
	return (head == NULL);
}
```

**isFULL()** is not required since there is no issue of limitations on the `stack size`.

## Preference
- **Linked list:** each `stack` element has a higher memory space requirement (for the `next` pointers). The allocation and de-allocation of `nodes` also takes a little bit of time. But the benefit here is the memory can _grow_ and _shrink_ dynamically without any upper limit.
- **Array:** it is pre-allocated so it is faster in terms of `pop()` and `push()` requests. The down side here is the _fixed_ memory space, it cannot grow neither shrink and leaves vacant space behind after `pop()` operations.

## Operation Types
### 1. Infix
When the operator is in between the `operands`.  
**Example:** A + B;

### 2. Prefix
when the operator is _before_ the `operands`.  
**Example:** + A B; ++x;

### 3. Postfix
when the operator is _after_ the `operands`.  
**Example:** A B +; x++;

### Conversion of Infix to Postfix
**Examples:**
1. A + (B * C)
	1. A + (B C \*)
	2. A B C \* +
2. (A + B) * C
	1. (A B +) * C
	2. A B + C \*

### Operator Precedence
1. Exponentiation: ^
2. Multiplication / Division: \*, / 
3. Addition / Subtraction: +, -

#### Rules
- A + B + C means (A + B) + C (left-to-right rule).
- A ^ B ^ C means A ^ (B ^ C) (right-to-left rule).

**Examples:**

| infix                 | postfix               |
| --------------------- | --------------------- |
| A + B                 | A B +                 |
| 12 + 60 - 23          | 12 60 + 23 -          |
| (A + B) * (C - D)     | A B + C D - *         |
| A ^ B * C - D + E / F | A B ^ C * D - E F / + |
