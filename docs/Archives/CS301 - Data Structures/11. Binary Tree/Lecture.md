---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Implementation of Priority Queue

```cpp
#include "Event.cpp"
#define PQMAX 30
class PriorityQueue {

	public:
		PriorityQueue() {
			size = 0; rear = -1;
		};
	
		~PriorityQueue() {};
		int full(void) {
			return ( size == PQMAX ) ? 1 : 0;
		};
	
		Event* remove() {
			if( size > 0 ) {
				Event* e = nodes[0];      
				for(int j=0; j < size-2; j++ )
				nodes[j] = nodes[j+1];
				size = size-1; rear=rear-1;
				if( size == 0 ) rear = -1;
				return e;
			}
			
			return (Event*)NULL;
			cout << "remove - queue is empty." << endl;
		};
	
		int insert(Event* e) {
			
			if( !full() ) {
				rear = rear+1;
				nodes[rear] = e;
				size = size 1;
				sortElements(); // in ascending order
				return 1;
			}
			
			cout << "insert queue is full." << endl;
			return 0;
		};
		
		int length() { return size; };
};
```

# Tree
There are some #data-structures which are _linear_ such as #stack, #linked-list etc.  
#tree is a _non-linear_ #data-structure.
# Binary Tree
It is a mathematical model defined as a

>[!NOTE]- #binary-tree is a finite set of elements which is either empty or is partitioned into 3 disjoint subsets.
>- the elements themselves are called `nodes`.
>- One of the 3 subsets contains a single `node` called the `root`.
>- Other 2 are `binary trees` themselves called the _left_ or _right_ `sub trees`.

![[Pasted image 20240608143138.png]]

# Terminologies of a Binary Tree
The _left subtree_ is called `left descendant` and _right subtree_ is called the `right descendant`.  
The `nodes` with no descendants are called `leaf nodes`.

# Strictly Binary Tree
This is a type of #binary-tree where every `non-leaf node` has to have a _left_ and a _right_ sub-tree.

# Level
The level of the `root node` is `0`.  
The more levels we go deeper, the more level increases by `1`.

## Depth
The maximum level number of a #binary-tree tree is called its `depth`.

# Complete Binary Tree
If there is _left_ and _right_ sub-tree of each node, it is called a `complete` #binary-tree.

If `l` is a certain `level value` in a `complete` #binary-tree then the number of `nodes` in that `level` is defined by `2^l`.

The total number of `nodes` in a `complete` #binary-tree with a `depth d` is:  

$$\sum^d_{i=0}2^i=2^{d+1}-1$$
