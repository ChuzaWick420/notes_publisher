---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Geometry of Continuous Functions
## One Variable
The graph can be imagined as if it was drawn using a pen and you keep moving the pen on the paper without lifting it up.

## Two Variables
The graph can be imagined as constructed from a thin sheet of clay which is pinched and hollowed into peaks and valleys.

## Continuity of `functions`[^1] in 2 Variables
1. $f(x_0, y_0)$ is defined
2. $\lim_{(x, y) \to (x_0, y_0)} f(x, y)$ exists
3. $\lim_{(x, y) \to (x_0, y_0)} f(x, y) = f(x_0, y_0)$

The first point makes sure that there is no hole in the sheet.

## Continuity of `functions`[^1] in 3 Variables
1. $f(x_0, y_0, z_0)$ is defined
2. $\lim_{(x, y, z) \to (x_0, y_0, z_0)} f(x, y)$ exists
3. $\lim_{(x, y, z) \to (x_0, y_0, z_0)} f(x, y, z) = f(x_0, y_0, z_0)$

## Rules of `continuous functions`[^2]
If $g(x)$ and $h(y)$ are `continuous functions`[^2] in one variable and $f(x, y)$ depends on $g(x)$ and $h(y)$ then

1. Product
2. Sum
3. Difference
4. Quotient
5. Composition

of these `functions`[^1]($f(x, y)$) is also `continuous`.

## Partial Derivatives
Let $f(x, y)$ be a `function`[^1].  
If we hold $y = y_0$ and view $x$ as the `variable` then $f(x, y_0)$ depends on $x$ alone.  
if $f(x, y_0)$ is `differentiable`[^3] at $x = x_0$ then $f_x(x_0, y_0)$ is called `partial derivative` of $f(x, y)$ with respect to $x$ at $(x_0, y_0)$.

Similarly, $f_y(x_0, y_0)$ is `partial derivative` of $f(x, y)$ with respect to $y$ at $(x_0, y_0)$.

### Example
Find $f_x(1, 2)$ and $f_y(1, 2)$ for  

$$f(x,y) = 2x^3y^2 + 2y + 4x$$

#### Solution

$$f_x(x, y) = 6 x^2 y^2 + 4$$

> Reminder: $y$ is treated like a `constant`.

$$f_y(x, y) = 4 x^3 y + 2$$

Substituting values, we get  

$$f_x(1, 2) = 6(1)^2(2)^2 + 4 = 28$$

$$f_y(1, 2) = 4(1)^3(2) + 2 = 10$$

### Example

$$Z = 4x^2 - 2y + 7x^4y^5$$

$$\frac{\partial z}{\partial x} = 8x + 28x^3y^5$$

$$\frac{\partial z}{\partial y} = -2 + 35x^4y^4$$

### Example

$$w = x^2 + 3y^2 + 4z^2 - xyz$$

$$\frac{\partial w}{\partial x} = 2x - yz$$

$$\frac{\partial w}{\partial y} = 6y - xz$$

$$\frac{\partial w}{\partial z} = 8z - xy$$

## References
Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[Mathematics/Function/Content|functions]].
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/12. Continuity/Lecture|continuity]].
[^3]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/15. The Derivative/Lecture|differentiation]].
