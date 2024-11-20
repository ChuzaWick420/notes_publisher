---
tags:
  - university-notes
  - sigma
  - series
  - function
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Infinite Series

## Definition

An `infinite series` is an expansion that can be written in the form  

$$\sum_{i = 1}^{\infty} u_i = u_1 + u_2  + \ldots$$

The $u_1$ and $u_2$ etc are called the `terms` of the `series`.

## Example

Imagine we have $0.333\ldots$  
Then we can re-write it as follows  

$$0.3 + 0.03 + 0.003 + \ldots$$

$$\frac{3}{10} + \frac{3}{10^2} + \frac{3}{10^3} + \ldots$$

We do know that $\frac 1 3 = 0.333\ldots$  
Therefore, this `series` should _converge_ to $\frac 1 3$.  

$$s_1 = \frac{3}{10} = 0.3$$

$$s_2 = \frac{3}{10} + \frac{3}{10^2} = 0.33$$

$$s_3 = \frac{3}{10} + \frac{3}{10^2} + \frac{3}{10^3} = 0.333$$

This means that as we keep adding more and more `terms`, our approximation gets more and more close to the actual answer.  
Therefore, we would just need `sum`[^1] of some finite $n$ values and our approximation should be good enough.  

$$S_n = \frac{3}{10} + \frac{3}{10^2} + \frac{3}{10^3} + \cdots + \frac{3}{10^n}$$

Applying `limit`,[^2] we get  

$$\lim_{n\rightarrow+\infty}S_{n}=\lim_{n\rightarrow+\infty}\left(\frac{3}{10}+\frac{3}{10^{2}}+\frac{3}{10^{3}}+\cdots+\frac{3}{10^{n}}\right)$$

Dividing by $10$, we get  

$$\frac{1}{10}S_n = \frac{3}{10^2} + \frac{3}{10^3} + \cdots + \frac{3}{10^n} + \frac{3}{10^{n+1}}$$

Subtracting the original from this new `series`, we get  

$$S_n - \frac{1}{10}S_n = \frac{3}{10} - \frac{3}{10^{n+1}}$$

$$\frac{9}{10}S_n = \frac{3}{10}\left(1 - \frac{1}{10^n}\right)$$

$$S_n = \frac{1}{3}\left(1 - \frac{1}{10^n}\right)$$

$$\because n \to +\infty \implies \frac{1}{10^n} \to 0$$

$$\lim_{n\rightarrow+\infty}S_n = \lim_{n\rightarrow+\infty}\frac{1}{3}\left(1 - \frac{1}{10^n}\right) = \frac{1}{3}$$

## Formal Definition

If $S_n$ is the `sequence`[^3] of partial `sums` of the `series` $u_1 + u_2 + \ldots u_i + \ldots$ and _converges_ to a `limit`[^2] $S$ then it is called the `sum`[^1] of `series`.  

$$S = \sum_{i = 1}^{\infty} u_i$$

However if the `sequence` _diverges_ then the `series` is said to _diverge_ and it has no `sum`.[^1]

## Geometric Series

A `series` in which each `term` is a result of previous `term` being multiplied to a `constant`, is called `geometric series`.  

$$a + ar + ar^2 + \ldots + ar^{i - 1} + \ldots$$

### Theorem

This `series` _converges_ if $\lvert r \rvert < 1$ and _diverges_ if $\lvert r \rvert > 1$  
If the `series` _converges_ then the `sum`[^1] is  

$$\frac {a}{1 - r}$$

## Harmonic Series

A `series` of the form  

$$\sum_{i=1}^{\infty}\frac{1}{i}=1+\frac{1}{2}+\frac{1}{3}+\cdots$$

is called `harmonic series`.

## Divergence Test

1. If $\lim_{n \to +\infty} u_n \ne 0$ then the `series` $\sum u_n$ _diverges_.
2. If $\lim_{n \to +\infty} u_n = 0$ then the `series` $\sum u_n$ either _converges_ or _diverges_.

## Properties

1. If the $\sum u_i$ and $\sum v_i$ are _convergent_ `series` then the following are also _convergent_

	- $$\sum_{i=1}^{\infty}(u_{i}+v_{i})=\sum_{i=1}^{\infty}u_{i}+\sum_{i=1}^{\infty}v_{i}$$

	- $$\sum_{i=1}^{\infty}(u_{i}-v_{i})=\sum_{i=1}^{\infty}u_{i}-\sum_{i=1}^{\infty}v_{i}$$

2. If $c$ is a `constant` then both `series`, $\sum u_i$ and $\sum c \cdot u_i$ both either _converge_ or _diverge_. In case of _convergence_, we get $$\sum_{i=1}^{\infty}c \cdot u_{i}=c\sum_{i=1}^{\infty}u_{i}$$

3. _Convergence_ and _Divergence_ are unaffected if we delete arbitrary amount of terms from the `series`. That is to say that following both `series` will not have their _convergence_ or _divergence_ affected

	 - $$\sum_{i=1}^{\infty}u_{i}=u_{1}+u_{2}+u_{3}+\cdots$$

	 - $$\sum_{i=K}^{\infty}u_{i}=u_{K}+u_{K+1}+u_{K+2}+\cdots$$

## Integral Test

If $f(x)$ is a `decreasing`[^4] `continuous function`[^5] defined over the `interval`[^6] $[a, +\infty]$ then  

$$\sum_{i = 1}^{\infty} u_i$$

$$\int_a^{\infty} f(x) dx$$

Both either _converge_ or _diverge_.

## Hyper Harmonic or P-series

The `series` of the form  

$$\sum_{i=1}^{\infty}\frac{1}{i^{p}}=1+\frac{1}{2^{p}}+\frac{1}{3^{p}}+\cdots$$

where $p > 0$, is called `hyper harmonic` or `p series`.  
If $p > 1$, the `series` _converges_.  
If $0 < p \le 1$, then `series` _diverges_.

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/9. Limits (Intuitive Introduction)/Lecture|limits]].
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/41. Sequence/Lecture|sequences]].
[^3]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/27. Sigma Notation/Lecture|sum]].
[^4]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/21. Applications of Differentiation/Lecture|decreasing functions]].
[^5]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/12. Continuity/Lecture|continuity]].
[^6]: Read more about [[1. Coordinates, Graphs, Lines|intervals]].