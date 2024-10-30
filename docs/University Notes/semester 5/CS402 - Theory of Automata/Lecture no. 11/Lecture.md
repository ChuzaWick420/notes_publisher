---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-10-26
---

<span style="color: gray;">Dated: 26-10-2024</span>

# Lecture No. 11

Let's prove the _2nd_ statement of `kleene's theorem`.[^1]  
To prove that a `transition graph`[^2] can represent a `regular expression`,[^3] we will develop an `algorithm` which converts the `transition graph`[^2] into `generalized transition graph`[^4]  
The `transition graph`[^4] we want to convert is the following.  
![[Pasted image 20241026193435.png]]  

## Step 1

If a `transition graph`[^2] has more than one `initial states` then make _one_ `initial state`, connecting the old `initial states`.  
![[Pasted image 20241026194130.png]]

## Step 2

Repeat the [step 1](#step-1) but for `final states`.  
![[Pasted image 20241026194524.png]]

## Step 3

If there are 2 `states` connected with more than one `transition edges`, including the loops, convert these edges into one edge.

![[Pasted image 20241026195119.png]]  
this can be converted into  
![[Pasted image 20241026195247.png]]  
This works with any number of `transition edges`.

## Step 4

If 3 `states` are connected in a sequence, then we can skip the middle `state`.  
Connecting the first `state` with the last one with the `transition edge` labeled as the concatenation of the `regular expressions`[^3] of all the edges.

![[Pasted image 20241026195751.png]]  
can be converted into  
![[Pasted image 20241026195913.png]]

## Example

![[Pasted image 20241026200811.png]]  
Can be converted into  
![[Pasted image 20241026201046.png]]

## Example

![[Pasted image 20241026203527.png]]  
This can be converted into  
![[Pasted image 20241026203921.png]]  
Which can further be converted to  
![[Pasted image 20241026204104.png]]

## References

[^1]: Read more about [[semester 5/CS402 - Theory of Automata/Lecture no. 10/Lecture|kleene's theorem]].
[^2]: Read more about [[semester 5/CS402 - Theory of Automata/Lecture no. 7/Lecture|transition graphs]].
[^3]: Read more about [[semester 5/CS402 - Theory of Automata/Lecture no. 3/Lecture|regular expressions]].
[^4]: Read more about [[semester 5/CS402 - Theory of Automata/Lecture no. 7/Lecture|transition graphs]].