---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

- If certain operations are requested then a data structure which fulfils those operations the most, is the one to be selected.
- There are 3 things associated with a data structure:
	1. Storage for each data item.
	2. Time to perform basic operation.
	3. Programming effort to implement the data structure.
- The merit of two data structures can be judged by solving the same problem using those data structures and then comparing the task completion time.
- Sometimes you will find that their performances change depending on size of data.
- `lvalue` is the value which is on the _left_ side of the = operator.
- if `int x[5]` is an array then `x` is a constant and is not a valid `lvalue`.

# Lists
Lists can store elements with same data types.

| Operation Name | Description                                    |
| -------------- | ---------------------------------------------- |
| createList()   | Creates a new list                             |
| copy()         | Sets one list of be copy of another            |
| clear()        | Clear a list (removes all elements)            |
| insert(X, ?)   | insert element `X` at position `?` in the list |
| remove(?)      | remove element at `?` position in the list     |
| get(?)         | Get element at position `?`                    |
| update(X, ?)   | Replace element at `?` by `X`.                 |
| find(X)        | Determine if `X` is present in list            |
| length()       | returns the length of the list                 |

There are 2 approaches to pointing to certain elements.
1. using indexes.
2. using a `current` marker (a pointer which we can move back and forth and then perform following operations).

| Functions | Description                                           |
| --------- | ----------------------------------------------------- |
| start()   | Moves the “current” pointer to the very first element |
| tail()    | Moves the “current” pointer to the very last element  |
| next()    | Move the current position forward one element         |
| back()    | Move the current position backward one element        |
