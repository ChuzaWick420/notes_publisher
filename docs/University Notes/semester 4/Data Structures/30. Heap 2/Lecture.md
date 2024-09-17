---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Deleting from Min Heap
The deletion causes a hole in the array which is again, filled by reversing the insert process.

# Building Heap
- The time to insert a `leaf node` will be $\log_2{N}$ 
- The worst time for building a `heap` with `N` keys is $N \cdot \log_2{N}$

## Algorithm

```cpp
for(i = N/2; i > 0; i--)
	percolateDown(i);
```
