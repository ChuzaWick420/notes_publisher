---
tags:
  - university-notes
  - line-integral
  - integral
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Examples

## Example

Evaluate the following along the boundaries of a `rectangle` with `vertices` $A(1, 0)$, $B(3, 0)$, $C(3, 2)$ and $D(1, 2)$.  

$$\oint (xy \, dx + (1 + y^2)dy)$$

### Solution

$$I_c = \oint (xy \, dx + (1 + y^2)dy)$$

We can divide $c$ into 4 paths, representing the sides of the `rectangle`.

#### $c_1$

$$\overline{AB} : c_1 : y = 0 \text { from } x = 1 \text{ to } 3$$

Putting this into our `integrand`,[^1] we get  

$$I_{c_1} = 0$$

#### $c_2$

$$\overline{BC} : c_2 : x = 3 \therefore dx = 0$$

Putting this into our `integrand`,[^1] we get  

$$I_{c_2}=\int_{0}^{2}(1+y^{2})dy=\left[y+\frac{y^{3}}{3}\right]_{0}^{2}$$

$$= \frac {15} 3$$

#### $c_3$

$$c_3 : \overline{CD} : y = 2 \therefore dy = 0$$

$$I_{c_3}=\int_{3}^{1}2xdx=\left[x^{2}\right]_{3}^{1}=-8$$

#### $c_4$

$$c_4 : \overline{DA} : x = 1 \therefore dx = 0$$

$$I_{c_4}=\int_{2}^{0}(1+y^{2})dy=\left[y+\frac{y^{3}}{3}\right]_{2}^{0}$$

$$= - \frac {15} 3$$

Therefore  

$$I_c = I_{c_1} + I_{c_2} + I_{c_3} + I_{c_4} = -8$$

## Line Integral with respect to Arc Length

$$\because I = \int_C F_t ds$$

We can relate a `function`[^2] $f(x, y)$ which depends on the position of the point.

$$\because I = \int_C f(x, y) ds$$

which we can of course convert into an `integral`[^1] depending upon

$$I = \int_C f(x, y) \frac {ds}{dx} dx$$

Where  

$$\frac{ds}{dx} = \sqrt{\left(\frac{dx}{dx}\right)^2 + \left(\frac{dy}{dx}\right)^2}$$

$$\int_{C}f(x,y)dx=\int_{x_{1}}^{x_{2}}f(x,y)\sqrt{1+\left(\frac{dy}{dx}\right)^{2}}dx$$

## Dependence of line Integral on Path of Integration

If the `integrant`[^1] seen to be an `exact differential`[^3] then the `line integral`[^3] is independent of the path taken.

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/25. Integrations/Lecture|integration]].
[^2]: Read more about [[Mathematics/Function/Content|functions]].
[^3]: Read more about [[semester 2/MTH301 - Calculus II/30. Exact Differential/Lecture|exact differential and line integrals]].