---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Expression Tree
![[Pasted image 20240802010329.png]]  
Take this tree for example, the `inorder transversal` gives us the #infix form.  
The `postfix transversal` gives us `postfix` form: `a b c * + d e * f + g * +`

We can also create the tree from a #stack.

![[Pasted image 20240802010804.png]]

As soon as `+` is encountered:  
![[Pasted image 20240802010830.png]]

Then we keep scanning the operands as such:  
![[Pasted image 20240802010901.png]]  
And we pop the elements as such  
![[Pasted image 20240802010918.png]]

![[Pasted image 20240802010952.png]]

![[Pasted image 20240802011013.png]]

# Huffman Encoding
This is a compression technique
1. List all characters including `space` characters along with their frequency in the string.
2. Consider each of these characters as a `node`.
3. Pick the two `nodes` with lowest frequency, if their frequency is equal then pick any.
4. Combine the frequencies of two `nodes` with equal frequencies into a parent `node`.

## Example
String: "traversing threaded binary trees"  
size: 33 characters (including `space` and `newline`)

| Letters | Frequency |
| ------- | --------- |
| NL      | 1         |
| SP      | 3         |
| a       | 3         |
| b       | 1         |
| d       | 2         |
| e       | 5         |
| g       | 1         |
| h       | 1         |

![[Pasted image 20240802012218.png]]
