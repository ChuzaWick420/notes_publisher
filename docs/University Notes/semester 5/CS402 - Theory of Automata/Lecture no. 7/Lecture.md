---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

<span style="color: gray;">Dated: 26-10-2024</span>

# Lecture No. 7

## Finite Automata Corresponding to Finite Languages

Consider $L = \{\Lambda, b, ab, bb\}$ which can be defined as $(\Lambda + b + ab + bb)$ or $(\Lambda + (\Lambda + a + b)b)$  
![[Pasted image 20241026121116.png]]  
Notice the connection between the `transition diagram` and the `regular expression`?[^1]  
$\Lambda$ suggests that the `initial state` is the `final state` at the same time.  
The right most $b$ in $(\Lambda + a + b)b$ suggest that every other `final state` ends by $b$.  
The number of `final states` is equal to the number of `strings` in the $L$.

There are some `states` here which are $x$ and $y$ and are called:

- Dead `States`
- Waste Baskets
- Davey John Lockers

## Example

$$L = \{w \in \{a, b\}^* : \text{length}(w) \ge 2, w \text{ ends with neither } aa \text{ or } bb\}$$

$$(a + b)^*(ab + ba)$$

![[Pasted image 20241026122607.png]]

## Example

$$L = \{w \in \{a, b\}^* : w \text{ does not ends with } aa\}$$

$$\Lambda + a + b + (a + b)^*(ab + ba + bb)$$

![[Pasted image 20241026123704.png]]

## Transition Graph

It is a collection of following:

- Finite number of `states` one of which is `initial state` and some or none being `final state`.
- Finite `set`[^2] of input `letters` from which `strings`[^3] are formed.
- Finite `set`[^2] of transitions that show how to transition from one `state` to another, based on substrings of input letters, possibly even `null string` $\Lambda$.

## References

[^1]: Read more about [[semester 5/CS402 - Theory of Automata/Lecture no. 3/Lecture|regular expressions]].
[^2]: Read more about [[Mathematics/Set/Content|sets]].
[^3]: Read more about [[semester 5/CS402 - Theory of Automata/Lecture no. 1/Lecture|strings.]]