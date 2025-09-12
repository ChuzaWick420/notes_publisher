---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

![[Pasted image 20240424095248.png]]

The memory address of `head` itself is `1062`.  
It stores the value (memory address of the first `node`) `1054`.  
The first `node` stores the value `2` and a `pointer` (value: `1051`) to the next `node` (which stores value `6`).  
The `current` pointer (with address: `1053`) points to `1063` which is the 3rd `node`, also pointed by 2nd `node`.

# Node Insertion

```cpp
Node* newNode = new Node(9);
```

This creates an object of class `Node` with `9` passed as a parameter to it's `constructor`.  
![[Pasted image 20240424100414.png]]

Algorithm: 
1. Get the node pointed by `current`.
2. Set `newNode.next` to `current.next`.
3. Set `current.next` to `newNode`.
4. Set `current` to `NewNode`.

# Node

```cpp
class Node {
	public:
		int get() {
			return object;	
		}

		void set(int value) {
			this->object = value;
		}

		Node* getNext() {
			return nextNode;	
		}

		void setNext(Node* node) {
			this->nextNode = node;
		}
	private:
		int object;
		Node* nextNode;
}
```

This `Node` class is a `factory`.  
`state variables`: `object`, `nextNode`.  
`methods`: `get`, `set`, `getNext`, `setNext`.

# List

```cpp
class List {
	public:
		List () {
			headNode = new Node();
			headNode -> setNext(NULL);
			currentNode = NULL;
			size = 0;
		}

	private:
		int size;
		Node* headNode;
		Node* currentNode;
		Node* lastCurrentNode;
}
```

## Add()

```cpp
void List::add(int value) {
	//create a node
	Node* newNode = new Node();

	//if the list is NOT empty
	if (currentNode != NULL) {
		//set new's next to current's next
		newNode->setNext(currentNode->getNext());
		newNode->set(value);
		//set new to current's next
		currentNode->setNext(newNode);
		//keeps track of preview node
		lastCurrentNode = currentNode;
		//set current to new
		currentNode = newNode;
	}

	//otherwise if the list is empty, there are no nodes in it
	else {
		//the final the only node
		newNode->setNext(NULL);
		headNode->setNext(newNode);
		lastCurrentNode = headNode;
		currentNode = newNode;
	}
	
	this->size++; //since a new node is added
}
```
