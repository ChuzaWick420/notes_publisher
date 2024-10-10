---
tags:
  - university-notes
  - vectors
  - tangent
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

## References
Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/14. Tangent Lines, Rates of Change/Lecture|tangents]].
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/4. Lines/Lecture|lines]].
[^3]: Read more about [[semester 2/MTH301 - Calculus II/10. Introduction to vectors/Lecture|vectors]].
[^4]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/3. Coordinate Planes and Graphs/Lecture|planes]].
