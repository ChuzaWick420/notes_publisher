---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

<span style="color: gray;">Dated: 25-10-2024</span>

# Lecture No. 6

## Example

Consider a `language` $L$ of `strings`[^1] such that each one starts and ends with a different `letter`.  

$$a (a + b)^* b + b (a + b)^* a$$

![[Pasted image 20241025233143.png]]

## Equivalent Finite Automaton

Two `finite automata`[^2] which accept the same language are called `equivalent finite automata`.  
The following 3 `finite automata` are `equivalent`.  
![[Pasted image 20241025233822.png]]  
![[Pasted image 20241025234036.png]]  
![[Pasted image 20241025234122.png]]  
The inputs for these would be $\Phi$ or $\{\}$ because there is no `final state`.  
Even if there is, it is impossible to reach.

## Example

A `language` $L$ defined over $\Sigma = \{a, b\}$ consisting of `strings`[^1] having either triple $a$ or $b$.  

$$(a + b)^*(aaa + bbb)(a + b)^*$$

![[Pasted image 20241026003147.png]]

## References

[^1]: Read more about [[semester 5/CS402 - Theory of Automata/Lecture no. 1/Lecture|strings]].
[^2]: Read more about [[semester 5/CS402 - Theory of Automata/Lecture no. 4/Lecture|finite automaton]].