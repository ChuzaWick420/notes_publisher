---
tags:
  - university-notes
  - integral
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Revision of `Integration`[^1]

## Double Integral

The `double integral` of a `function`[^2] of 2 variables $x$ and $y$ over a region $R$ can be denoted as  

$$\iint_R = f(x, y) dx dy$$

### Example

Find the `volume` of a solid bounded by `plane`[^3] $z = 4 - x - y$ and `rectangle` $R = \{(x, y) : 0 \le x \le 1, 0 \le y \le 2\}$

#### Solution

$$V = \iint_R(4 - x - y) dxdy$$

$$=\int_0^2\int_0^1 (4 - x - y) dxdy$$

$$=\int_0^2 \left[4x - \frac{x^2} 2 - xy\right]_0^1 dy$$

$$=\int_0^2 \left[4(1) - \frac{1^2} 2 - (1)y\right] - \left[4(0) - \frac{0^2} 2 - (0)y\right] dy$$

$$= \int_0^2 \left(\frac 7 2 - y\right) dy$$

$$= \left[\frac 7 2 y - \frac {y^2}{2}\right]_0^2$$

$$= \left(\frac 7 2 (2) - \frac{(2)^2} 2\right) -  \left(\frac 7 2 (0) - \frac{(0)^2} 2 \right)$$

$$= 7 - 2$$

$$= 5$$

## Iterated or Repeated `Integral`[^1]

Following is called `iterated` or `repeated integral`  

$$\int_a^b \left(\int_c^d f(x, y)dx\right) dy$$

$$\int_c^d \left(\int_a^b f(x, y)dy\right) dx$$

Here $c \le x \le d$ and $a \le y \le b$. 

Integrating with respect to $x$ yields a `function`[^2] of $y$ and integrating with respect to $y$ yields a `function`[^2] of $x$. 

## Theorem

$$\int_a^b\int_c^d f(x, y) dxdy = \int_c^d\int_a^b f(x, y) dydx$$

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[25. Integrations|integration]].
[^2]: Read more about [[Mathematics/Function/Content|function]].
[^3]: Read more about [[3. Coordinate Planes and Graphs|planes]].