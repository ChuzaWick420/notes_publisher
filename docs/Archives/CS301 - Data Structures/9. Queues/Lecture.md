---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

![[Pasted image 20240501162240.png]]  
The #process contains the `code` of its executable,  
Then it has some `static` data such as `global` variables etc.  
Then it has a #stack which grows downwards and a #heap which grows upward. #heap is for #dynamic-memory-allocation.

When we declare a variable as `static`, it is moved into the static data portion.  
That is the reason when the functions `return`, those variables do not lose their data.

# Queues
This #data-structure uses the #FIFO (First In First Out) philosophy.

| Operation  | Description                                    |
| ---------- | ---------------------------------------------- |
| enqueue(X) | Place X at the _rear_ of the queue.            |
| dequeue()  | Remove the _front_ element and return it.      |
| front()    | Return _front_ element without removing it.    |
| isEmpty()  | Return TRUE if queue is empty, FALSE otherwise |

![[Pasted image 20240501202244.png]]
- Removal or Addition of `nodes` take constant time if done on `front` or `rear`.
- `rear` should be used for insertion because it is already in the end.
- `front` should be used when we are removing all `nodes` (because we can transverse through the list).

```cpp
//removes the front element and move the front pointer forward
int dequeue() {
	int x = front->get();
	Node* p = front;
	front = front->getNext();
	delete p;
	return x;
}

/* Insert an element in the rear */
void enqueue(int x) {
	Node* newNode = new Node();
	newNode->set(x);
	newNode->setNext(NULL);
	rear->setNext(newNode);
	rear = newNode;
}

/* To retrieve the front element */
int front() {
	return front->get();
}

/* To check if the queue is empty */
int isEmpty() {
	return (front == NULL);
}
```

## Array Implementation
With the array implementation, removal of `nodes` at the `front` will leave empty space.  
![[Pasted image 20240501205122.png]]  
As shifting the array will be costly, we will leave it as it is.

Now if we insert 2 elements, then we run into problem that there is still 2 places (index: `0`, `1`) remaining to be filled.  
There should be a way to wrap around.  
That is why we are going to make it into a _circle_.

![[Pasted image 20240501211930.png]]  
Now we have to keep track of:
- Where the `front` is.
- Where the `rear` is.
- What is the _size_ of the array.
- Total number of elements stored in the array.

```cpp
void enqueue(int x) {
	rear = (rear + 1) % size;
	array[rear] = x;
	noElements = noElements + 1;
}

int isFull() {
	return noElements == size;
}

int isEmpty() {
	return noElements == 0;
}

int dequeue() {
	int x = array[front];
	front = (front + 1) % size;
	noElements = noElements - 1;
	return x;
}
```
