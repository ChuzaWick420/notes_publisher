---
tags:
  - university-notes
  - integral
  - limits
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Examples

## Example

Let $R_a$ be a region bounded by `circle` $x^2 + y^2 = a^2$.  
Then evaluate  

$$\int_{- \infty}^{+ \infty}\int_{- \infty}^{+ \infty} e^{-(x^2 + y^2)} dx dy$$

$$= \lim_{a \to \infty} \iint_R e^{-(x^2 + y^2)} dx dy$$

$$\because e^x = \exp (x)$$

$$= \lim_{a \to \infty} \iint_R \exp\left(-(x^2 + y^2)\right) dx dy$$

$$= \lim_{a \to \infty} \int_0^{2 \pi} \int_0^a \exp\left(-r^2\right) r dr d\theta$$

$$\because \frac d {dx} a^{bx} = a^{bx} \cdot \ln (a) \cdot \frac d {dx} (bx)$$

Also applying `integration by subtitution`,[^1] we get  

$$= \lim_{a \to \infty} \int_0^{2 \pi} \left[ -\frac {\exp(-r^2)}{2} \right]_0^{a} d\theta$$

$$= \lim_{a \to \infty} \int_0^{2 \pi} \left[-\frac {\exp(-a^2)}{2} - \frac 1 2 \right] d\theta$$

$$= \lim_{a \to \infty} \frac 1 2 \left[\left(1 - \exp(-a^2) \right) \theta \right]_0^{2 \pi}$$

$$
= \pi - \lim_{a \to \infty} \frac{\pi}{\exp (-a^2)} = \pi
$$

## Theorem

Let $G$ be a `rectangular` region bounded by following  

$$a \le x \le b$$

$$c \le y \le d$$

$$k \le z \le l$$

Then if $f(x, y, z)$ is a `continuous`[^2] `function`[^3] then

$$
\iiint_{G} f(x, y, z) dV = \int_{a}^{b} \int_{c}^{d} \int_{k}^{\ell} f(x, y, z) dz \, dy \, dx
$$

And the order of `integrals`[^4] can be changed.

## Example

Evaluate  

$$\iiint_S xyz \, dx dy dz$$

Where  

$$S = \{(x, y, z) : x^2 + y^2 + z^2 \le 1, x \ge 0, y \ge 0, z \ge 0\}$$

### Solution

$$\int_0^1\int_0^{\sqrt{1 - x^2}}\int_0^{\sqrt{1 - x^2 - y^2}} xyz \, dzdydx$$

$$= \int_0^1\int_0^{\sqrt{1 - x^2}}xy\left[\frac {z^2} 2\right]_0^{\sqrt{1 - x^2 - y^2}} \, dydx$$

Continue evaluating and we will get  

$$= \frac 1 {48}$$

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/26. Integration by Substitution/Lecture|integration by substitution]].
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/12. Continuity/Lecture|continuity]].
[^3]: Read more about [[Mathematics/Function/Content|functions]].
[^4]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/25. Integrations/Lecture|integrals]].