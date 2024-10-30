---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-10-26
---

<span style="color: gray;">Dated: 26-10-2024</span>

# Lecture No. 10

## Example

Consider a `language` $L$ defined over $\Sigma = \{a, b\}$ containing $aa$ or $bb$.  

$$(a+b)^*(aa + bb)(a + b)^*$$

![[Pasted image 20241026163451.png]]

## Non Determinism

It is possible that for a certain `string`,[^1] there may not be any path or there may be multiple paths.  
This causes `non determinism`.  
Though it can help differentiating between `finite automata`[^2] from `transition graphs`[^3] and `generalized transition graphs`[^4] since `finite automa`[^2] are also called `deterministic finite automata`.

## Kleene's Theorem

If a `language` can be represented by either

1. A `finite automaton`[^2]
2. A `transition graph`[^3]
3. A `regular expression`[^5]

Then it can be represented by other 2 as well.

This theorem can be proved by following arguments

1. If a `language` is represented by `finite automaton`[^2] then it can be represented by a `transition graph`[^3] as well since every `finite automaton`[^2] is a `transition graph`[^3]
2. If a `language` is represented by `transition graph`[^3] then it can be represented by a `regular expression`[^5] as well
3. If a `language` is represented by a `regular expression`[^5] then it can be represented by a `finite automaton`[^2] as well since it is also a `transition graph`[^3]

## References

[^1]: Read more about [[semester 5/CS402 - Theory of Automata/Lecture no. 1/Lecture|strings]].
[^2]: Read more about [[semester 5/CS402 - Theory of Automata/Lecture no. 4/Lecture|finite automata]].
[^3]: Read more about [[semester 5/CS402 - Theory of Automata/Lecture no. 7/Lecture|transition graph]].
[^4]: Read more about [[notes_publisher/docs/University Notes/semester 5/CS402 - Theory of Automata/Lecture no. 9/Lecture|generalized transition graph]].
[^5]: Read more about [[semester 5/CS402 - Theory of Automata/Lecture no. 3/Lecture|regular expressions]].