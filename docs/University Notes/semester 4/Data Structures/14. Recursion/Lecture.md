---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Recursive Calls
When a #function calls another #function, the parameters, local variables and return address is stored on the #call-stack and the control is passed to the #function which is called.  
Once the called #function returns, the return address stored in the #call-stack is used to return back to the calling #function.

# Non Recursive Traversal

```cpp
void inorder(TreeNode<int>* root) {
	
	Stack<TreeNode<int>* > stack;
	TreeNode<int>* p;
	p = root;
	
	do {
		while( p != NULL ) {
			stack.push(p);
			p = p->getLeft();
		}
		
		// at this point, left tree is empty
		if(!stack.empty()) {
			p = stack.pop();
			cout << *(p->getInfo()) << " ";
			
			// go back & traverse right subtree
			p = p->getRight();
		}
		
	} while (!stack.empty() || p != NULL);
}
```

# Traversal Trace
