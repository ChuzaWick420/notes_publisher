---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# AVL Tree
If `k` is any level in the #binary-tree then total number of `nodes` at that level is $2^k$.

![[Pasted image 20240731200338.png]]

We need to keep track of these balance values called `balance factor`.

# Insertion in AVL Tree

![[Pasted image 20240731203736.png]]

Here `B` indicates the positions where inserting a node will keep the tree `balanced`.  
Whereas, the `U` indicates the positions where inserting a node will cause the whole tree to be `unbalanced`.

The letters `A`, `B`, `C` can be treated as numbers, meaning that they can be sorted in ascending or descending order. This order of letters (start from `A`, being less than `B`) is called `lexographic` order.

![[Pasted image 20240801164633.png]]

The order according to `inorder` is:
1. T1
2. B
3. T2
4. A
5. T3

Notice how if we are to insert a new element in `inorder` way, the balance of the tree is destroyed.

![[Pasted image 20240801164741.png]]

Notice how even after changing the arrangement of nodes in the tree, the order of `inorder` transversal remains the same.
1. T1
2. B
3. T2
4. A
5. T3

This tree modification process is called `Tree Rotation`.

# Example (AVL Tree Building)

![[Pasted image 20240801165419.png]]

First, we create a node with `1` as `root`.  
Then we insert `2` and since it is greater so it goes into the _right subtree_.

![[Pasted image 20240801165527.png]]

Similarly, we inserted `3` as well but now the balance of the tree is off.  

$$0 - 2 = -2$$

To fix this, we apply `rotation`.  
![[Pasted image 20240801165858.png]]
