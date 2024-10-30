---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Change of Parameter

$$\vec r(t) = 3 \cos (t) \hat i + 3 \sin(t) \hat j \text{ where } 0 \le t \le 2 \pi$$

This is the parametric equation for a `circle` with $\text{radius} = 3$, where $\vec r$ depends on the `angle`.  

$$\because l = r \theta$$

$$\frac l r = \theta$$

$$\therefore t = \frac l 3$$

$$0 \times 3 \le l \le 2 \pi \times 3$$

$$0 \le l \le 6 \pi$$

Hence, our equation becomes  

$$\vec r(l) = 3 \cos \left(\frac l 3\right) \hat i + 3 \sin \left( \frac l 3\right) \hat j \text{ where } 0 \le l \le 6 \pi$$

$t = g(u)$ is called a smooth change in parameter if $g(u)$ satisfies the following conditions::

1. $g$ is `differentiable`[^1]
2. $g^\prime$ is `continuous`[^2]
3. $g^\prime(u) \ne 0$ for any $u$ in the `domain`[^3] of $g$

## Arc Length

Because we do `derivative`[^2] of `vector valued functions`[^4] component wise, we can also do `integration`[^5] component wise.

### Example

if $x^\prime (t)$ and $y^\prime (t)$ are `continuous`[^2] for $a \le t \le b$ then the `arc length` is  

$$L = \int_a^b \sqrt{\left(\frac {dx}{dt}\right)^2 + \left(\frac {dy}{dt}\right)^2} dt$$

## Arc Length as Parameter

1. Select an arbitrary point P on the curve C to serve as a reference point.
2. Choose one direction to move along the curve which will be considered `positive` and other direction will be considered `negative`.

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/15. The Derivative/Lecture|differentiation]].
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/12. Continuity/Lecture|continuity]].
[^3]: Read more about [[Mathematics/Function/Content|functions]].
[^4]: Read more about [[semester 2/MTH301 - Calculus II/27. Vector Valued Functions/Lecture|vector valued functions]].
[^5]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/25. Integrations/Lecture|integrals]].