---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Usage of Const Keyword

```cpp
void change(const int& reg);
```

When this function is called, there is no copy of passed object is generated, due to it being a `reference`.  
Also, the function cannot change the value of it either because of it being a `const`.  
Hence, overall, this reduces the time because there is no memory generated.

Imagine this:

```cpp
const Etype& change() const;
```

The second `const` makes sure that the function does not changes the member variables of the class it belongs to.  
The first `const` makes sure that the returned `reference` is not modifiable by the caller.

# Degenerate BST

If we have sorted data then the #binary-search-tree takes the form of a #linked-list.  
![[Pasted image 20240731183529.png]]

The following tree is balanced as the number of `nodes` at each level are equal.  
![[Pasted image 20240731183621.png]]

However this is still not good enough.  
We need a #binary-search-tree with each `node` having a `sub right` and `sub left` tree.  
If `d` is the `depth` of a #binary-search-tree then total number of `nodes` in the tree should be $2^{d+1}-1$. Where `root level` having `d = 0`.

# AVL Tree
It is named after Adelson-Velskii and Landis.  
There are 2 differences between #AVL-tree and #binary-search-tree.
1. Height of left and right subtree might differ by at most 1.
2. Height of an empty tree is defined to be `-1`.

![[Pasted image 20240731194609.png]]

Look at this tree, the `root node` is `5`.  
The _right subtree_ has height `2` and the _left subtree_ has the height `3`.  
The difference of the heights between both subtrees is `1` or `-1` depending on which you subtract from which.  
These differences should be `1`, `-1` or `0` and should be consistent on every node.  
The `leaf nodes` have height `0`.

Let us define the `balance = left subtree height - right subtree height`  
![[Pasted image 20240731195448.png]]  
Look at the `root node`, it is `-1` because the height of _right subtree_ is 1 larger than the height of _left subtree_.
