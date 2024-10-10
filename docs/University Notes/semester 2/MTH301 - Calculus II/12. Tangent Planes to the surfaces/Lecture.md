---
tags:
  - university-notes
  - vectors
  - tangent
  - partial-differential
university-name: Virtual University of Pakistan
---

# Tangent Planes to the Surfaces
If $C$ is a parametric curve on 3D then the `tangent line`[^1] to the $C$ at a point $P_0$ is the `line`[^2] going through $P_0$ and the `unit tangent vector`[^3].

## Tangent Plane
If $P_0(x_0, y_0, z_0)$ is any point on the `surface` $S$ then the `plane`[^4] which contains all the `tangents`[^1] to the point $P_0$ is called `tangent plane`.

## Surface Normal
The `vector`[^3] which is _perpendicular_ to [tangent plane](#tangent-plane) is called `surface normal`.

## Parametric Equations of a `line`[^2]
The parametric equations of a `line`[^2] in 2D, going through $P(x_0, y_0)$, _parallel_ to the `vector`[^3] $a \hat i + b \hat j$ is given by  

$$x = x_0 + at \text{ and } y = y_0 + bt$$

Eliminating $t$, we get  

$$\frac{x-x_{0}}{a}=\frac{y-y_0}{b}$$

$$y-y_{0}=\frac{b}{a}(x-x_{0})$$

Similarly for 3D,

$$\frac{x-x_{0}}{a}=\frac{y-y_0}{b} = \frac{z - z_0}{c}$$

## Parametric Vector Form

$$\vec{r}(t) = (x_0 + at) \hat i + (y_0 + bt) \hat j$$

The idea is to make the $x$ and $y$ `variables` dependent on some other variable which is $t$ in this case.

## Equation of a Tangent Plane
We can construct a `plane`[^4] if we know

1. A point on the `plane`[^4]
2. A [normal vector](#surface-normal) to it.

Let there be a point $P_0(x_0, y_0, z_0)$ on the `plane`[^4] and [normal](#surface-normal) being in the direction of $\vec n = a \hat i + b \hat j + c \hat k$  
Then let $P(x, y, z)$ be any arbitrary point on this `plane`[^4].  
Then we can construct number of `vectors`[^3] on this `plane`[^4] by  

$$\vec{P_0P} = (x - x_0) \hat i + (y - y_0) \hat j + (z - z_0) \hat k$$

Also  

$$\vec n \cdot \vec{P_0P} = 0$$

Then the equation of the `tangent plane` is  

$$a(x - x_0) + b(y - y_0) + c(z - z_0) = 0$$

## Example
We know that the general equation for the `plane`[^4] is 

$$ax + by + cz + d = 0$$

Let their be 2 points on it  

$$(x_1, y_1, z_1)$$

$$(x_2, y_2, z_2)$$

Putting these in our equation of the `plane`[^4], we get  

$$ax_1 + by_1 + cz_1 + d = 0$$

$$ax_2 + by_2 + cz_2 + d = 0$$

Subtracting these, we get  

$$a(x_2 - x_1) + b(y_2 - y_1) + c(z_2 - z_1) = 0$$

From the definition of `dot product`[^3], we can reverse it as 

$$( a \hat i + b \hat j + c \hat k ) \cdot \left((x_2 - x_1) \hat i + (y_2 - y_1) \hat j + (z_2 - z_1) \hat k\right) = 0$$

Here  

$$\vec V = (x_2 - x_1) \hat i + (y_2 - y_1) \hat j + (z_2 - z_1) \hat k$$

If  

$$\Phi = ax + by + cz$$

then  

$$\Phi_x = a \text{ and } \Phi_y = b \text{ and } \Phi_z = c$$

$$\therefore \nabla \Phi = a \hat i + b \hat j + c \hat k$$

Plugging it into the equation we got from the `dot product`[^3] definition, we get  

$$\nabla \Phi \cdot \vec V = 0$$

This shows that $\nabla \Phi$ is always [normal](#surface-normal) to the `surface`.

## Gradients and Tangents to the Surface

$$z = f(x, y) = c$$

If this differentiable `function`[^5] has a constant value $c$ along some smooth curve having parametric equations  

$$x = g(t)$$

$$y = h(t)$$

$$\vec r = g(t) \hat i + h(t) \hat j$$

Then  

$$\frac{d}{dt} \left(f\left(g(t), h(t)\right)\right) = \frac{d}{dt} c$$

Applying `chain rule`[^6], we get  

$$\frac{\partial f}{\partial x}\frac{dg}{dt}+\frac{\partial f}{\partial y}\frac{dh}{dt}=0$$

From the `dot product`[^3] definition  

$$\left(\frac{\partial f}{\partial x}\hat i+\frac{\partial f}{\partial y} \hat j\right)\cdot\left(\frac{dg}{dt} \hat i+\frac{dh}{dt}\hat j\right)=0$$

Some additional reversing, we get  

$$\nabla f \cdot \frac{d \vec{r}}{dt} = 0$$

### Example
Find [tangent plane](#tangent-plane) to the surface  

$$f(x, y, z) = 9 x^2 + 4y^2 - z^2 - 36 \text{ at } P(2, 3, 6)$$

#### Solution

$$\frac{\partial}{\partial x} f(x, y, z) = 18x$$

$$\frac{\partial}{\partial y} f(x, y, z) = 8y$$

$$\frac{\partial}{\partial z} f(x, y, z) = -2z$$

$$f_x(P) = 18(2) = 36$$

$$f_y(P) = 8(3) = 24$$

$$f_z(P) = -2(6) = -12$$
  
So the equation for [tangent plane](#tangent-plane) will be  

$$36(x-2)+24(y-3)-12(z-6)=0$$

$$3x+2y-z-6=0$$

## References
Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/14. Tangent Lines, Rates of Change/Lecture|tangents]].
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/4. Lines/Lecture|lines]].
[^3]: Read more about [[semester 2/MTH301 - Calculus II/10. Introduction to vectors/Lecture|vectors]].
[^4]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/3. Coordinate Planes and Graphs/Lecture|planes]].
[^5]: Read more about [[Mathematics/Function/Content|functions]].
[^6]: Read more about [[semester 2/MTH301 - Calculus II/8. Euler theorem/Lecture|the chain rule]].
