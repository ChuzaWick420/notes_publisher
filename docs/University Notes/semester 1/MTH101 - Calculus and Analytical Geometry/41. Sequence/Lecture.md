---
tags:
  - university-notes
  - sequences
  - "limits"
university-name: Virtual University of Pakistan
---

# Sequences and Monotone Sequences
## Definition of a Sequence
A `sequence` is a succession of `numbers`.

### Example

$$1, 2, 3, \ldots$$

Each `number` is called `term` of the `sequence`.  
Each `term` has a _positional_ name as well such as `1st term`, `2nd term` etc.  
We write them as  

$$a_1, a_2, \ldots$$

### Example

Let us say we have a `sequence` $$2, 4, 6, \ldots$$

Then we can also write it as  

$$\{2^n\}^{+\infty}_{n = 1}$$

### Generalized
Therefore, we can write a `sequence` of the form $a_1, a_2, \ldots$ as  

$$\{a_n\}^{+\infty}_{n = 1}$$

## Formal Definition
A `sequence` or a `infinite sequence` is a `function`[^1] whose domain is a `set`[^2] of `positive integers` ($\mathbb{Z^+}$).  
We have 2 notations for this

- $$\{a_n\}_{n = 1}^{+\infty}$$

- $$f(n) = a_n; n \in \mathbb{Z^+}$$

## Graphs of Sequences
Imagine we have $f(x) = x^2$  
Then if the `domain`[^1] is $x \in \{\mathbb{R^+} + \{0\}\}$ then the graph would look something like  
![[Pasted image 20240930165630.png]]  
But if the `domain` is $x \in \{\mathbb{Z}^+ + \{0\}\}$ then graph would be  
![[Pasted image 20240930165957.png]]

> These graphs only are captured inside the `interval`[^3] $[0, 2]$

## `Limits`[^4] For Sequence
A `sequence` $\{a_n\}$ is said to _converge_ to the `limit`[^4] $L$ if given any $\epsilon > 0$ there is $N$ such that $\lvert a_n - L\rvert < \epsilon$ for $n \ge N$.  
In this case we write  

$$\lim_{n \to + \infty} a_n = L$$

A `sequence` which does not _converge_ is said to _diverge_.

### Geometric Intuition
![[Pasted image 20240930171329.png]]  
After $n > 5$, our values start to approach $L$.

## Theorems

- $$\lim_{n \to +\infty} c = c$$

- $$\lim_{n \to +\infty}c a_n = c \lim_{n \to +\infty} a_n= c L_1$$

- $$\lim_{n \to +\infty} (a_n + b_n) = \lim_{n \to + \infty} a_n + \lim_{n \to +\infty} b_n = L_1 + L_2$$

- $$\lim_{n \to +\infty} (a_n - b_n) = \lim_{n \to + \infty} a_n - \lim_{n \to +\infty} b_n = L_1 - L_2$$

- $$\lim_{n \to +\infty} (a_n \cdot b_n) = \lim_{n \to + \infty} a_n \cdot \lim_{n \to +\infty} b_n = L_1 \cdot L_2$$

- $$\lim_{n \to +\infty}\left(\frac{a_n}{b_n}\right) = \frac{\lim_{n \to +\infty} a_n}{\lim_{n \to +\infty} b_n} = \frac{L_1}{L_2}$$

## References

[^1]: Read more about [[Mathematics/Function/Content|functions]].
[^2]: Read more about [[Mathematics/Set/Content|sets]].
[^3]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/1. Coordinates, Graphs, Lines/Lecture|interval]].
[^4]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/9. Limits (Intuitive Introduction)/Lecture|limits]].
