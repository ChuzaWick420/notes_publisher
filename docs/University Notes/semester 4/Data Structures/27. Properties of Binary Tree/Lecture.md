---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Properties of Binary Tree
A #binary-tree with `N` `internal nodes` has `2N` links, `N - 1` with `internal nodes` and `N + 1` with `external nodes`.

# Threaded Binary Trees
This tree replaces the `null pointers` of a `node` to the appropriate `inorder successor` predecessor of that `node`.

# Adding Threads During Insert
Following are the steps which insert a `node` in the `threaded binary tree`

```cpp
t->L = p->L; // copy the thread
t->LTH = thread;
t->R = p; // *p is successor of *t
t->RTH = thread;
p->L = t; // attach the new leaf
p->LTH = child;
```

![[Pasted image 20240802022436.png]]

First instruction: points the `left pointer` to the `current node's left pointer`.  
![[Pasted image 20240802022548.png]]  
Next instruction: set the `flag` that `right` thread has been established  
![[Pasted image 20240802022858.png]]

Next instruction: point the `right pointer` of `t` to the `current node`.  
![[Pasted image 20240802023011.png]]

Next instruction: set the `flag` that `thread` has been established  
![[Pasted image 20240802023140.png]]

Next instruction: set the `left pointer` of `current node` to the `t` `node`.  
![[Pasted image 20240802023240.png]]

Lastly, set the `left pointer` of `t node` to the `current node`.  
![[Pasted image 20240802023426.png]]

The complete tree looks like this:  
![[Pasted image 20240802023652.png]]

```cpp
TreeNode* nextInorder(TreeNode* p) {
	
	if(p->RTH == thread) 
		return(p->R);
		
	else {
		p = p->R;
		
		while(p->LTH == child)
			p = p->L;
			
		 return p;
	}
}
```
