---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Single Right Rotation

![[Pasted image 20240801181841.png]]

```cpp
TreeNode* singleRightRotation(TreeNode* k2) {
	if(k2 == NULL)
		return NULL; // k1 (first node in k2's left subtree) will be the new root 
	TreeNode* k1 = k2->getLeft(); // Y moves from k1's right to k2's left 
	k2->setLeft(k1->getRight());
	k1->setRight(k2); 
	// reassign heights. First k2 
	int h = Max(height(k2->getLeft()), height(k2->getRight()));
	k2->setHeight(h+1);
	// k2 is now k1's right subtree 
	h = Max(height(k1->getLeft()), k2->getHeight()); 
	k1->setHeight(h+1);
	return k1;
}
```

## Height Function

```cpp
int height(TreeNode* node) {

	if(node != NULL) 
		return node->getHeight();
		
	return –1;
}
```

# Single Left Rotation

![[Pasted image 20240801182033.png]]

```cpp
TreeNode* singleLeftRotation(TreeNode* k1) {
	if(k1 == NULL)
		return NULL; // k2 is now the new root 
		
	TreeNode* k2 = k1->getRight();
	k1->setRight(k2->getLeft()); // Y 
	k2->setLeft(k1); // reassign heights. First k1 (demoted) 
	
	int h = Max(height(k1->getLeft()), height(k1->getRight())); 
	
	k1->setHeight(h+1); // k1 is now k2's left subtree 
	h = Max( height(k2->getRight()), k1->getHeight()); 
	k2->setHeight(h+1); 
	
	return k2;
}
```

# Double Right-Left Rotation
![[Pasted image 20240801182333.png]]

![[Pasted image 20240801182538.png]]

```cpp
TreeNode* doubleRightLeftRotation(TreeNode* k1) { 
	if(k1 == NULL)
		// single right rotate with k3 (k1's right child) 
		return NULL; 
		
	// now single left rotate with k1 as the root 
	k1->setRight(singleRightRotation(k1->getRight())); 
	return singleLeftRotation(k1);
}
```

# Double Left-right Rotation
![[Pasted image 20240801182814.png]]

![[Pasted image 20240801182841.png]]

```cpp
TreeNode* doubleLeftRightRotation(TreeNode* k3) {
	if(k3 == NULL)
		// single left rotate with k1 (k3's left child) 
		return NULL; 
		
	// now single right rotate with k3 as the root 
	k3->setLeft(singleLeftRotation(k3->getLeft())); 
	return singleRightRotation(k3);
}
```

# Deletion in AVL Tree
At the worst case, we will have to perform $log_2(N)$ rotations where `N` is the number of nodes.  
![[Pasted image 20240801213634.png]]

We are going to delete node `A` and it will be the worst case possible.

![[Pasted image 20240801213811.png]]

![[Pasted image 20240801213832.png]]

![[Pasted image 20240801213852.png]]

# Cases of Deletion in AVL Tree
There are 5 cases:

## Case 1a

>[!NOTE] The `node` to be deleted has a parent with `balance` as `0` and the `node` is in _left subtree_

![[Pasted image 20240801214522.png]]

The left one indicates that the `node` has `0` `balance`.  
The right one indicates that the `node` has _right subtree_ with greater `height`.

## Case 1b

>[!NOTE] The `node` to be deleted has a parent with `balance` as `0` and the `node` is in _right subtree_

![[Pasted image 20240801214829.png]]

## Case 2a

>[!NOTE]- The `node` to be deleted is at the _left subtree_ of a parent `node` with no _right subtree_

![[Pasted image 20240801215040.png]]
