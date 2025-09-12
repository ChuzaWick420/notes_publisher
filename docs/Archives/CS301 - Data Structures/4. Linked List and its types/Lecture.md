---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# start()

```cpp
//moves the pointers to the beginning of the list
void List::start() {
	lastCurrentNode = headNode;
	currentNode = headNode;
}
```

# remove()

```cpp
void List::remove() {
	if (currentNode != NULL && currentNode != headNode) {
		//set last's next to current's next
		lastCurrentNode->nextNode(currentNode()->getNext());
		//delete current 
		delete currentNode;
		//set current to new
		currentNode = lastCurrentNode->getNext();

		this->size--;
	}
}
```

# Doubly-linked List
A `node` in a #doubly-linked-list has 3 parts:
1. object
2. preNode
3. nextNode  
![[Pasted image 20240424121543.png]]  
![[Pasted image 20240424121647.png]]

Now imagine you want to insert a `node` with value `9` in them, it will be done as follows:  
![[Pasted image 20240424122005.png]]

```cpp
Node* newNode = new Node();
newNode -> set(9);
```

![[Pasted image 20240424122204.png]]

```cpp
newNode->setNext(current->getNext());
```

![[Pasted image 20240424122337.png]]

```cpp
newNode->setprev(current);
```

![[Pasted image 20240424122439.png]]

```cpp
(current->getNext())->setPrev(newNode);
```

![[Pasted image 20240424122522.png]]

```cpp
current->setNext(newNode);
```

![[Pasted image 20240424122709.png]]

```cpp
current = newNode;
```

![[Pasted image 20240424122739.png]]

# Circularly-Linked-List
![[Pasted image 20240424122941.png]]  
In this case, the last `node` points to first `node` instead of pointing to `NULL`.  
We can use `head` node to indicate when the `list` is repeating.

# Josephus Problem

```cpp
/*This program solves the Josephus Problem */

#include <iostream.h>
#include "CList.cpp"  //contains the circularly-linked list definition

// The main method
void main() {
	// creating an object of list
	CList list;
	int i, N=10, M=3;
	// initializing the list with values
	for(i=1; i <= N; i++ ) list.add(i);
	// pointing the pointers at the start of the list
	list.start();
	// counting upto M times and removing the element
	while( list.length() > 1 ) {
	    for(i=1; i <= M; i++ ) list.next();
	             cout << "remove: " << list.get() << endl;
	             list.remove();
	}
	//displaying the remaining node
	cout << "leader is: " << list.get() << endl;
}
```
