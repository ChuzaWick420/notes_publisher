---
tags:
  - university-notes
  - series
  - sigma
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

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

This `alternating series` satisfies the conditions of [alternating series test](#alternating-series-test) which implies that it _converges_ which further implies that it has a `sum`[^2] $S$ which must lie between 2 successive partial `sums`.[^2]  

$$S_{7}=1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\frac{1}{5}-\frac{1}{6}+\frac{1}{7}=\frac{319}{420}$$

$$S_{8}=1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\frac{1}{5}-\frac{1}{6}+\frac{1}{7}-\frac{1}{8}=\frac{533}{840}$$

$$S_7 < S < S_8$$

We can arbitrarily choose $S = \ln (2)$ because it satisfies the `inequality`.[^3]  

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

## Ratio Test for Absolute Convergence

Suppose that $\sum u_i$ be a `series`[^1] with `non zero terms` and  

$$p=\lim_{i\rightarrow\infty}\frac{\lvert u_{i+1}\rvert}{\lvert u_{i}\rvert}$$

Then if

1. $p < 1$, then $\sum u_i$ _converges_ absolutely.
2. $p > 1$, then $\sum u_i$ _diverges_.
3. $p = 1$, no conclusion can be drawn about _convergence_ or `absolute convergence`.

## Power Series in $x$

If $c_0, c_1$ etc are `constants` and $x$ is a `variable` then the `series`[^1] of the form

$$\sum_{i=0}^{\infty}c_{i}x^{i}=c_{0}+c_{1}x+c_{2}x^{2}+\ldots+c_{i}x^{i}+\ldots$$

is called `power series`.

### Theorem

For `power series`, exactly one of the following is true

1. The `series`[^1] _converges_ only for $x = 0$
2. The `series`[^1] _converges_ absolutely for all real values of $x$.
3. The `series`[^1] _converges_ absolutely for all $x$ in some finite `open interval`[^5] $(-R, R)$, _diverges_ if $x < -R$ or $x > R$ and at $x = -R, R$, can either
	1. converge
	2. converge absolutely
	3. diverge

## Radius and Interval of Convergence

The set of values of $x$ where the `power series` _converges_ is always an `interval`[^5] centered at $0$.  
This `interval`[^5] is called `interval of convergence`.  
Corresponding to which, the `series` has `radius` called `radius of convergence`.

### Example

Find `interval of convergence` and `radius of convergence` of the following `power series`  

$$\sum_{i = 1}^{\infty} x ^i$$

#### Solution

Applying the `ratio test`  

$$p=\lim_{i\rightarrow\infty}\frac{\lvert u_{i+1}\rvert}{\lvert u_{i}\rvert}$$

$$=\lim_{i\rightarrow\infty}\frac{\lvert {x^{i + 1}}\rvert}{\lvert x^{i}\rvert}$$

$$= \lim_{i \to \infty} \lvert x \rvert = \lvert x \rvert$$

So the `ratio test` implies that the `series`[^1] would _converge_ absolutely if $p = \lvert x \rvert < 1$ and would _diverge_ if $p = \lvert x \rvert > 1$  
Since $\lvert x \rvert = 1$ means either $x = 1$ or $x = -1$. Therefore, we have to check the `convergence` at both points.

##### $x = 1$

$$\sum_{k=0}^{\infty}1^{k}=1+1+1+\ldots$$

##### $x = -1$

$$\sum_{k=0}^{\infty}(-1)^{k}=1-1+1-1+\ldots$$

Both of these _diverge_. Therefore, the `interval of convergence` is $(-1, 1)$ and the `radius of convergence` is $R = 1$.

## Power Series in $x - a$

$$\sum_{i=0}^{\infty}c_{i}(x-a)^{i}=c_{0}+c_{1}(x-a)+c_{2}(x-a)^{2}+\ldots+c_{i}(x-a)^{i}+\ldots$$

### Theorem

For any `power series` of the form  

$$\sum c_{i}(x-a)^{i}$$

exactly one of the following is true

1. The `series`[^1] _converges_ only for $x = a$
2. The `series`[^1] _converges_ absolutely for all real values of $x$.
3. The `series`[^1] _converges_ absolutely for all $x$ in some `open interval`[^5] $(a - R, a + R)$, _diverges_ if $x < a - R$ or $x > a + R$ and at $x = a \pm R$, may
	1. converge
	2. converge absolutely
	3. diverge

The `interval of convergence` is centered at $x = a$.

## Reference

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/42. Infinite Series/Lecture|series]].
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/27. Sigma Notation/Lecture|sum]].
[^3]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/1. Coordinates, Graphs, Lines/Lecture|inequalities]].
[^4]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/2. Absolute Value/Lecture|absolute values]].
[^5]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/1. Coordinates, Graphs, Lines/Lecture|intervals]].