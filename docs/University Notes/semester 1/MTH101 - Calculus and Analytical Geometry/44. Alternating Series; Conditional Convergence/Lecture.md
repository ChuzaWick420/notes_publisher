---
tags:
  - university-notes
  - series
  - "sigma"
university-name: Virtual University of Pakistan
---

# Alternating `Series`[^1] and Conditional Convergence
## Alternating `Series`[^1]
The `series`[^1] of the form  

$$\sum_{k=1}^{\infty}(-1)^{k+1}a_{k}=a_{1}-a_{2}+a_{3}-a_{4}+\ldots$$

$$\sum_{k=1}^{\infty}(-1)^{k}a_{k}=a_{1}-a_{2}+a_{3}-a_{4}+\ldots$$

Are called `alternating series`.

## Alternating Series Test
The `alternating series` _converges_ if the following 2 conditions are satisfied

1. $$a_1 > a_2 > \ldots > a_i > \ldots$$

2. $$\lim_{i \to +\infty} a_i = 0$$

## Theorem
If an `alternating series` satisfies the [alternating series test](#alternating-series-test) and the `sum`[^2] is approximated by $n^{th}$ partial `sum`[^2] $S_n$, thereby resulting in an error of $S - S_n$ then  

$$\lvert S - S_n \rvert < a_{n + 1}$$

The sign of the error is same as the coefficient of $a_{n+1}$.

### Example
Assume an `alternating series`  

$$\sum_{i = 1}^{\infty} (-1)^{i + 1} \frac 1 i$$

This `alternating series` satisfies the conditions of [alternating series test](#alternating-series-test) which implies that it _converges_ which further implies that it has a `sum`[^2] $S$ which must lie between 2 successive partial `sums`[^2].  

$$S_{7}=1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\frac{1}{5}-\frac{1}{6}+\frac{1}{7}=\frac{319}{420}$$

$$S_{8}=1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\frac{1}{5}-\frac{1}{6}+\frac{1}{7}-\frac{1}{8}=\frac{533}{840}$$

$$S_7 < S < S_8$$

We can arbitrarily choose $S = \ln (2)$ because it satisfies the `inequality`[^3].  

$$\lvert \ln 2-S_{7}\rvert = \lvert \ln 2-\frac{319}{420}\rvert <a_{8}=\frac{1}{8}$$

$$\lvert \ln 2-S_{8}\rvert = \lvert \ln 2-\frac{533}{840}\rvert<a_{9}=\frac{1}{9}$$

## Absolute Convergence
A `series`[^1]  

$$\sum_{i=1}^{\infty}u_{i}=u_{1}+u_{2}+ \ldots +u_{i}+ \ldots$$

is said to _converge_ absolutely if the `series`[^1] of its `absolute values`[^4] _converges_.  

$$\sum_{i=1}^{\infty}\lvert u_{i}\rvert=\lvert u_{1}\rvert+\lvert u_{2}\rvert+\ldots+\lvert u_{i}\rvert+\ldots$$

## Conditional Convergence
Imagine a `series`[^1] like 

$$\sum_{i = 1}^{\infty} (-1)^{i + 1} \frac 1 i = 1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\ldots+(-1)^{i+1}\frac{1}{i}+\ldots$$

Which _converges_ but the following `series`[^1] _diverges_  

$$\sum_{i = 1}^{\infty}\lvert (-1)^{i + 1} \frac 1 i \rvert = 1+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+\ldots+(-1)^{i+1}\frac{1}{i}+\ldots$$
  
Hence, it is not `absolutely convergent`.  
Such a `series`[^1] is called `conditionally convergent`.

## Reference

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/42. Infinite Series/Lecture|series]].
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/27. Sigma Notation/Lecture|sum]].
[^3]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/1. Coordinates, Graphs, Lines/Lecture|inequalities]].
[^4]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/2. Absolute Value/Lecture|absolute values]].
