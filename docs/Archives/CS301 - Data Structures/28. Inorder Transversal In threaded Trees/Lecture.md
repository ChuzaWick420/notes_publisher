---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Inorder Traversal in Threaded Tree
The code snippet in previous lecture is not enough to determine the `inorder` traversal from the `root node`.  
We therefore need a _dummy node_ for it to work.  
![[Pasted image 20240802031159.png]]

# Complete Binary Tree
![[Pasted image 20240802031846.png]]

The tree with `leaf nodes` being from left to right is called a `complete binary tree`
1. The total number of `nodes` can be between $2^k$ to $2^{k+1}-1$ `nodes`.
2. The height of such a tree is $\lfloor log_2{N} \rfloor$  

We can arrange the tree in an #array following the `level order` pattern  
![[Pasted image 20240802032618.png]]

>[!NOTE] For any given element with index `i`, the _left child node_ is at index `2i` and the right one being at index `2i + 1` and parent `node` being at $\lfloor \frac{i}{2} \rfloor$ 
