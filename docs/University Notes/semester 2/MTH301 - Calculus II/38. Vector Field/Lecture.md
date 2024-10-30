---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Vector Field

## Conservative Vector Fields

The value of `integral`[^1] $\int_c \vec F \cdot d \vec r$ between 2 points depends on particular paths of `integration`.[^1]  
However if this value in independent of the path for a `vector field` $\vec F$ then $\vec F$ is called a `conservative vector field`.  

$$\oint_c \vec F \cdot d \vec r = 0$$

## Example

If $\vec F = 2xyz \hat i + x^2 z \hat j + x^2 y \hat k$ then evaluate $\int_c \vec F \cdot d \vec r$ between $A(0, 0, 0)$ and $B(2, 4,6)$.

1. Along the curve $c$ whose parametric equations are $x = u$, $y = u^2$ and $z = 3u$
2. Along 3 straight `lines`[^2] $c_1: (0, 0, 0)$ to $(2, 0, 0)$, $c_2: (2, 0, 0)$ to $(2, 4, 0)$ and $c_3: (2, 4, 0)$ to $(2, 4, 6)$.

### Solution

$$\vec F(x, y, z) = 2xyz \hat i + x^2 z \hat j + x^2 y \hat k$$

$$d \vec r = dx \hat i + dy \hat j + dz \hat k$$

$$\vec F(x, y, z) \cdot d \vec r = (2xyz \hat i + x^2z \hat j + x^2y \hat k) \cdot (dx \hat i + dy \hat j + dz \hat k)$$

$$=2xyz \, dx+x^{2}z \, dy+x^{2}y \,dz$$

$$\because x = u \implies dx = du$$

$$\because y = 2u \implies dy = 2du$$

$$\because z = 3u \implies dz = 3du$$

$$\therefore \vec F(u) \cdot d \vec r = 15u^4 du$$

Using any of the $x(u), y(u), z(u)$, we can see that the bounds for $u$ are $0, 2$.  

$$\therefore \int_c \vec F(u) \cdot d \vec r = \int_0^2 15u^4 du = \left[3u^5\right]_0^2 = 96$$

Now we will `integrate`[^1] along the straight `lines`.[^2]

#### $c_1$

$$c_1: (0, 0, 0) \text{ to } (2, 0, 0)$$

This shows us that  

$$y = 0, z = 0, dy = 0$$

$$\int_{c_1} \vec F(x, y, z) \cdot d \vec r = \int_{c_1} (2xyz~dx+x^{2}zdy+x^{2}ydz)$$

$$= \int_{c_1}0 + 0 + 0 = 0$$

#### $c_2$

$$c_2: (2, 0, 0) \text{ to } (2, 4, 0)$$

This shows us that  

$$x = 2, dx = 0, z = 0, dz = 0$$

$$\int_{c_2} \vec F(x, y, z) \cdot d \vec r = \int_{c_2} (2xyz~dx+x^{2}zdy+x^{2}ydz)$$

$$= \int_{c_2}0 + 0 + 0 = 0$$

#### $c_3$

$$c_3: (2, 4, 0) \text{ to } (2, 4, 6)$$

This shows us that  

$$x = 2, dx = 0, y = 4, dy = 0$$

$$\int_{c_3} \vec F(x, y, z) \cdot d \vec r = 0 + 0 + \int_0^6 16 dz$$

$$= \left[16z\right]_0^6 = 96$$

$$\int_c \vec F \cdot d \vec r = \int_{c_1 + c_2 + c_3} \vec F \cdot d \vec r$$

$$= \int_{c_1} \vec F \cdot d \vec r + \int_{c_2} \vec F \cdot d \vec r + \int_{c_3} \vec F \cdot d \vec r$$

$$= 0 + 0 + 96 = 96$$

This shows that the `vector field` $\vec F$ is `conservative`.  
Also,

$$\nabla \times \vec F = \left|\begin{matrix}\hat i & \hat j & \hat k \\\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\2xyz & x^2 z & x^2y\end{matrix}\right|$$

$$= 0$$

We can apply 3 conditions to check if a `vector field` $\vec F$ is `conservative` or not.

1. $$\oint \vec F \cdot d \vec r$$

2. $$\nabla \times \vec F = 0$$

3. $$\vec F = \nabla V$$

## Divergence Theorem or Gauss' Theorem

For a closed `surface` $S$, enclosing a region $V$ in a `vector field` $\vec F$,  

$$\int_V \nabla \cdot \vec F dV = \int_S \vec F \cdot d \vec S$$

### Example

Verify the [divergence theorem](#divergence-theorem-or-gauss-theorem) for the `vector field`.  

$$\vec F = x^2 \hat i + z \hat j + y \hat k$$

taken over the region bounded by the `planes`[^3] $z = 0$, $z = 2$, $x = 0$, $x = 1$, $y = 0$ and $y = 3$.  

$$dV = dxdydz$$

We have to show that  

$$\int_V \nabla \cdot \vec F dV = \int_S \vec F \cdot d \vec S$$

#### Left Hand Side

$$\nabla \cdot \vec F = \left(\frac{\partial}{\partial x} \hat i + \frac{\partial}{\partial y} \hat j + \frac{\partial}{\partial z} \hat k\right) \cdot (x^2 \hat i + z \hat j + y \hat k)$$

$$=\frac{\partial}{\partial x}(x^{2})+\frac{\partial}{\partial y}(z)+\frac{\partial}{\partial z}(y)$$

$$=2x+0+0=2x$$

$$\therefore \int_V \vec F dV = \int_V 2x dV$$

$$= \iiint_V 2x dzdydx$$

$$= \int_0^1 \int_0^3 \int_0^2 2x dzdydx$$

$$= 6$$

#### Right Hand Side

$$\int_S \vec F \cdot d \vec S = \int_S \vec F \cdot \hat n dS$$

The $S$ consists of $6$ `surfaces`.

##### Base

$$S_1: z = 0, \hat n = - \hat k$$

$$\therefore \vec F = x^2 \hat i + y \hat k$$

$$\therefore dS_1 = dx dy$$

$$\int_{S_1} \vec F \cdot \hat n dS = \iint_{S_1} (x^2 \hat i + y \hat k) \cdot (- \hat k) dy dx$$

$$= \int_0^1\int_0^3 (-y) dy dx$$

$$= - \frac 9 2$$

##### Top

$$S_2: z = 2, \, \hat{n} = \hat{k}$$

$$\therefore \vec F = x^2 \hat i + z \hat j + y \hat k$$

$$\therefore \, dS_2 = dx \, dy$$

$$\int_{S_2} \vec F \cdot \hat{n} \, dS = \iint_{S_2} \left( x^2 \hat{i} + z \hat{j} + y \hat{k} \right) \cdot (\hat{k}) \, dy \, dx$$

$$= \int_0^1 \int_0^3 y \, dy \, dx = \frac{9}{2}$$

##### Right

$$S_3: y = 3, \hat n = \hat j \cdot dS_3 = dx \, dz \, \hat j$$

$$\therefore \vec F = x^2 \hat i + z \hat j + y \hat k$$

$$\int_{S_3} \vec F \cdot \hat{n} \, dS = \iint_{S_3} \left( x^2 \hat{i} + z \hat{j} + y \hat{k} \right) \cdot (\hat{j}) \, dz \, dx$$

$$= \int_0^1\int_0^2 z dz dx$$

$$= 2$$

##### Left

$$S_4: y = 0, \hat n = - \hat j$$

$$\therefore dS_4 = dx \, dz$$

$$\therefore \vec F = x^2 \hat i + z \hat j + y \hat k$$

$$\int_{S_4} \vec F \cdot \hat{n} \, dS = \iint_{S_4} \left( x^2 \hat{i} + z \hat{j} + y \hat{k} \right) \cdot (\hat{-j}) \, dz \, dx$$

$$= \int_0^1\int_0^2 (-z) dz dx$$

$$= -2$$

##### Front

$$S_5: x = 1, \hat n = \hat i$$

$$\therefore dS_5 = dy dz$$

$$\int_{S_5} \vec F \cdot \hat{n} \, dS = \iint_{S_5} \left(\hat{i} + z \hat{j} + y \hat{k} \right) \cdot (\hat{i}) \, dy \, dz$$

$$\int_0^2\int_0^3 1 \, dy \, dz$$

$$= 6$$

##### Back

$$x = 0, \hat n = - \hat i$$

$$\therefore dS_5 = dy \, dz$$

$$\int_{S_6} \vec F \cdot \hat{n} \, dS = \iint_{S_6} \left(z \hat{j} + y \hat{k} \right) \cdot (\hat{-i}) \, dy \, dz$$

$$= \iint_{S_6} 0 dy \, dz = 0$$

$$\therefore \int_S \vec F \cdot dS = - \frac 9 2 + \frac 9 2 + 2 - 2 + 6 + 6 + 0 = 6$$

Hence, verified.

## Stoke's Theorem

If $\vec F$ is a `vector field` existing over a `surface` $S$ over a boundary $c$ then  

$$\int_S \nabla \times \vec F \cdot d \vec S = \oint_c \vec F \cdot d \vec r$$

### Example

A `hemisphere` $S$ is defined as $x^2 + y^2 + z^2 = 4$ where $z \ge 0$.  
A `vector field` $\vec F = 2y \hat i + x \hat j+ xz \hat k$ exists over the surface around its boundary $c$.  
Verify [stokes theorem](#stokes-theorem) on it.  

$$\int_S \nabla \times \vec F \cdot d \vec S = \oint_c \vec F \cdot d \vec r$$

$$S: x^2 + y^2 + z^2 - 4 = 0$$

$$c : x^2 + y^2 = 4$$

$$\vec F = 2y \hat i - x \hat j + xz \hat k$$

#### Right Hand Side

$$\oint_c \vec F \cdot d \vec r = \int_c (2y \hat i - x\hat j + xz \hat k) \cdot (\hat i dx + j \hat dy + \hat k dz)$$

$$= \int_c (2y dx - x dy + xz dz)$$

Converting coordinates into `polar coordinates`,[^4]  

$$\because x = 2 \cos (\theta) \implies dx = - 2 \sin(\theta)$$

$$\because y = 2 \sin (\theta) \implies 2 \cos(\theta)$$

$$\because z = 0$$

The bounds for $\theta$ will be  

$$\theta = 0, 2\pi$$

Therefore, our `integral`[^1] becomes  

$$= -4 \int_0^{2 \pi} (2 \sin^2(\theta) + \cos^2(\theta)) d\theta$$

$$= - 12 \pi$$

#### Left Hand Side

$$\int_S \nabla \times \vec F \cdot d \vec S = \int_S \nabla \times \vec F \cdot \hat n dS$$

$$\vec F = 2y \hat i - x \hat j + xz \hat k$$

$$\nabla \times \vec F = \left|\begin{matrix}\hat i & \hat j & \hat k \\\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\2y & -x & xz\end{matrix}\right|$$

$$= -z \hat j - 3 \hat k$$

$$\hat n = \frac{\nabla S}{\lvert \nabla S \rvert}$$

$$= \frac{2x \hat i + 2y \hat j + 2z \hat k}{\sqrt{4x^2 + 4y^2 = 4z^2}}$$

$$= \frac{x \hat i + y \hat j + z \hat k}{2}$$

$$\int_S \nabla \times \vec F \cdot \hat n dS = \int_S (-z \hat k - 3 \hat k) \cdot \left(\frac{x \hat i + y \hat j + z \hat k} 2\right) dS$$

$$= \frac 1 2 \int_S (- yz - 3z) dS$$

Converting the coordinates into `spherical coordinate system`.[^4]  

$$x = 2 \sin (\phi) \cos (\theta)$$

$$y = 2 \sin (\phi) \sin (\theta)$$

$$z = 2 \cos (\theta)$$

$$dS = 4 \sin (\phi) d\phi \, d \theta$$

$$\therefore \int_S \nabla \times \vec F \cdot \hat n dS = - \int_0^{2 \pi}\int_0^{\frac \pi 2}(2\sin^{2}(\phi) \cos(\phi) \sin(\theta)+3\sin(\phi) \cos(\phi))d\phi d\theta$$

$$-12 \pi$$

Hence, verified.

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/25. Integrations/Lecture|integrals]].
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/4. Lines/Lecture|lines]].
[^3]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/3. Coordinate Planes and Graphs/Lecture|planes]].
[^4]: Read more about [[semester 2/MTH301 - Calculus II/4. Polar coordinates/Lecture|other coordinate systems]].