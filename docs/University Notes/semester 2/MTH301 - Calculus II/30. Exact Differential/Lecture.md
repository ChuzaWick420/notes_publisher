---
tags:
  - university-notes
  - partial-differential
  - distance
university-name: Virtual University of Pakistan
---

# Exact Differential
If $z = f(x, y, w)$ then  

$$dz = \frac{\partial z}{\partial x}dx + \frac{\partial z}{\partial y}dy+ \frac{\partial z}{\partial w}dw$$

Any expression of the form $dz = P dx + Q dy$ where $P$ and $Q$ are `functions`[^1] of $x$ and $y$ is an `exact differential` if it can be `integrated`[^2] to determine $z$.  

$$\because P = \frac{\partial z}{\partial x} \text{ and } Q = \frac{\partial z}{\partial y}$$

$$\frac{\partial P}{\partial y} = \frac{\partial z}{\partial y \partial x} \text{ and } \frac{\partial Q}{\partial z} = \frac{\partial z}{\partial x \partial y}$$

$$\because \frac{\partial z}{\partial x \partial y} = \frac{\partial z}{\partial y \partial x}$$

$$\therefore \frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x}$$

## Example

$$dz = (3x^2 + 4y^2)dx + 8xy dy$$

### Solution

$$P = 3x^2 + 4y^2$$

$$\frac{\partial P}{\partial y} = 8y$$

$$Q = 8xy$$

$$\frac{\partial Q}{\partial x} = 8y$$

$$\because \frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x}$$

Therefore, $dz$ is the [exact differential](#exact-differential).

## `Integration`[^2] Of `Exact Differentials`

$$dz = P dx + Q dy$$

$$\therefore z = \int P dx \text{ and } z = \int Q dy$$

### Example

$$dz = (2xy + 6x) dx + (x^2 + 2y^3) dy$$

$$P = \frac{\partial z}{\partial x} = 2xy + 6x$$

$$z = \int (2xy + 6x) dx$$

$$z = x^2y + 3x^2 + f(y)$$

Here $f(y)$ is the `constant` of `integral`[^2].  

$$Q = \frac{\partial z}{\partial y} = x^2 + 2y^3$$

$$z = \int (x^2 + 2y^3) dy$$

$$z = x^2y + \frac{y^4}{2} + g(x)$$

We can find values of $g(x)$ and $f(y)$ such that both equations represent the same $z$.  
So by comparing both equations, we see that  

$$f(y) = \frac{y^4} 2$$

$$g(x) = 3x^2$$

$$z = x^2y + 3x^2 + \frac{y^4}{2}$$

## Area Enclosed by a Closed Curve
Imagine in a 2D `plane`[^3], we have a curve, bounded by a `function`[^1] $f(x)$ within the `interval`[^4] $[x_1, x_2]$.  
![[Pasted image 20241016130628.png]]  
We know that the area of this region is given by the `integral`[^2]  

$$A_1 = \int_{x_1}^{x_2} f(x) dx$$

Then there is another curve $g(x)$ such that it intersects $f(x)$ at 2 points at least, making a closed loop.  
Similarly, the area under $g(x)$ would be  

$$A_2 = \int_{x_1}^{x_2} g(x) dx$$

Then the `area` of the closed loop is  

$$\text{Area} = \int_{x_1}^{x_2} f(x) dx - \int_{x_1}^{x_2} g(x) dx$$

To make a closed loop with counter clockwise orientation,

$$\text{Area} = - \int_{x_2}^{x_1} f(x) dx - \int_{x_1}^{x_2} g(x) dx$$

$$\text{Area} = - \left(\int_{x_2}^{x_1} f(x) dx + \int_{x_1}^{x_2} g(x) dx \right)$$

Here, we are `integrating`[^2] $g(x)$ from _left to right_ and $f(x)$ from _right to left_.  

$$\text{Area} = - \oint y dx$$

### Example
Determine the `area` within the `interval`[^4] $[0, 2]$ bounded by `functions`[^1] $y = 4x$ and $y = x^3$.

#### Solution
![[Pasted image 20241016131959.png]]

Let us define paths such that we `integrate`[^2] in a counter clockwise direction.  

$$c_1 : y=x^3 \text{ from } x=0 \text{ to } 2$$

$$c_2 : y=4x \text{ from } x=2 \text{ to } 0$$

$$A = - \oint y dx$$

$$=-\left\{\int_{1}^{2}x^{3}dx+\int_{2}^{0}4xdx\right\}$$

$$=-\left\{\left(\frac{x^{4}}{4}\right)_{0}^{2}+\left(2x^{2}\right)_{0}^{2}\right\}$$

$$= 4$$

### Example
Find `area` of `triangle` with `vertices` $O(0, 0)$, $A(5, 3)$ and $B(2, 6)$.

#### Solution
![[Pasted image 20241016142057.png]]  
The equations for the sides of the `triangle` are  

$$m\overline{OA} = y = \frac 3 5x$$

$$m\overline{OB} = y = \frac 6 2x = 3x$$

$$m\overline{AB} = y = \frac {6 - 3}{2 - 5}x + 8 = 8 - \frac 3 3 x = 8 -x$$

Here $8$ is the `y intercept`[^5].  
Let us now define paths for our counter clockwise direction.  

$$c_1: y = \frac 3 5 x \text{ from } x = 0 \text{ to } 5$$

$$c_2: y = 8 - x \text{ from } x = 5 \text{ to } 2$$

$$c_3: y = 3x \text{ from } x = 2 \text{ to } 0$$

$$\because A = - \oint y dx$$

$$=-\left\{\int_{0}^{5}\frac{3}{5}xdx+\int_{5}^{2}(8-x)dx+\int_{2}^{0}3xdx\right\}$$

$$= 12$$

## Line Integral
Imagine a curve $C$ from $A$ and $B$ and there is a particle at $K$ on this curve.  
Then imagine there is a `force` $\vec{F}$ acting on the particle at $K$  
This `force` can be broken down into its components such that one component is along the `tangent vector`[^6] of the curve and other one is along the `normal` to the curve.  
Let us define $\delta s$ along the curve which is the `distance` from $K$ to $L$  

$$\delta s = \lvert L - K \rvert$$

Then the `work` done in moving the particle on $K$ is given by  

$$\lim_{\delta s \to 0} \sum F_t \delta s = \int F_t ds \text{ from } A \text{ to } B$$

$$= \int_{AB} F_t ds$$

This `integral`[^2] is called `line integral`.  
We can further break the `tangent component` $F_t$ into its $x$ component which is $P dx$ and $y$ component which is $Q dy$.

## References
Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[Mathematics/Function/Content|functions]].
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/25. Integrations/Lecture|integrals]].
[^3]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/3. Coordinate Planes and Graphs/Lecture|planes]].
[^4]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/1. Coordinates, Graphs, Lines/Lecture|intervals]].
[^5]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/8. Graphing Functions/Lecture|intercepts]].
[^6]: Read more about [[semester 2/MTH301 - Calculus II/10. Introduction to vectors/Lecture|vectors]].
