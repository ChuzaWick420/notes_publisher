---
tags:
  - university-notes
  - gradient
  - vectors
university-name: Virtual University of Pakistan
---

# The Triple Scalar or Box Product
![[Pasted image 20241010124601.png]]  
The following is called the `triple scalar product`  

$$(\vec{A} \times \vec{B}) \cdot \vec{C} = \lvert \vec{A} \times \vec{B} \rvert \lvert \vec{C} \rvert \lvert \cos(\theta) \rvert$$

$$= 
\left|
\begin{matrix}
a_1 & a_2 & a_3 \\
b_1 & b_2 & b_3 \\
c_1 & c_2 & c_3 
\end{matrix}
\right|
$$

## Gradient of a Scalar `Function`[^1]

$$\nabla = \hat{i} \frac{\partial}{\partial x} + \hat{j} \frac{\partial}{\partial y} + \hat{k} \frac{\partial}{\partial z}$$

The $\nabla$ is called the `del operator`.  
It is also called `gradient` and operates on a `function`[^1].  
It returns us a `vector field` which is a `set`[^2] of `vectors`[^3] pointing towards the steepest change in the `function`[^1].

## Directional Derivative
If $f(x, y)$ is differentiable at $(x_0, y_0)$, and if $\vec{u} = (u_1, u_2)$ is a `unit vector`[^3], then the `directional derivative` of $f$ at $(x_0, y_0)$ in the direction of $\vec{u}$ is defined by  

$$D_{\vec{u}} f(x_0, y_0) = f_x(x_0, y_0) u_1 + f_y(x_0, y_0) u_2$$

> NOTE: There are infinite choices of $\vec{u}$ at the point $(x_0, y_0)$.

It can also be written as  

$$D_{\vec{u}} f(x, y) = \nabla f(x, y) \cdot \hat{u}$$

## Gradient of a `Function`[^1]
If $f(x, y)$ is a `function`[^1] then the `gradient` is defined as  

$$\nabla f(x, y) = f_x(x, y) \hat{i} + f_y(x, y) \hat{j}$$

### Properties of Gradient

$$D_{\vec{u}} f = \nabla f \cdot \hat{u} = \lvert \nabla f \rvert \cos (\theta)$$

1. $f$ _increases_ most rapidly in the direction of $\nabla f$, which means $\cos(\theta) = 1$ suggesting that _direction_ given by $\vec{u}$ is in the same direction of $\nabla f$.  

$$D_{\vec{u}} f = \lvert \nabla f \rvert \cos (0) = \lvert \nabla f \rvert$$
  
2. It _decreases_ most rapidly in direction of $- \nabla f$  

$$D_{\vec{u}} f = \lvert \nabla f \rvert \cos (\pi) = - \lvert \nabla f \rvert$$
  
3. There is no change if we move in direction _perpendicular_ to $\nabla f$.  

$$D_{\vec{u}} f = \lvert \nabla f \rvert \cos \left(\frac{\pi}{2}\right) = \lvert \nabla f \rvert \cdot 0 = 0$$

## Example
Imagine we have a `function`[^1]  

$$f(x, y) = x^2 + y^2$$
  
We are interested to know that at $(1, 1)$, in _which_ directions does this `function`[^1] most rapidly

1. increases
2. decreases

$$\frac{\partial}{\partial x} f(x, y) = f_x(x, y) = 2x$$

$$\frac{\partial}{\partial y} f(x, y) = f_y(x, y) = 2y$$

$$\nabla f(x, y) = 2x \hat i + 2y \hat j$$

$$\because \nabla f(x, y) \cdot \hat u = \lvert \nabla f(x, y) \rvert \cos(\theta)$$
  
Also

$$\because \lvert \nabla f(x, y) \rvert = 2 \sqrt{x^2 + y^2}$$

$$\therefore \lvert \nabla f(x, y) \rvert_{(1, 1)} = 2 \sqrt{1^2 + 1^2} = 2 \sqrt 2$$

$$\nabla f(x, y)_{(1, 1)} = 2 \hat i + 2 \hat j$$

### Increase
We get maximum increase in the direction of the `gradient`. Therefore, we need to find the `unit vector`[^3] for `gradient`.  

$$\hat u = \frac{2 \hat i + 2 \hat j}{2 \sqrt 2} = \frac{i + j}{\sqrt 2}$$

### Decrease
The decrease would be in opposite direction. Therefore,  

$$- \frac{i + j}{\sqrt 2}$$

## References
Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[Mathematics/Function/Content|functions]].
[^2]: Read more about [[Mathematics/Set/Content|sets]].
[^3]: Read more about [[semester 2/MTH301 - Calculus II/10. Introduction to vectors/Lecture|vectors]].
