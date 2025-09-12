---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Left-right Double Rotation
![[Pasted image 20240801175255.png]]

(ignore the caption in the img, it is not consistent with the lecture notes).

![[Pasted image 20240801175501.png]]

# Right-left Double Rotation
![[Pasted image 20240801175740.png]]

![[Pasted image 20240801175759.png]]

# C++ Code for AVL Insert Method

```cpp
/* This is the function used to insert nodes satisfying the AVL condition.*/
TreeNode* avlInsert(TreeNode* root, int info) {
	if(info < root->getInfo()){
	
		root->setLeft(avlInsert(root->getLeft(), info));
		int htdiff = height(root->getLeft()) – height(root->getRight());
		
		if(htdiff == 2) {
			if(info < root->getLeft()->getInfo())
				//outside insertion case 
				root = singleRightRotation(root); 
			else //inside insertion case 
				root = doubleLeftRightRotation(root);
		}
	}
	
	else if(info > root->getInfo()) {
	
		root->setRight(avlInsert(root->getRight(),info));
		int htdiff = height(root->getRight()) – height(root->getLeft());
		
		if(htdiff == 2) {
			if(info > root->getRight()->getInfo())
				root = singleLeftRotation(root);
			else 
				root = doubleRightLeftRotation( root ); 
		}
	}
// else a node with info is already in the tree. In // case, reset the height of this root node.
	int ht = Max(height(root->getLeft()), height(root->getRight()));
	// new height for root.
	root->setHeight(ht + 1);
	return root;
}
```
