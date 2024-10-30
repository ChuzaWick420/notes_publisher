---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Examples

## Example

Find `absolute maximum`[^1] and `absolute minimum`[^1] values on the closed triangular region $R$ with `vertices` $(0, 0)$, $(0, 4)$ and $(5, 0)$ for the `function`[^2]  

$$f(x, y) = xy - x - 3y$$

### Solution

$$f_x(x, y) = y - 1$$

$$f_y(x, y) = x - 3$$

#### For Critical Points

$$f_x(x, y) = 0\text{ and } f_y(x, y) = 0$$

$$y = 1$$

$$x = 3$$

So there is only one `critical point`[^3] that is $(3, 1)$.

#### Boundaries

There are 3 boundaries for triangle which are `line segments`.[^4]

##### Line between $(0, 0)$ and $(5, 0)$

Here $y = 0$, therefore,  

$$f(x, 0) = -x \text{ where } 0 \le x \le 5$$

##### Line between $(0, 0)$ and $(0, 4)$

Here $x = 0$, therefore,  

$$f(0, y) = -3y \text{ where } 0 \le y \le 4$$

##### Line between $(5, 0)$ and $(0, 4)$

Here $y = - \frac 4 5 x + 4$, therefore,  

$$f\left(x, -\frac 4 5 x + 4\right) = - \frac 4 5 x^2 + \frac 3 5 x + 12 \text{ where } 0 \le x \le 5$$

$$f^{\prime}\left(x, -\frac 4 5 x + 4\right) = - \frac 8 5 x + \frac 3 4 x$$

If we solve for $x$, we get $x = \frac 3 8$.  
Similarly, changing the equation into  

$$-(y - 4) \cdot \frac 5 4 = x$$

putting it inside $f(x, y)$ and solving for $y$, we get  

$$y = \frac{37}{10}$$

|                 $(x, y)$                  |    $(f(x, y))$     |
| :---------------------------------------: | :----------------: |
|                 $(0, 0)$                  |        $0$         |
|                 $(5, 0)$                  |        $-5$        |
|                 $(0, 4)$                  |        $-4$        |
| $\left(\frac{3}{8}, \frac{37}{10}\right)$ | $- \frac{807}{80}$ |
|                 $(3, 1)$                  |        $-3$        |

From there, we can conclude that `absolute maximum`[^1] is $0$ existing at $(0, 0)$ and `absolute minimum`[^1] is $- \frac{807}{80}$ existing at $(\frac{3}{8}, \frac{37}{10})$.

## Example

Find dimensions of a box such that is has maximum `volume`, which is inscribed in a `sphere` with `radius` $r = 4$.

### Solution

The equation for `volume` is  

$$V(x, y, z) = xyz$$

The equation for `sphere` is  

$$x^2 + y^2 + z^2 = 4^2$$

We will isolate $z$,  

$$z = \sqrt{16 - x^2 - y^2}$$

Plugging it back into $V(x, y, z)$, the `function`[^2] becomes dependent on only $x$ and $y$.  

$$V(x, y) = xy \sqrt{16 - x^2 - y^2}$$

Since we want to maximize it, the `absolute maximum`[^3] exists at `critical points`.[^3]  
To find those, we assume $V_x = 0$ and $V_y = 0$.  

$$V_x = \frac{\partial}{\partial x} xy\sqrt{16 - x^2 - y^2}$$

$$0 = y\left(\frac{-2x^{2}-y^{2}+16}{\sqrt{16-x^{2}-y^{2}}}\right)$$

This gets us down to  

$$2x^2 + y^2 = 16$$

Similarly, $V_y$ gets us down to  

$$x^2 + 2y^2 = 16$$

Solving both these equations, we get  

$$x = y = \frac{4}{\sqrt{3}}$$

This suggests there is only one `critical point`.[^3]  
Then for our `2nd partial derivative test`,[^5] we find additional terms which are  

$$V_{xx}=\frac{xy(2x^{2}+3y^{2}-48)}{(16-x^{2}-y^{2})^{\frac{3}{2}}}$$

$$V_{yy}=\frac{xy(3x^{2}+2y^{2}-48)}{(16-x^{2}-y^{2})^{\frac{3}{2}}}$$

$$V_{xy} = \frac{2y^{4}+3x^{2}y^{2}-48y^{2}-2x^{2}y-16x^{2}+256}{(16-x^{2}-y^{2})\sqrt{16-x^{2}-y^{2}}}$$

$$\because D = V_{xx}(x_0, y_0) \cdot V_{yy}(x_0, y_0) - V_{xy}^2(x_0, y_0)$$

$$V_{xx}\left(\frac{4}{\sqrt 3}, \frac{4}{\sqrt 3}\right) = \frac{-16}{3}$$

$$V_{yy}\left(\frac{4}{\sqrt 3}, \frac{4}{\sqrt 3}\right) = \frac{-16}{3}$$

$$V_{xy}\left(\frac{4}{\sqrt 3}, \frac{4}{\sqrt 3}\right) = \frac{-8}{3}$$

Plugging it into $D$, we get  

$$D = \frac {320}{3} > 0$$

Since $D > 0$ and $V_{xx} < 0$, the `absolute maximum`[^3] exists at $\left(\frac{4}{\sqrt 3}, \frac{4}{\sqrt 3}\right)$.  
Therefore, the side lengths are $\frac 4 {\sqrt 3}$.

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 2/MTH301 - Calculus II/14. Extrema of function of two variables/Lecture|extreme values]].
[^2]: Read more about [[Mathematics/Function/Content|functions]].
[^3]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/22. Relative Extrema/Lecture|extreme values]].
[^4]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/4. Lines/Lecture|lines]].
[^5]: Read more about [[semester 2/MTH301 - Calculus II/15. Examples/Lecture|second partial derivative test]].