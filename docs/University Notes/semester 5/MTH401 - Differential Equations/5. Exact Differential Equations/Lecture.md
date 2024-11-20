---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-08
---

<span style="color: gray;">Dated: 08-11-2024</span>

# Exact Differential Equation

$$
\frac{dy}{dx} = f(x, y)
$$

$$
f(x,y) = -\frac{M(x,y)}{N(x,y)}
$$

$$
M(x,y)dx + N(x,y)dy = 0
$$

This equation is `exact differential equation` if the following condition is satisfied

$$
\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}
$$

$$
\frac{\partial F}{\partial x} = M(x,y), \quad \frac{\partial F}{\partial y} = N(x,y)
$$

## Method of Solution

- Check the equation is `exact differential equation`.
- Write the system $\frac{\partial F}{\partial x} = M(x,y), \quad \frac{\partial F}{\partial y} = N(x,y)$.
- `Integrate`[^1] either the $1^{\text{st}}$ equation with respect to $x$ or $2^{\text{nd}}$ with respect to $y$. If we choose $1^{\text{st}}$ equation then

$$
F(x,y) = \int M(x,y)dx + \theta(y)
$$

The $\theta(y)$ is an arbitrary `function`.[^2]

- Use the $2^{\text{nd}}$ equation in step 2 and the equation from step 3 to find $\theta^\prime(y)$.

$$
\frac{\partial F}{\partial y} = \frac{\partial}{\partial y}\left(\int M(x,y)dx+\theta^{\prime}(y)\right) = N(x,y)
$$

$$
\theta^{\prime}(y) = N(x,y) - \frac{\partial}{\partial y}\int M(x,y)dx
$$

- `Integrate`[^1] $\theta^\prime(y)$ and write down the `function`[^2] $F(x, y)$.
- All solutions are given by implicit `function`[^2]  

$$F(x, y) = C$$

- If we are given the `initial value problem`[^3] then plugin the condition to find $C$.
- $x$ should disappear from $\theta^\prime(y)$ otherwise something is wrong.

## Example

$$\frac {dy}{dx} = - \frac{3x^2y + 2}{x^3 + y}$$

$$
(3x^{2}y+2)dx+(x^{3}+y)dy=0
$$

$$
M=3x^{2}y+2 \text{ and } N=x^{3}+y
$$

### Step 1

$$
\frac{\partial M}{\partial y} = 3x^{2}, \quad \frac{\partial N}{\partial x} = 3x^{2}
$$

$$
\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}
$$

### Step 2

$$
\frac{\partial f}{\partial x} = 3x^{2}y+2 = M
$$

$$
\frac{\partial f}{\partial y} = x^{3}+y = N
$$

### Step 3

`Integrating`[^2] $1^{\text{st}}$ equation with respect to $x$, we get 

$$
f(x,y)=x^{3}y+2x+h(y)
$$

### Step 4

Finding the `derivative`[^3] of the above `function`[^2] with respect to $y$.

$$
\frac{\partial f}{\partial y} = x^{3} + h^{\prime}(y) = x^{3} + y = N
$$

Following `function`[^2] is independent of $x$ 

$$h^\prime(y) = y$$

and `integrating`[^1] it, we get

$$
h(y)=\frac{y^{2}}{2}
$$

Thus

$$
f(x,y)=x^{3}y+2x+\frac{y^{2}}{2}
$$

### Step 5

$$
f(x,y)=c
$$

$$
x^{3}y+2x+\frac{y^{2}}{2}=c
$$

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[25. Integrations|integration]].
[^2]: Read more about [[notes_publisher/docs/Mathematics/Function/Content|functions]].
[^3]: Read more about [[15. The Derivative|derivatives]].