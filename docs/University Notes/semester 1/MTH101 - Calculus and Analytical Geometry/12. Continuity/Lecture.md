---
tags:
  - university-notes
  - function
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Continuity

## Continuity

There are 3 conditions for a `function`[^1] to be `continous` near $x= c$.

1. $f(c)$ is defined.

2. $$\lim_{x \rightarrow c^+} f(x) = \lim_{x \rightarrow c^-} f(x)$$

3. $$\lim_{x \rightarrow c} f(x) = f(c)$$

## Continuous Function

A `function`[^1] is called _continuous_ if it follows the rules of `continuity` over the interval $(-\infty, +\infty)$.

## Discontinuity

If a `function`[^1] violates any of the rules of _continuity_ at point $c$ then it is called _point of discontinuity_.

## Properties of Continuous Functions

if $f(x)$ and $g(x)$ are `continuous functions` then following functions are also _continuous_.

1. $f(x) + g(x)$
2. $f(x) - g(x)$
3. $f(x) \cdot g(x)$
4. $\frac{f(x)}{g(x)}$

We can prove these properties by looking at the theorems of `limits`[^2]

## Continuity of Composite Functions

1. If $\lim g(x) = L$ and $f(x)$ is _continuous_ at $x = L$ then $\lim{fog(x)} = f(L)$
2. If $g(x)$ is _continuous_ at $c$ and $f(x)$ is _continuous_ at $g(c)$ then $fog(x)$ is _continuous_ at $c$.

## Theorems

### Intermediate Value Theorem

![[Pasted image 20240814200819.png]]

If $f(x)$ is _continuous_ at the interval $[a, b]$ and there is a value $c$ between $f(a)$ and $f(b)$, inclusively, then there must be a value $x$ where $f(x) = c$.

## Another Theorem

![[Pasted image 20240814202000.png]]

If $f(x)$ is _continuous_ over the interval $[a, b]$ and $f(a)$ and $f(b)$ have opposite signs then there is at least one solution for $f(x) = 0$ in the interval $(a, b)$.

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[Mathematics/Function/Content|functions]].
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/10. Limits (Computational Techniques)/Lecture|limits]].