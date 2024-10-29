---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

<span style="color: gray;">Dated: 29-10-2024</span>

# Lecture No. 13

## Concatenation of Two `Finite Automaton`[^1]

### Example

$$r_1 = (a + b)^* b$$

$$r_2 = (a + b)^* aa (a + b)^*$$

#### $r_1$

![[cs402_13_d_1.svg]]

#### $r_2$

![[cs402_13_d_2.svg]]

#### $r_1r_2$

For the `finite automaton`[^1] of $r_1r_2$, the `initial state` should correspond to that of $r_1$ and `final state` with $r_2$.  
In a sense, the `final state` of $r_1$ _is_ the `initial state` of $r_2$.

| Old States                     | New States after reading     |                              |
| ------------------------------ | ---------------------------- | ---------------------------- |
|                                | a                            | b                            |
| $z_1^- \equiv x_1$             | $x_1 \equiv z_1$             | $(x_2, y_1) \equiv z_2$      |
| $z_2 \equiv (x_2, y_1)$        | $(x_1, y_2) \equiv z_3$      | $(x_2, y_1) \equiv z_2$      |
| $z_3 \equiv (x_1, y_2)$        | $(x_1, y_3) \equiv z_4$      | $(x_2, y_1) \equiv z_2$      |
| $z_4^+ \equiv (x_1, y_3)$      | $(x_1, y_3) \equiv z_4$      | $(x_2, y_1, y_3) \equiv z_5$ |
| $z_5^+ \equiv (x_2, y_1, y_3)$ | $(x_1, y_2, y_3) \equiv z_6$ | $(x_2, y_1, y_3) \equiv z_5$ |
| $z_6^+ \equiv (x_1, y_2, y_3)$ | $(x_1, y_3) \equiv z_4$      | $(x_2, y_1, y_3) \equiv z_5$ |  

![[cs402_13_d_3.svg]]

## References

[^1]: Read more about [[semester 5/CS402 - Theory of Automata/Lecture no. 4/Lecture|finite automaton]].