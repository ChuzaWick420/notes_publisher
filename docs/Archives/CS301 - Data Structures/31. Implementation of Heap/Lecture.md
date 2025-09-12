---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# C++ Code

```cpp
/* The heap class. This is heap.h file */ 
template <class eType>
class Heap {
	public:
		Heap(int capacity = 100);
		void insert(const eType& x);
		void deleteMin(eType& minItem); 
		const eType& getMin(); 
		bool isEmpty();
		bool isFull();
		int Heap<eType>::getSize();
		
	private: 
		// The heap array 
		eType* array; 
		// Number of elements in heap 
		int currentSize;
		int capacity;
		void percolateDown(int hole);
};

```

```cpp
#include <Heap.h>

template <class eType>
Heap<eType>::Heap(int capacity) {
	array = new eType[capacity + 1];
	currentSize = 0;
}

template <class eType>
bool Heap<eType>::insert(const eType& x) {
	if (isFull()) {
		std::cout << "insert - Heap is full" << std::endl;
		return 0;
	}

	//percolate up
	int hole = ++currentSize;
	for (; hole > 1 && x < array[hole / 2]; hole /= 2)
		array[hole] = array[hole / 2];
	array[hole] = x;
}

```
