---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Lecture No. 15

## Non Deterministic Finite Automaton

A `non deterministic finite automaton` is a `transition graph`[^1] with a unique `initial state` and single `letter` as label for transitions.  
It is a collection of following things:

- Finite many `states` with one `initial` and some `final states`.
- Finite `set`[^2] of input letters $\Sigma = \{a, b, c\}$.
- Finite `set`[^2] of transitions. $\Lambda$ is not a valid transition and there may be more than one transitions for a `letter` or no transitions at all.

It can be considered as an intermediate structure between `finite automaton`[^3] and `transition graph`[^1]

### Note

To remove a loop at a `state`, it is to be noted that the `finite automaton`[^3] may be converted to a `non deterministic finite automaton`, as a circuit.

The following `finite automaton`[^3]  
![[cs402_15_d_1.svg]]

can be converted into following `non deterministic finite automaton`.  
![[cs402_15_d_2.svg]]

## Converting a `Finite Automaton`[^3] into Equivalent `Non Deterministic Finite Automaton`

According to `Kleene's Theorem`,[^4] if a `language` is accepted by a `finite automaton`[^3] then there exists a `transition graph`[^1] which accepts that language as well.  
Since the `non deterministic finite automaton` is also a `transition graph`[^1] so the language accepted by the `finite automaton`[^3] is also accepted by the `non deterministic finite automaton`, which makes them equivalent.

$$r = (a + b)^*b$$

### `Finite Automaton`[^3]

![[cs402_15_d_3.svg]]

### `Non Deterministic Finite Automaton`

![[cs402_15_d_4.svg]]

## References

[^1]: Read more about [[semester 5/CS402 - Theory of Automata/Lecture no. 7/Lecture|transition graph]].
[^2]: Read more about [[Mathematics/Set/Content|sets]].
[^3]: Read more about [[University Notes/semester 5/CS402 - Theory of Automata/Lecture no. 4/Lecture|finite automaton]].
[^4]: Read more about [[semester 5/CS402 - Theory of Automata/Lecture no. 10/Lecture|Kleene's theorem]].