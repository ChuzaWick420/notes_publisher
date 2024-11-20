---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Examples

## Example

Evaluate $\int_v \vec F dv$ where $\vec F = 2 \hat i + 2z \hat j + y \hat k$ and $v$ is the region bounded by the `planes`[^1] $z = 0, 4$ and the `surface` $x^2 + y^2 = 9$.

### Solution

In this chase, it would be convenient for us to convert the coordinates into `polar coordinates`.[^2]  

$$\int_v \vec F dv = \iiint_v (2 \hat i + 2z \hat j + y \hat k) dxdydz$$

$$\because x = r \cdot \cos(\theta)$$

$$\because y = r \cdot \sin(\theta)$$

$$\because z = z$$

$$\because dv = r \cdot dr \cdot d\theta \cdot dz$$

$$= \int_0^{2 \pi} \int_0^3 \int_0^4 (2 \hat i + 2z \hat j + r \sin (\theta) \hat k) r \cdot dz \cdot dr \cdot \theta$$

$$= 72 \pi (\hat i + 2 \hat j)$$

## Scalar Fields

A `scalar field` $F = xyz$ exists over the `surface` $S$ $x^2 + y^2 = 4$ bounded by the `planes`[^1] $z = 0, 3$.  
Evaluate the following  

$$\int_S F \cdot d \vec S$$

$$\because d \vec S = \hat n \cdot \lvert \vec S \rvert$$

$$\therefore \hat n = \frac {\nabla S}{\lvert \nabla S \rvert}$$

$$\nabla S = \hat i \frac{\partial S}{\partial x} + \hat j \frac{\partial S}{\partial y} + \hat k \frac{\partial S}{\partial z} = 2x \hat i + 2y \hat j$$

$$\lvert \nabla S \rvert = \sqrt{(2x)^2 + (2y)^2} = 2 \sqrt {x^2 + y^2} = 2 \sqrt 4 = 4$$

$$\therefore \hat n = \frac {x \hat i + y \hat j}{2}$$

$$\therefore d \vec S = \hat n \cdot dS$$

$$d \vec S = \frac {x \hat i + y \hat j}{2} dS$$

$$\int_S F \cdot d \vec S = \int_S F \cdot \hat n \cdot dS$$

$$= \int_S xyz \cdot \frac {x \hat i + y \hat j}{2} dS$$

$$=\frac{1}{2}\int_{S}(x^{2}yz \hat i+xy^{2}z \hat j) dS$$

Now we will convert the coordinates into `polar coordinates`.[^2]

$$\because x = r \cdot \cos(\theta) = 2 \cos (\theta)$$

$$\because y = r \cdot \sin(\theta) = 2 \sin(\theta)$$

$$\because z = z$$

$$\because dS = r \cdot dz \cdot d \theta = 2 \cdot dz \cdot d\theta$$

$$\because x^{2}yz=(4 \cos^{2}(\theta))(2 \sin(\theta))(z)=8 \cos^{2}(\theta)\sin(\theta) z$$

$$\because xy^{2}z=(2\cos(\theta))(4\sin^{2}(\theta))(z)=8\cos(\theta )\sin^{2}(\theta) z$$

$$\therefore \int_S F \cdot dS = \frac 8 2 \int_0^{\frac \pi 2} \int_0^3 (\cos^2(\theta) \sin(\theta)\hat i + \cos(\theta)\sin(2 \theta) \hat j) 2zdzd\theta$$

$$= 12 (\hat i + \hat j)$$

## Vector Field

A `vector field` $\vec F = y \hat i+ 2 \hat j + \hat k$ exists over the `surface` $S$ defined by $x^2 + y^2+ z^2 = 9$ and bounded by $x = 0, y= 0, z= 0$ .  
Evaluate  

$$\int_S \vec F \cdot d \vec S$$

### Solution

$$d \vec S = \hat n \cdot \lvert \vec S \rvert$$

$$\hat n = \frac{\nabla S}{\lvert \nabla S \rvert}$$

$$S: x^2 + y^2 + z^2 - 9 = 0$$

$$\nabla S = \frac{\partial S}{\partial x} \hat i + \frac{\partial S}{\partial y} \hat j + \frac{\partial S}{\partial z} \hat k = 2x \hat i + 2 \hat j + 2 \hat k$$

$$\lvert \nabla S\rvert=\sqrt{4x^{2}+4y^{2}+4z^{2}}=2\sqrt{x^{2}+y^{2}+z^{2}}=2\sqrt{9}=6$$

$$\therefore \hat n = \frac 1 3 (x \hat i + y \hat j + z \hat k)$$

$$\int_S \vec F \cdot d \vec S = \int_S \vec F \cdot \hat n \cdot dS$$

$$= \int_S (y \hat i + 2 \hat j + \hat k) \cdot \frac 1 3 (x \hat i + y \hat j + z \hat k) dS$$

$$ = \frac 1 3 \int_S (xy + 2y + z) dS$$

Before `integrating`[^3] over the surface, we will convert the coordinates into `spherical coordinates`.[^2]  

$$x = 3 \sin (\phi) \cos (\theta)$$

$$y = 3 \sin (\phi) \sin (\theta)$$

$$z = 3 \cos(\phi)$$

$$dS = 9 \sin(\phi) d \phi d \theta$$

Both $\phi$ and $\theta$ are limited from $0$ to $\frac \pi 2$.  

$$\because xy=3 \sin (\phi)\cos(\theta) \cdot 3 \sin(\phi) \sin(\theta) = 9 \sin^{2}(\theta)\cos(\theta)$$

$$\because 2y=2\cdot3 \sin(\phi)\sin(\theta)=6\sin(\phi)\sin(\theta)$$

$$\because z = 3 \cos (\phi)$$

$$\because dS = 9 \sin(\phi) d \phi d \theta$$

Putting these values in the `integral`,[^3] we get  

$$\therefore \int_{S}\vec F \cdot d \vec S=\frac{1}{3}\int_{0}^{\frac \pi 2}\int_{0}^{\frac \pi 2}(9\sin^{2}(\phi) \sin(\theta) \cos(\theta)+6\sin(\phi) \sin(\theta)+3\cos(\phi))9\sin(\phi) d\phi d\theta$$

$$=9\left(1+\frac{3\pi}{4}\right)$$

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[3. Coordinate Planes and Graphs|planes]].
[^2]: Read more about [[semester 2/MTH301 - Calculus II/4. Polar coordinates/Lecture|other coordinate systems]].
[^3]: Read more about [[25. Integrations|integration]].