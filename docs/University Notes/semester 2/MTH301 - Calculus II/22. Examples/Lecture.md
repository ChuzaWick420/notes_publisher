---
tags:
  - university-notes
  - integral
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Examples

## Example

Find the `volume` of the solid common to both `cylinders` $x^2 + y^2 = 25$ and $x^2 + z^2 = 25$

### Solution

The region $R$ which we will be `integrating`[^1] over, is bounded by $x^2 + y^2 = 25$  
The `surface` which will limits our `integral`[^1] is the other `cylinder`.  

$$x^2 + z^2 = 25$$

$$z = \sqrt{25 - x^2} $$

This is our height limit, which is our `surface`.  

$$\because x^2 + y^2 = 5^2$$

$$\text{radius } = 5$$

$$\because V = \iint_R f(x, y) dxdy$$

We will be `integrating`[^1] with respect to $y$ in the end.  
Therefore, we need numeric bounds for the `integral`[^1] so we can get a numeric volume.  
Since the `radius` is $5$, $0 \le y \le 5$.  
For the inner `integral`,[^1] we need bounds to be a `function`[^2] of $y$.  

$$\because x^2 +y^2 = 25$$

$$y = \sqrt{25 - x^2}$$

Plugging in the values, we get  

$$V = \int_0^5\int_{0}^{\sqrt{25 - x^2}} (\sqrt{25 - x^2})dxdy$$

Evaluate this and we will get  

$$= \frac {2000} 3$$

## Area Calculated as `Double Integral`[^3]

We know that  

$$\text{volume} = \text{area of R} \times \text{height}$$

If we want to find the `area` of $R$ then `height` is $1$.  

$$\iint_R dA = \text{area of R} \times 1$$

$$\text{area of R} = \iint_R dA$$

### Example

Find the `area` bounded by `parabola` $y = x^2$ and `line`[^4] $y = x + 2$

#### Solution

Trying to find the intersection points between both equations, we will get $x = -1, 2$.  

$$A = \int_{-1} ^ 2 \int_{x^2}^{x + 2} dy dx$$

$$= \int_{-1}^2 \left[y\right]_{x^2}^{x + 2} dx$$

$$=\int_{-1}^2 (x + 2 - x^2)dx$$

$$= \left[\frac{x^2} 2 + 2x - \frac{x^3} 3\right]_{-1}^2$$

$$= \frac 9 2$$

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/25. Integrations/Lecture|integrals]].
[^2]: Read more about [[Mathematics/Function/Content|functions]].
[^3]: Read more about [[semester 2/MTH301 - Calculus II/18. Revision Of Integration/Lecture|double integrals]].
[^4]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/4. Lines/Lecture|lines]].