---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Operations on Binary Tree

| **Operation**  | **Description**                                                            |
| -------------- | -------------------------------------------------------------------------- |
| left(p)        | Returns a pointer to the left sub-tree                                     |
| right(p)       | Returns a pointer to the right sub-tree                                    |
| parent(p)      | Returns the father node of p                                               |
| brother(p)     | Returns the brother node of p                                              |
| info(p)        | Returns the contents of node p                                             |
| setLeft(p, x)  | Creates the left child node of _p_ and set the value _x_ into it.          |
| setRight(p, x) | Creates the right child node of _p_, the child node contains the info _x_. |

# Applications of Binary Tree
#binary-tree is useful when a 2-way decision is made at each point.  
**Example:** we want to find the duplicates from the following list:

```
14, 15, 4, 9, 7, 18, 3, 5, 16, 4, 20, 17, 9, 14, 5
```

# Searching For Duplicates
We can either use an #array or a #linked-list to transverse this list and figure out the frequency of the duplicate elements but it is slow.  
It can be optimized by using a #binary-tree implemented through #linked-list.

The first element becomes the `root` node, for the other elements, if they are _less_ than the `root` then they become part of the _left subtree_.  
Otherwise, if greater, then they become part of _right subtree_.

# C++ Implementation of Binary Tree

## Implementation

```cpp
/* This file contains the TreeNode class declaration. TreeNode contains the functionality for a binary tree node. */

#include <stdlib.h>

template <class Object>
class TreeNode {
	public:
		// constructors
		TreeNode() {
			this->object = NULL;
			this->left = this->right = NULL;
		};
  
		TreeNode( Object *  object ) {
			this->object = object;
			this->left = this->right = NULL;
		};
		
		Object* getInfo() {
			return  this->object;
		};
		
		void setInfo(Object* object) {
			this->object = object;
		};
		
		TreeNode* getLeft() {
			return left;
		};
		
		void setLeft(TreeNode* left) {
			this->left = left;
		};
		
		TreeNode* getRight() {
			return right;
		};
		
		void setRight(TreeNode* right) {
			this->right = right;
		};
		
		int isLeaf() {
		
			if(this->left == NULL && this->right == NULL)
				return  1;
				
			return  0;
		};
 
	private:
		Object* object;
		TreeNode* left;
		TreeNode* right;
}; // end class TreeNode
```

## Usage

```cpp
#include <iostream>
#include <stdlib.h>
#include "TreeNode.cpp"

int main(int argc, char* argv[]) {

    int x[] = {14,15,4,9,7,18,3,5,16,4,20,17,9,14,5,-1};
    TreeNode<int>* root = new TreeNode<int>();
    root->setInfo(&x[0]);
    
    for(int i = 1; x[i] > 0; i++) {
        insert(root, &x[i]);
    }
}

void insert(TreeNode<int>* root, int* info) {

    TreeNode<int>* node = new TreeNode <int> (info);
    TreeNode<int>* p, *q;
    p = q = root;
    
    while(*info != *(p->getInfo()) && q != NULL) {
        p = q;
        if(*info < *(p->getInfo()))
            q = p->getLeft();
        else
            q = p->getRight();
    }
    
    if(*info == *(p->getInfo())) {
        std::cout << "attempt to insert duplicate: " << *info << std::endl;
        delete node;
    }
    else if(*info < *(p->getInfo()))
        p->setLeft(node);
    else
        p->setRight(node);
}

```

# Trace of Insert
We are inserting number `17`.  
First, the `p` and `q` point to the `root`.  
![[Pasted image 20240608210433.png]]

Then this section is executed:

```cpp
while(*info != *(p->getInfo()) && q != NULL) {
	p = q;
	if(*info < *(p->getInfo()))
		q = p->getLeft();
	else
		q = p->getRight();
}
```

The `else` block is triggered and `q` is moved to the _right_.  
![[Pasted image 20240608211622.png]]

```cpp
p = q;
```

![[Pasted image 20240608212008.png]]

As the #while-loop repeats,  
![[Pasted image 20240608212248.png]]

After reaching `16`, the statement:  

```cpp
else
    q = p->getRight();
```

Is executed and makes the #while-loop condition false.

![[Pasted image 20240608212543.png]]

Then finally, this section runs

```cpp
if(*info == *(p->getInfo())) {
    std::cout << "attempt to insert duplicate: " << *info << std::endl;
    delete node;
}
else if(*info < *(p->getInfo()))
    p->setLeft(node);
else
    p->setRight(node);
```

![[Pasted image 20240608212608.png]]
