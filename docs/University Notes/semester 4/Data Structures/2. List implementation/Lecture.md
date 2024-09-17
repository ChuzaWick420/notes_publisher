---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Boundary Conditions
Imagine we have an array of 100 elements and `current` pointer is pointing to the last element.  
Now if we use `next()`, it will throw an error.  
Now imagine if the `current` pointer is at first element.  
Now if we use `back()`, it will throw an error.

# remove()
Imagine a list `(2, 4, 6, 8)` and `current` pointer is set to `3` (points to `6`).  
`remove()` is called.  
element `6` is deleted, leaving an empty space.  
elements on the right side of `current` pointer are shifted towards left.

`(2, 4, 6, 8)`  
`(2, 4, , 8)`  
`(2, 4, 8, )`

# find(X)

```cpp
int find (int value) {
	//loops through the list
	int index;
	for (index = 1; index < size + 1; index++) {
		if (list_name[index] == value)
			break;
	}

	//index now stores where the value is
	//if the whole list was not searched, that means element was found
	//move the current pointer to that location and return true
	if (index < size + 1) {
		current = index;
		return 1;
	}

	//otherwise return false
	return 0;
}
```

# Time Complexity
Imagine we have a list of `1000` elements. 

## Worst case
- `add()`: beginning of the list since everything needs to be shifted to the left to make room for _added_ element.
- `remove()`: beginning of the list since everything needs to be shifted to right to fill in the gap left by the _removed_ element.
- `find()`: end of the list since the whole list has to be searched.

## Best case
vise versa.

# Linked List
A linked list consists of dynamically allocated `nodes`.  
Each `node` has 2 parts:
1. `object`: the information it stores.
2. `next`: pointer to the next `node`.

There are 2 special pointers as well:
1. `head`: points the the first `node`.
2. `current`: points to the current `node`.
