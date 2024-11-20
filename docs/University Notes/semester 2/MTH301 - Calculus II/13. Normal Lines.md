---
tags:
  - university-notes
  - partial-differential
  - function
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Orthogonal Surfaces

## Normal line

If $P_0(x_, y_0, z_0)$ be any point on the `surface` $f(x, y, z) = 0$.  
If $f(x, y, z)$ is differentiable at $P_0$ then the `normal line` at $P_0$ has the equation  

$$x = x_0 + f_x(P_0)t$$

$$y = y_0 + f_y(P_0)t$$

$$z = z_0 + f_z(P_0)t$$

### Example

Find the `tangent plane`[^1] and `normal line` to the `surface`

$$f(x,y,z)=x^{2}+y^{2}+z^{2}-14$$

at  

$$P(1,-2,3)$$

#### Solution

$$f_x = 2x, \, f_x(P_0) = 2(1) = 2$$

$$f_y = 2y, \, f_y(P_0) = 2(-2) = -4$$

$$f_z = 2z, \, f_z(P_0) = 2(3) = 6$$

##### `Tangent Plane`[^1]

$$2(x-1)-4(y+2)+6(z-3)=0$$

$$x-2y+3z-14=0$$

##### Normal line

$$
\frac{x-1}{2}=\frac{y+2}{-4}=\frac{z-3}{6}
$$

Multiplying by $2$.

$$
\frac{x-1}{1}=\frac{y+2}{-2}=\frac{z-3}{3}
$$

## Orthogonal Surfaces

Two `surfaces` are called `orthogonal` if, at their point of intersection, `normals` of both are _orthogonal_.

### Condition

Imagine we have 2 `surfaces`  

$$f(x, y, z) = 0$$

$$g(x, y, z) = 0$$

Their `normals` are  

$$\vec{n_1} = f_x \hat i + f_y \hat j + f_z \hat k$$

$$\vec{n_2} = g_x \hat i + g_y \hat j + g_z \hat k$$

Using the `dot product`[^2] definition  

$$\vec{n_1} \cdot \vec{n_2} = 0$$

$$f_{x}g_{x}+f_{y}g_{y}+f_{z}g_{z}=0$$

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 2/MTH301 - Calculus II/12. Tangent Planes to the surfaces/Lecture|tangent lines]].
[^2]: Read more about [[semester 2/MTH301 - Calculus II/10. Introduction to vectors/Lecture|vectors]].