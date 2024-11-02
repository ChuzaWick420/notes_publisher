---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-02
---

<span style="color: gray;">Dated: 02-11-2024</span>

# Lecture No. 17

## Method 3

In a `non deterministic finite automaton`,[^1] for a `letter`, there may be no `transition` at all or multiple `transitions`.  
The corresponding `finite automaton`[^2] can be represented as having `empty state` and having combination of `states`.

### Example

Consider the `non deterministic finite automaton`[^1] which accepts the `language` containing the `string`[^3] $bb$.  
![[cs402_17_d_1.svg]]

| Old States                     | New Starts After Reading                   |                              |
| ------------------------------ | ------------------------------------------ | ---------------------------- |
|                                | a                                          | b                            |
| $z_1^- \equiv x_1$             | $x_1 \equiv z_1$                           | $(x_1, x_2) \equiv z_2$      |
| $z_2 \equiv (x_1, x_2)$        | $(x_1, \varnothing) \equiv x_1 \equiv z_1$ | $(x_1, x_2, x_3) \equiv z_3$ |
| $z_3^+ \equiv (x_1, x_2, x_3)$ | $(x_1, x_3) \equiv z_4$                    | $(x_1, x_2, x_3) \equiv z_3$ |
| $z_4^+ \equiv (x_1, x_3)$      | $(x_1, x_3) \equiv z_4$                    | $(x_1, x_2, x_3) \equiv z_3$ |

![[cs402_17_d_2.svg]]

## `Non Deterministic Finite Automaton`[^1] And `Kleene's Theorem`[^4]

The `non deterministic finite automaton`[^1] can help proving the 3rd part of `kleene's theorem`[^4]  
There are 2 methods for this

## Method 1

### Example

$$L_1 = \{a\}, L_2=\{b\}, L_3=\{\Lambda\}$$

#### $NFA_1$

![[cs402_17_d_3.svg]]

#### $NFA_2$

![[cs402_17_d_4.svg]]

#### $NFA_3$

![[cs402_17_d_5.svg]]

#### $FA_1$

![[cs402_17_d_6.svg]]

#### $FA_2$

![[cs402_17_d_7.svg]]

#### $FA_3$

![[cs402_17_d_8.svg]]

## Method 2

### Example

#### $FA_1$

![[cs402_17_d_9.svg]]

#### $FA_2$

![[cs402_17_d_10.svg]]

#### `Non Deterministic Finite Automaton`[^1] Corresponding to $FA_1 \cup FA_2$

![[cs402_17_d_11.svg]]

## References

[^1]: Read more about [[semester 5/CS402 - Theory of Automata/Lecture no. 15/Lecture|non deterministic finite automaton]].
[^2]: Read more about [[semester 5/CS402 - Theory of Automata/Lecture no. 4/Lecture|finite automaton]].
[^3]: Read more about [[notes_publisher/docs/University Notes/semester 5/CS402 - Theory of Automata/Lecture no. 1/Lecture|strings]].
[^4]: Read more about [[semester 5/CS402 - Theory of Automata/Lecture no. 10/Lecture|kleene's theorems]].