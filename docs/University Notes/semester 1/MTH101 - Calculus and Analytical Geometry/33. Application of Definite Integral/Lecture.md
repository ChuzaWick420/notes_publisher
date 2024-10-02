---
tags:
  - university-notes
  - integral
university-name: Virtual University of Pakistan
---

# Applications of `Definite Integrals`[^1]
## Area between 2 Curves
Let there be 2 `functions`[^2] $f(x)$ and $g(x)$ defined over the `interval`[^3] $[a, b]$ such that $f(x) \ge g(x)$.  
![[Pasted image 20240927203241.png]]  
Let $A_1$ be `area` under $f(x)$ and $A_2$ be `area` under $g(x)$ then $A$, being the `area` _between_ them can be found out by  

$$A = A_1 - A_2$$

$$A=\int_{a}^{b}f(x)dx-\int_{a}^{b}g(x)dx=\int_{a}^{b}(f(x)-g(x))dx$$

It is possible that one of the `functions`[^2] is under the `x axis`. Then in that case, we translate both `functions`[^2] above the `x axis` by some `constant` value $m$.  
![[Pasted image 20240927203616.png]]  

$$A=\int_{a}^{b}(f(x)+m)dx-\int_{a}^{b}(g(x)+m)dx=\int_{a}^{b}(f(x)-g(x))dx$$

This definition also applies if we replace $x$ with $y$.

## References
Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/29. Definite Integral/Lecture|definite integrals]].
[^2]: Read more about [[Mathematics/Function/Content|functions]].
[^3]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/1. Coordinates, Graphs, Lines/Lecture|intervals]].
