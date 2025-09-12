---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# C++ Code for Remove

```cpp
TreeNode<int>* remove(TreeNode<int>* tree, int info) {
	TreeNode<int>* t;
	int cmp = info - *(tree->getInfo());
	
	if(cmp < 0){// node to delete is in left subtree
		t = remove(tree->getLeft(), info);
		tree->setLeft(t);
	}
    
	else if(cmp > 0){ // node to delete is in right subtree
		t = remove(tree->getRight(), info);
		tree->setRight(t);
	}
	
	//two children, replace with inorder successor
	else if(tree->getLeft() != NULL && tree->getRight() != NULL){ 
		TreeNode<int>* minNode;
		MinNode = findMin(tree->getRight());
		tree->setInfo(minNode->getInfo());
		t = remove(tree->getRight(), *(minNode->getInfo()));
		tree->setRight(t);
	}
	
	else {  // _case 1_
		TreeNode<int>* nodeToDelete = tree;
		
		if(tree->getLeft() == NULL) //will handle 0 children
			tree = tree->getRight();
		else if(tree->getRight() == NULL)
			tree = tree->getLeft();
		else tree = NULL;
		
		delete nodeToDelete;  // release the memory
	}
	
	return tree;
}
```

```cpp
TreeNode<int>* findMin(TreeNode<int>* tree) {
	if(tree == NULL)
		return NULL;
		
	if(tree->getLeft() == NULL)
		return tree; // _this is it._
		
	return findMin(tree->getLeft());
}
```

# Binary Search Tree Class

```cpp
#ifndef _BINARY_SEARCH_TREE_H_
#define _BINARY_SEARCH_TREE_H_

#include <iostream.h>

// Binary node and forward declaration
template <class EType>
class BinarySearchTree;

template <class EType>
class BinaryNode {

	EType element;
	BinaryNode *left;
	BinaryNode *right;
	// constructor
	BinaryNode(const EType& theElement, BinaryNode *lt, BinaryNode *rt) : element(theElement), left(lt), right(rt){}
	
	friend class BinarySearchTree<EType>;
};
```

```cpp
/* binarysearchtree.h file also contains the definition of the BinarySearchTree */
template <class EType>
class BinarySearchTree {
	public:
		BinarySearchTree(const EType& notFound);
		BinarySearchTree(const BinarySearchTree& rhs);
		~BinarySearchTree();
		const EType& findMin() const;
		const EType& findMax() const;
		const EType& find(const EType & x) const;
		bool isEmpty() const;
		void printInorder() const;
		void insert(const EType& x);
		void remove(const EType& x);
		const BinarySearchTree & operator = (const BinarySearchTree & rhs);
		
	private:
		BinaryNode<EType>* root;
		// ITEM_NOT_FOUND object used to signal failed finds
		const EType ITEM_NOT_FOUND;
		const EType& elementAt(BinaryNode<EType>* t);
		void insert(const EType& x, BinaryNode<EType>* & t);
		void remove(const EType& x, BinaryNode<EType>* & t);
		BinaryNode<EType>* findMin(BinaryNode<EType>* t);  
		BinaryNode<EType>* findMax(BinaryNode<EType>* t);
		BinaryNode<EType>* find(const EType& x, BinaryNode<EType>* t );
		void makeEmpty(BinaryNode<EType>* & t);
		void printInorder(BinaryNode<EType>* t);
};
#endif
```

# Sample Program

```cpp
/* This file contains the declaration of binary node and the binary search tree */
#ifndef BINARY_SEARCH_TREE_H_
#define BINARY_SEARCH_TREE_H_
#include <iostream.h>       // For NULL
  // Binary node and forward declaration
template <class EType>
class BinarySearchTree;

template <class EType>
class BinaryNode {
    EType element;
    BinaryNode *left;
    BinaryNode *right;
    BinaryNode(const EType & theElement, BinaryNode *lt, BinaryNode *rt) : element(theElement), left(lt), right(rt){}
    friend class BinarySearchTree<EType>;
};

// BinarySearchTree class
//
// CONSTRUCTION: with ITEM_NOT_FOUND object used to signal failed finds
//
// ******************PUBLIC OPERATIONS*********************
// void insert(x)       --> Insert x
// void remove(x)       --> Remove x
// EType find(x)   --> Return item that matches x
// EType findMin()  --> Return smallest item
// EType findMax()  --> Return largest item
// boolean isEmpty()     --> Return true if empty; else false
// void makeEmpty()      --> Remove all items
// void printTree()      --> Print tree in sorted order

template <class EType>
class BinarySearchTree {

	public:
		BinarySearchTree(const EType& notFound);
		BinarySearchTree(const BinarySearchTree& rhs);
		
		~BinarySearchTree();
		
		const EType& findMin() const;
		const EType& findMax() const;
		const EType& find(const EType& x) const;
		
		bool isEmpty() const;
		void printTree() const;
		void makeEmpty();
		
		void insert(const EType & x);
		void remove(const EType & x);
		
		const BinarySearchTree& operator=(const BinarySearchTree& rhs);
		
	private:
		BinaryNode<EType> *root;
		
		const EType ITEM_NOT_FOUND;
		const EType& elementAt(BinaryNode<EType> *t) const;
		
		void insert(const EType& x, BinaryNode<EType>* & t) const;
		void remove(const EType& x, BinaryNode<EType>* & t) const;
		
		BinaryNode<EType>* findMin(BinaryNode<EType> *t) const;
		BinaryNode<EType>* findMax(BinaryNode<EType> *t) const;
		BinaryNode<EType>* find(const EType& x, BinaryNode<EType> *t) const;
		
		void makeEmpty(BinaryNode<EType>* &t) const;
		void printTree(BinaryNode<EType> *t) const;
		
		BinaryNode<EType>* clone(BinaryNode<EType> *t) const;
};

#include "BinarySearchTree.cpp"
#endif
```

The contents of the `BinarySearchTree.cpp`:

```cpp
/* This file contains the implementation of the binary search tree */
#include <iostream.h>
#include "BinarySearchTree.h"

//construct the tree
template <class EType>
BinarySearchTree<EType>::BinarySearchTree(const EType& notFound) : ITEM_NOT_FOUND(notFound), root(NULL) {}

//Copy Constructor
template <class EType>
BinarySearchTree<EType>::BinarySearchTree(const BinarySearchTree<EType>& rhs) : root(NULL), ITEM_NOT_FOUND(rhs.ITEM_NOT_FOUND) {
	*this = rhs;
}

//Destructor
template <class EType>
BinarySearchTree<EType>::~BinarySearchTree() {
	makeEmpty();
}

//Insert x into the tree; duplicates are ignored.
template <class EType>
void BinarySearchTree<EType>::insert(const EType& x) {
	insert(x, root);
}

//Remove x from the tree. Nothing is done if x is not found.
template <class EType>
void BinarySearchTree<EType>::remove(const EType& x) {
	remove(x, root);
}

//Find the smallest item in the tree.
//Return smallest item or ITEM_NOT_FOUND if empty.
template <class EType>
const EType& BinarySearchTree<EType>::findMin() const {
	return elementAt(findMin(root));
}

//Find the largest item in the tree.
//Return the largest item of ITEM_NOT_FOUND if empty.
template <class EType>
const EType& BinarySearchTree<EType>::findMax() const {
	return elementAt(findMax(root));
}

//Find item x in the tree.
//Return the matching item or ITEM_NOT_FOUND if not found.
template <class EType>
const EType& BinarySearchTree<EType::find(const EType& x) const {
	return elementAt(find(x, root));
}

//Make the tree logically empty.
template <class EType>
void BinarySearchTree<EType>::makeEmpty() {
	makeEmpty(root);
}

//Test if the tree is logically empty.
//Return true if empty, false otherwise.
template <class EType>
bool BinarySearchTree<EType>::isEmpty() const {
	return root == NULL;
}

//Print the tree contents in sorted order.
template <class EType>
void BinarySearchTree<EType>::printTree() const {
	if(isEmpty())
		cout << "Empty tree" << endl;
	else
		printTree( root );
}

//Deep copy.
template <class EType>
const BinarySearchTree<EType>& BinarySearchTree<EType>::operator=( const BinarySearchTree<EType>& rhs) {
	if(this != &rhs) {
		makeEmpty();
		root = clone(rhs.root);
	}
	return *this;
}

//Internal method to get element field in node t.
//Return the element field or ITEM_NOT_FOUND if t is NULL.
template <class EType>
const EType & BinarySearchTree<EType>::elementAt(BinaryNode<EType> *t) const {
	if(t == NULL)
		return ITEM_NOT_FOUND;
	else
		return t->element;
}

//Internal method to insert into a subtree.
//x is the item to insert.
//t is the node that roots the tree.
//Set the new root.
template <class EType>
void BinarySearchTree<EType>::insert(const EType& x, BinaryNode<EType>* &t) const {
	if(t == NULL)
		t = new BinaryNode<EType>(x, NULL, NULL);
	else if(x < t->element)
		insert(x, t->left);
	else if(t->element < x)
		insert(x, t->right);
	else
        ;  // Duplicate; do nothing
}

//Internal method to remove from a subtree.
//x is the item to remove.
//t is the node that roots the tree.
//Set the new root.
template <class EType>
void BinarySearchTree<EType>::remove(const EType& x, BinaryNode<EType>* & t) const {
	if(t == NULL)
		return;   // Item not found; do nothing
	if(x < t->element)
		remove( x, t->left );
	else if(t->element < x)
		remove(x, t->right);
	else if(t->left != NULL && t->right != NULL) {// Two children
		t->element = findMin(t->right)->element;
		remove(t->element, t->right);
	}
	else {
		BinaryNode<EType> *nodeToDelete = t;
		t = (t->left != NULL) ? t->left : t->right;
		delete nodeToDelete;
    }
}

//Internal method to find the smallest item in a subtree t.
//Return node containing the smallest item.
template <class EType>
BinaryNode<EType>* BinarySearchTree<EType>::findMin(BinaryNode<EType> *t) const {
	if(t == NULL)
		return NULL;
	if(t->left == NULL)
		return t;
    return findMin(t->left);
}

//Internal method to find the largest item in a subtree t.
//Return node containing the largest item.
template <class EType>
BinaryNode<EType>* BinarySearchTree<EType>::findMax(BinaryNode<EType> *t) const {
	if(t != NULL)
		while(t->right != NULL)
			t = t->right;
	return t;
}

//Internal method to find an item in a subtree.
//x is item to search for.
//t is the node that roots the tree.
//Return node containing the matched item.
template <class EType>
BinaryNode<EType>* BinarySearchTree<EType>::find(const EType& x, BinaryNode<EType> *t) const {
	if(t == NULL)
		return NULL;
	else if(x < t->element)
		return find(x, t->left);
	else if(t->element < x)
		return find(x, t->right);
	else
		return t;    // Match
}

//**********NONRECURSIVE VERSION**********
template <class EType>
BinaryNode<EType> *
BinarySearchTree<EType>::find(const EType& x, BinaryNode<EType> *t) const {
	while(t != NULL) {
		if(x < t->element)
			t = t->left;
		else if( t->element < x )
			t = t->right;
		else
			return t;    // Match
	}
	return NULL;   // No match
}

//Internal method to make subtree empty.
template <class EType>
void BinarySearchTree<EType>::makeEmpty(BinaryNode<EType>* &t) const {
	if(t != NULL) {
		makeEmpty(t->left);
		makeEmpty(t->right);
		delete t;
	}
	t = NULL;
}

//Internal method to print a subtree rooted at t in sorted order.
template <class EType>
void BinarySearchTree<EType>::printTree(BinaryNode<EType> *t) const {
	if(t != NULL){
		printTree(t->left);
		cout << t->element << endl;
		printTree(t->right);
	}
}

//Internal method to clone subtree.
template <class EType>
BinaryNode<EType>* BinarySearchTree<EType>::clone(BinaryNode<EType> *t) const {
	if(t == NULL)
		return NULL;
	else
		return new BinaryNode<EType>(t->element, clone(t->left), clone(t->right));
}
```
