---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Level Order Traversal
![[Pasted image 20240621161320.png]]

```cpp
void levelorder( TreeNode <int> * treeNode ) {
	Queue <TreeNode<int> *> q;
	
	if(treeNode == NULL) return;
	
	q.enqueue(treeNode);
	
	while(!q.empty()) {
		treeNode = q.dequeue();
		cout << *(treeNode->getInfo()) << " ";
		
		if(treeNode->getLeft() != NULL)
			q.enqueue(treeNode->getLeft());
			
		if(treeNode->getRight() != NULL)
			q.enqueue(treeNode->getRight());
	}
	
	cout << endl;
}
```

# Binary Search Tree with Strings

```cpp
void wordTree() {
	TreeNode<char> * root = new TreeNode<char>();
	
	static char * word[] = {"babble", "fable", "jacket",
	"backup", "eagle","daily","gain","bandit","abandon",
	"abash","accuse","economy","adhere","advise","cease",
	"debunk","feeder","genius","fetch","chain", NULL};
	
	root->setInfo(word[0]);
	
	for(i = 1; word[i]; i++)
		insert(root, word[i]);
		
	inorder(root);
	cout << endl;
}
```

```cpp
void insert(TreeNode<char> * root, char * info) {
	TreeNode<char> * node = new TreeNode<char>(info);
	TreeNode<char> *p, *q;
	p = q = root;
	
	while(strcmp(info, p->getInfo()) != 0 && q != NULL ) {
		p = q;
		
		if( strcmp(info, p->getInfo()) < 0 )
			q = p->getLeft();
			
		else
			q = p->getRight();
	}
	
	if(strcmp(info, p->getInfo()) == 0) {
		cout << "attempt to insert duplicate: " << * info << endl;
		delete node;
	}
	
	else if(strcmp(info, p->getInfo()) < 0)
		p->setLeft(node);
		
	else
		p->setRight(node);
}
```

# Deleting a Node from BST
There are 2 cases while deleting `nodes` from the #binary-search-tree:
1. The `node` is a `leaf node`.
	1. ![[Pasted image 20240622130113.png]]
2. The `node` is not a `leaf node` and has only one _subtree_.
	1. ![[Pasted image 20240622130138.png]]
3. The `node` is not a `leaf node` and has both _subtrees_.
	1. ![[Pasted image 20240622131809.png]]

For _2nd_ case, the `parent node` of the `node` to be deleted, has to be re-adjusted to point to the `inorder` successor of the `node` to be deleted.  
![[Pasted image 20240622131535.png]]

For _3rd_ case, assume we want to delete the `node` with value `2`.  
Firstly, we find the _left_ most `node` of the _right subtree_.  
Copy its contents into the `node` to be deleted.  
Then do the procedure used in _2nd_ case.  
![[Pasted image 20240622134643.png]]  
![[Pasted image 20240622134659.png]]
