---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Binary Search Tree
A #binary-tree in which all the items in the _left subtree_ are **smaller** than the `root` item and all the items in the _right subtree_ are **larger** than the `root` item, is called a #binary-search-tree.

# Traversing a Binary Tree
Imagine the _left subtree_, _right subtree_ and _root_ node labeled as `L`, `R` and `N` respectively.  
Then, the traversal of the form:
1. (N, L, R) is called #pre-order-traversal.
2. (L, N, R) is called #in-order-traversal.
3. (L, R, N) is called #post-order

# C++ Code

```cpp
void preorder(TreeNode<int>* treeNode) {
	if(treeNode != NULL) {
		cout << *(treeNode->getInfo())<<" ";
		preorder(treeNode->getLeft());
		preorder(treeNode->getRight());
	}
}
```

```cpp
void inorder(TreeNode<int>* treeNode) {
	if(treeNode != NULL) {
		inorder(treeNode->getLeft());
		cout << *(treeNode->getInfo())<<" ";
		inorder(treeNode->getRight());
	}
}
```

```cpp
void postorder(TreeNode<int>* treeNode) {
	if(treeNode != NULL) {
		postorder(treeNode->getLeft());
		postorder(treeNode->getRight());
		cout << *(treeNode->getInfo())<<" ";
	}
}
```
