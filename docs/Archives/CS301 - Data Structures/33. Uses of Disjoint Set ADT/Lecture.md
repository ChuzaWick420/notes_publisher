---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Priority Queue Using Heap

```cpp
#include “Event.cpp” 
#include “Heap.cpp” 
#define PQMAX 30 

class PriorityQueue {
	public: 
		PriorityQueue() {
			heap = new Heap (PQMAX);
		}; 

		~PriorityQueue() {
			delete heap; 
		};

		Event* remove() {
		
			if (!heap->isEmpty()) {
				Event* e;
				heap -> deleteMin(e);
				return e;
			}
			
			std::cout << "remove - queue is empty" << std::endl;
			return (Event*)NULL;
		};

		int insert (Event* e) {
		
			if (!heap->isFull()) {
				heap->insert(e);
				return 1;
			}

			std::cout << "insert queue is full" << std::endl;
		};

		int length() {
			return heap->getSize();
		}	

```

# Equivalence Relations
A binary relation R over a set S is called _equivalence relation_ if it has the following properties.
1. Reflexivity: $\forall x \in S, x R x$  
2. Symmetry: $\forall x \land y \in S, x R y \land y R x$ 
3. Transitivity: $\forall x, y, z \in S$ if $x R y \land y R z$ then $x R z$
