---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-10-29
---

<span style="color: gray;">Dated: 29-10-2024</span>

# Lecture No. 12

## Example

![[cs402_12_d_1.svg]]  
![[cs402_12_d_2.svg]]  
![[cs402_12_d_3.svg]]  
![[cs402_12_d_4.svg]]  
![[cs402_12_d_5.svg]]  
![[cs402_12_d_6.svg]]  
![[cs402_12_d_7.svg]]

## Kleene's Theorem part 3

If the language can be expressed by a `regular expression`[^1] then there exists an `finite automaton`[^2] accepting the language.

### Union of Two `Finite Automata`[^2]

Imagine you are given 2 `regular expressions`[^1] $r_1$ and $r_2$ then it is possible to make a `finite automaton`[^2] using $r_1 + r_2$.

#### Example

$$r_1 = (a + b)^*b$$

$$r_2 = (a + b)^* aa (a + b)^*$$

##### $r_1$

![[cs402_12_d_8.svg]]

##### $r_2$

![[cs402_12_d_9.svg]]

##### $r_1 + r_2$

The corresponding `finite automaton`[^2] will have `initial state` which matches the `initial state` of both previous `finite automata`.[^2]  
Same goes for the `final state`.  

$$r_1 + r_2 = (a + b)^*b + (a + b)^* aa (a + b)^*$$

![[cs402_12_d_10.svg]]

## References

[^1]: Read more about [[semester 5/CS402 - Theory of Automata/Lecture no. 3/Lecture|regular expression]].
[^2]: Read more about [[semester 5/CS402 - Theory of Automata/Lecture no. 4/Lecture|finite automaton]].