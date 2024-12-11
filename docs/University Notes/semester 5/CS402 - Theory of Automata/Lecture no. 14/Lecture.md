---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-10-29
---

<span style="color: gray;">Dated: 29-10-2024</span>

# Lecture No. 14

## Closure of a `Finite Automaton`[^1]

It is concatenation of a `finite automaton`[^1] with itself.  
The `initial state` is also the `final state`.

### Example

$$r = (a + b)^* b$$

![[cs402_14_d_1.svg]]  

$$r^* = ((a + b)^* b)^*$$

![[cs402_14_d_2.svg]]

| Oldstate                  | New state after reading |                         |
| ------------------------- | ----------------------- | ----------------------- |
|                           | a                       | b                       |
| $z_1^\pm \equiv x_1$      | $x_1 \equiv z_2$        | $(x_2, x_1) \equiv z_3$ |
| $z_2 \equiv x_1$          | $x_1 \equiv z_2$        | $(x_2, x_1) \equiv z_3$ |
| $z_3^+ \equiv (x_2, x_1)$ | $x_1 \equiv z_2$        | $(x_2, x_1) \equiv z_3$ |

![[cs402_14_d_3.svg]]

### Example

$$r = (a+b)^*aa(a + b)^*$$

![[cs402_14_d_4.svg]]

| Old States                     | New States after reading     |                         |
| ------------------------------ | ---------------------------- | ----------------------- |
|                                | a                            | b                       |
| $z_1^\pm \equiv y_1$           | $y_2 \equiv z_3$             | $y_1 \equiv z_2$        |
| $z_2 \equiv y_1$               | $y_2 \equiv z_3$             | $y_1 \equiv z_2$        |
| $z_3 \equiv y_2$               | $(y_3, y_1) \equiv z_4$      | $y_1 \equiv z_2$        |
| $z_4^+ \equiv (y_3, y_1)$      | $(y_3, y_1, y_2) \equiv z_5$ | $(y_3, y_1) \equiv z_4$ |
| $z_5^+ \equiv (y_3, y_1, y_2)$ | $(y_3, y_1, y_2) \equiv z_5$ | $(y_3, y_1) \equiv z_4$ |

![[cs402_14_d_5.svg]]

## References

[^1]: Read more about [[CS402_03|finite automaton]].