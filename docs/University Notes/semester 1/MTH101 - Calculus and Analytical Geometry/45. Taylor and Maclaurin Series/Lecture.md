---
tags:
  - university-notes
  - sigma
  - function
  - differentiation
  - "calculus"
university-name: Virtual University of Pakistan
---

# Taylor and Maclaurin Series
One of the early applications of `calculus` was to approximate numerical values of `functions`[^1] such as $\sin (x)$ and $\ln (x)$ etc.  
To do this, we would approximate the `function`[^1] using `polynomials`[^2] and then later approximating the numerical values from that.

## Problem
Given a `function`[^1] $f(x)$ and a point $a$ over the `x axis`, find a `polynomial`[^2] of a specified degree that best approximates the $f(x)$ over the vicinity of the point $a$.  

## Solution
Imagine we have a `polynomial`[^2]  

$$P(x) = c_0 + c_1 \cdot x + c_2 \cdot x^2 + \ldots + c_n \cdot x^n$$

The `polynomial`[^2] $P(x)$ has $n + 1$ coefficients. Therefore, it is reasonable to think that we can impose $n + 1$ conditions over it.  
Assume that our point of interest is $a = 0$ then to have a high degree of resemblance between $f(x)$ and $P(x)$, we find the coefficients of $P(x)$ such that  

$$f^{\prime}(0) = P^{\prime}(0)$$

$$f^{n}(0) = P^{n}(0)$$

Once we start finding some of these `derivatives`[^3], we will get a pattern that is  

$$f^n(0) = P^n(0) = n!c_n$$

So the general coefficient $c_n$ for $P(0)$ will be  

$$c_n = \frac{f^n(0)}{n!}$$

## Maclaurin Series
Plugging the $c_n$ term into our `polynomial`[^2], we get  

$$P_{n}(x)=f(0)+f'(0)x+\frac{f''(0)}{2!}x^{2}+\frac{f'''(0)}{3!}x^{3}+\ldots+\frac{f^{(n)}(0)}{n!}x^{n}$$

This is the case at $x = 0$

## Taylor Series
If we make the case for $x = a$ then [maclaurin series](#maclaurin-series) becomes  

$$P_{n}(x)=f(a)+f'(a)(x-a)+\frac{f''(a)}{2!}(x-a)^{2}+\frac{f'''(a)}{3!}(x-a)^{3}+\ldots+\frac{f^{(n)}(a)}{n!}(x-a)^{n}$$

and if $f(x)$ has `derivatives` of all orders of $a$ then  

$$\sum_{i=0}^{\infty}\frac{f^{(i)}(a)}{i!}(x-a)^{i}=f(a)+f'(a)(x-a)+\frac{f''(a)}{2!}(x-a)^{2}+\ldots+\frac{f^{(i)}(a)}{i!}(x-a)^{i}+\ldots$$

## References
Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[Mathematics/Function/Content|functions]].
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/7. Operations on Functions/Lecture|polynomials]].
[^3]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/15. The Derivative/Lecture|derivatives]].
