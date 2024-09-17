---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Deletion in AVL Tree
## Case 3a

>[!NOTE]- The `node` to be deleted is in the _left subtree_ of a parent with `balance` `-1`. The _right subtree_ was balanced.

![[Pasted image 20240801215959.png]]

To fix this  
![[Pasted image 20240801220215.png]]

## Case 4a

>[!NOTE]- The `node` to be deleted is in the _left subtree_ of a parent with `balance` `-1`. The _right subtree_ was unbalanced.

![[Pasted image 20240801220351.png]]

![[Pasted image 20240801220434.png]]

## Case 5a
![[Pasted image 20240801220638.png]]

To fix this:  
![[Pasted image 20240801220815.png]]

# Other Uses of Binary Tree
## Expression Trees
![[Pasted image 20240801221058.png]]

These are sometimes also called `parse trees`.

## Compiler Optimization
Let an `expression` be `(f+d*e) + ((d*e+f)*g)`, its `expression tree` will be:  
![[Pasted image 20240801221630.png]]

Notice how the circled blobs are similar? We can re-write it as:  
![[Pasted image 20240801221718.png]]
