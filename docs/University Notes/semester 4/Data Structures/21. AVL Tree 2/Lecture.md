---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# AVL Tree Building Example
If the `balance factor` of each node in the tree is `0` then it is called a `perfectly balanced tree`.  
As we keep inserting nodes, we eventually reach a point like this.  

![[Pasted image 20240801173440.png]]

We need to perform a `rotation`.  
![[Pasted image 20240801173556.png]]

# Cases for Rotation
There are `4` cases of violation:
1. An assertion into the _left subtree_ of the _left child_ of `alpha`.
2. An assertion into the _right subtree_ of the _right child_ of `alpha`.
3. An assertion into the _left subtree_ of the _right child_ of `alpha`.
4. An assertion into the _left subtree_ of the _right child_ of `alpha`.

For case `1` and `2`, the single rotation is enough to balance the tree but for other cases, it is not.  
![[Pasted image 20240801174716.png]]

![[Pasted image 20240801174747.png]]
