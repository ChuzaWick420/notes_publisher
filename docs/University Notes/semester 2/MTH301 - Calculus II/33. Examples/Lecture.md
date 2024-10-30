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

Evaluate the following from $A(1, 2)$ to $B(3, 5)$  

$$I = \int_c(3ydx + (3x + 2y)dy)$$

### Solution

From the inspection, we notice that the `integrant`[^1] is in the following pattern

$$P dx + Q dy$$

$$\because P = \frac{\partial z}{\partial x} = 3y \therefore \frac{\partial P}{\partial y} = 3$$

$$\because Q = \frac{\partial z}{\partial y} = 3x + 2y \therefore \frac{\partial Q}{\partial x} = 3$$

$$\because \frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x}$$

This is an `exact differential`.[^2]  

$$\therefore I = \int_c dz$$

So now, we need to find what that $z$ is.  

$$P = \int 3y dx = 3xy + f(y)$$

$$Q = \int (3x + 2y) dy = 3xy + y^2 + g(x)$$

comparing $P$ and $Q$, we get  

$$z = 3xy + y^2$$

$$\therefore I = \int_{(1, 2)}^{(3, 5)} d (3xy + y^2)$$

$$= \left[3xy + y^2\right]^{(3, 5)}_{(1, 2)}$$

$$= 60$$

## Theorem

If $P dx + Q dy$ is an `exact differential`[^2] then

1. $I = \int_c (Pdx + Qdy)$ is independent of the path of `integration`[^1]
2. $I = \oint_c (Pdx + Qdy) = 0$

## Green's Theorem

Let $P(x)$ and $Q(y)$ be `continuous functions`[^3] within the region $R$ including its boundary $c$.  
If its first `partial derivatives`[^4] are `continuous` then  

$$\iint_R\left(\frac{\partial P}{\partial y} - \frac{\partial Q}{\partial x}\right) dx dy = - \oint_C (P dx + Q dy)$$

## Example

Evaluate the following at `vertices` $O(0, 0)$, $A(1, 0)$ and $B(1, 2)$  

$$I = \oint (2x + y)dx + (3x - 2y)dy$$

### Solution

#### By Previous Method

##### $c_1$

$$c_1 : y = 0 \therefore dy = 0$$

$$I_{c_1}=\int_{0}^{1}2xdx=\left[x^{2}\right]_{0}^{1}=1$$

##### $c_2$

$$c_2 : x = 1 \therefore dx = 0$$

$$I_{c_2}=\int_{0}^{2}(3-2y)dy=\left[3y-y^{2}\right]_{0}^{1}=2$$

##### $c_3$

$$c_3 : y = 2x \therefore dy = 2$$

$$I_{c_3}=\int_{1}^{0}\{4xdx+(3x-4x)2dx\}$$

therefore  

$$I = I_{c_1} + I_{c_2} + I_{c_3} = 2$$

#### By Green's Theorem

$$I = \oint (2x + y)dx + (3x - 2y)dy$$

$$P = 2x + y \therefore \frac{\partial P}{\partial y} = 1$$

$$Q = 3x - 2y \therefore \frac{\partial Q}{\partial y} = 3$$

$$I=-\iint_{R}\left(\frac{\partial P}{\partial y}-\frac{\partial Q}{\partial x}\right)dxdy$$

$$I = 2 \iint_R dxdy = 2 A$$

Here $A$ is the `area` of the `triangle`.  

$$\because \text{Area} = 1$$

$$I = 2$$

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/25. Integrations/Lecture|integrals]].
[^2]: Read more about [[semester 2/MTH301 - Calculus II/30. Exact Differential/Lecture|exact differentials]].
[^3]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/12. Continuity/Lecture|continuity]].
[^4]: Read more about [[semester 2/MTH301 - Calculus II/6. Geometry of continuous functions/Lecture|partial derivatives]].