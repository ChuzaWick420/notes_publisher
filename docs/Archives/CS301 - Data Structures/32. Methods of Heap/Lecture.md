---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# perculateDown Method

```cpp
template <class eType>
void Heap<eType>::percolateDown(int hole) {
	int child;
	eType tmp = array[hole];
	
	for (; hole * 2 <= currentSize; hole = child) {
		child = hole * 2;
		
		if(child != currentSize && array[child + 1] < array[child])
			child++; //right child is smaller
			
		if(array[child] < tmp) 
			array[hole] = array[child];
			
		else 
			break ;
	}

	array[hole] = tmp;
	
}
```

# getMin Method

```cpp
template <class eType>
const eType& Heap<eType>::getMin() {

	if (!isEmpty())
		return array[1];
	
}
```

# buildHeap Method

```cpp
template <class eType>
void Heap<eType>::buildHeap(eType* anArray, int n) {
	
	for(int i = 1; i <= n; i++)
		array[i] = anArray[i - 1];
		
	currentSize = n;
	
	for(int i = currentSize / 2; i > 0; i--)
		percolateDown(i);
}
```

# isEmpty Method

```cpp
//isEmpty method
template <class eType>
bool Heap<eType>::isEmpty() {
	return currentSize == 0;
}
```

# isFull Method

```cpp
template <class eType>
bool Heap<eType>::isFull() {
	return currentSize == capacity;
}
```

# getSize Method

```cpp
template <class eType>
int Heap<eType>::getSize() {
	return currentSize;
}
```

# Theorem
For a `perfect binary tree` with height `h` containing `N` nodes ($2^{k+1} - 1$), the sum of the heights of `nodes` is $2^{k+1} - 1 - (h + 1)$ or $N - h - 1$  

$$S = \sum_{i = 0}^{h - 1} 2^i (h - i)$$

$$S = 2^{k+1} - 1 - (h + 1)$$

$$S\simeq N - \log_2{N + 1}$$
