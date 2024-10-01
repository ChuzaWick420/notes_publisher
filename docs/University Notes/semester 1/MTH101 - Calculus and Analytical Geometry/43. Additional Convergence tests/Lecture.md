---
tags:
  - university-notes
  - sigma
university-name: Virtual University of Pakistan
---

# Additional Convergence Tests
## The Comparison Test
Let us say there are two `series`[^1] $\sum a_i$ and $\sum b_i$ with `non negative terms` such that  

$$a_1 \le b_1, a_2 \le b_2, \ldots a_i \le b_i$$

Then
1. If $\sum b_i$ _converges_ then $\sum a_i$ also _converges_.
2. If $\sum a_i$ _diverges_ then $\sum b_i$ also _diverges_.

## The Ratio Test
Let $\sum u_i$ be a `series`[^1] and $p = \lim_{i \to \infty} \frac {u_{i + 1}}{u_i}$ then if

1. $p < 1$ then `series`[^1] _converges_.
2. $p > 1$ then `series`[^1] _diverges_.
3. $p = 1$ then `series`[^1] may either _converge_ or _diverge_.

## The Root Test
Let $\sum u_i$ be a `series`[^1] and $p = \lim_{i \to \infty} (u_i)^{\frac 1 i}$ then if

1. $p < 1$ then `series`[^1] _converges_.
2. $p > 1$ then `series`[^1] _diverges_.
3. $p = 1$ then `series`[^1] may either _converge_ or _diverge_.

## Informal Principal
1. The `constant terms` in the `denominator` can usually be deleted without affecting the _convergence_ and _divergence_ of the `series`[^1].
2. If a `polynomial`[^2] in $i$ (or whatever `index` used for `sum`[^3]) appears as a `factor` in `numerator` or `denominator` then all the $i$ `terms` except for the the one with the highest `power`, can usually be deleted without affecting the _convergence_ and _divergence_ of the `series`[^1].

### Examples
The following 2 behaves alike  

$$\sum_{i=1}^{\infty}\frac{1}{2^{i}+1}$$

$$\sum_{i=1}^{\infty}\frac{1}{2^{i}}$$

The following 2 behaves alike  

$$\sum_{i=1}^{\infty}\frac{1}{\sqrt{i^{3}+2i}}$$

$$\sum_{i=1}^{\infty}\frac{1}{\sqrt{i^{3}}}$$

## The Limit Comparison Test
Let us say there are two `series`[^1] $\sum a_i$ and $\sum b_i$ with `positive terms` such that $p = \lim_{i \to +\infty}\frac{a_i}{b_i}$.  
Then if $p > 0$ and is `finite` then both `series`[^1] either _converge_ or _diverge_.

## References

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/42. Infinite Series/Lecture|series]].
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/7. Operations on Functions/Lecture|polynomials]].
