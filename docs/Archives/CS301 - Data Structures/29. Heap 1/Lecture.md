---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Complete Binary Tree
![[Pasted image 20240802033238.png]]  
If the #array has _holes_ in it then it is not a `complete binary tree`.

# Heap
The `complete binary tree` with `heap order` is called a `heap`.  
This `heap order` (in case of `min heap`) is defined such that if `k` is the keys of `nodes` then $k_p \le k_c$  
Where subscript `p` stands for `parent node` and `c` stands for `child nodes`.

# Max Heap
`max heap` follows $k_p \ge k_c$.  
![[Pasted image 20240802034336.png]]

# Insertion in a Heap
If inserting a new element violates the `min heap` order then it replaces positions with the arrow's(pointed in the array) _head_ and _tail_  
![[Pasted image 20240802034657.png]]
