---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-08
---

<span style="color: gray;">Dated: 08-11-2024</span>

# Integrating Factor Technique

If the following equation is not exact 

$$
M(x,y)dx+N(x,y)dy=0
$$

then 

$$
\frac{\partial M}{\partial y} \ne \frac{\partial N}{\partial x}
$$

Therefore, we will look for a `function`[^1] $u(x, y)$ such that

$$
u(x,y)M(x,y)dx+u(x,y)N(x,y)dy=0
$$

This `function`[^1] $u(x, y)$ is called the `integrating factor`.

$$
\frac{\partial M}{\partial y}u+\frac{\partial u}{\partial y}M=\frac{\partial N}{\partial x}u+\frac{\partial u}{\partial x}N
$$

## Example

Show that the following  

$$\frac 1 {(x^2 + y^2)}$$

is an `integrating factor` for the following

$$
(x^{2}+y^{2}-x)dx-ydy=0
$$

$$
M = x^{2}+y^{2}-x, \quad N = -y
$$

$$
\frac{\partial M}{\partial y} = 2y, \quad \frac{\partial N}{\partial x} = 0
$$

$$
\frac{\partial M}{\partial y} \ne \frac{\partial N}{\partial x}
$$

If we multiply the following

$$\frac 1 {(x^2 + y^2)}$$

then the following equation is exact.

$$
\left(1-\frac{x}{x^2+y^2}\right)dx-\frac{y}{x^2+y^2}dy=0
$$

Checking again

$$
M=1-\frac{x}{x^{2}+y^{2}} \text{ and } N=-\frac{y}{x^{2}+y^{2}}
$$

$$
\frac{\partial M}{\partial y}=\frac{2xy}{(x^{2}+y^{2})^{2}}=\frac{\partial N}{\partial x}
$$

We can write the original equation as

$$
dx-\frac{xdx+ydy}{x^{2}+y^{2}}=0
$$

$$
dx-\frac{1}{2}d\left[\ln(x^{2}+y^{2})\right]=0
$$

$$
d\left[x-\frac{\ln(x^{2}+y^{2})}{2}\right]=0
$$

By `integration`,[^2] we have

$$
x-\ln\sqrt{x^{2}+y^{2}}=k
$$

### Case 1

If the given expression

$$
\frac{\frac{\partial M}{\partial y}-\frac{\partial N}{\partial x}}{N}
$$

is a `function`[^1] of $x$ only then the `integrating factor` $u(x, y)$ is given by

$$
u = \exp\left(\int \frac{\frac{\partial M}{\partial y}-\frac{\partial N}{\partial x}}{N}dx\right)
$$

### Case 2

If the given expression

$$
\frac{\frac{\partial N}{\partial x}-\frac{\partial M}{\partial y}}{M}
$$

is a `function`[^1] of $y$ only then the `integrating factor` $u(x, y)$ is given by

$$
u = \exp\left(\int \frac{\frac{\partial N}{\partial x}-\frac{\partial M}{\partial y}}{M}dy\right)
$$

### Case 3

If the given equation is `homogeneous`[^3] and  

$$xM + yN \ne 0$$

then

$$
u=\frac{1}{xM+yN}
$$

### Case 4

If the equation is of the form

$$
yf(xy)dx+xg(xy)dy=0
$$

and

$$
xM-yN\ne0
$$

then

$$
u=\frac{1}{xM-yN}
$$

Once $u(x, y)$ is found, multiply the old equation by $u(x, y)$ to get a new one which is exact.  
Solve it and write the solution.

## Summary

- Write the equation in the form

$$
M(x,y)dx+N(x,y)dy=0
$$

- Check the exactness by

$$
\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}
$$

- If the equation is not exact then evaluate

$$
\frac{\frac{\partial M}{\partial y}-\frac{\partial N}{\partial x}}{N}
$$

If the result is a `function`[^1] of only $x$ then

$$
u(x) = \exp\left(\int \frac{\frac{\partial M}{\partial y}-\frac{\partial N}{\partial x}}{N}dx\right)
$$

otherwise evaluate

$$
\frac{\frac{\partial N}{\partial x}-\frac{\partial M}{\partial y}}{M}
$$

If the result is a `function`[^1] of only $y$ then

$$
u(y)=\exp\left(\int\frac{\frac{\partial N}{\partial x}-\frac{\partial M}{\partial y}}{M}dy\right)
$$

- Test if the equation is `homogeneus`[^3] and 

$$
xM+yN\ne0
$$

then

$$
u=\frac{1}{xM+yN}
$$

- Test if the equation is of the form

$$
yf(xy)dx+xg(xy)dy=0
$$

and 

$$
xM-yN\ne0
$$

then

$$
u=\frac{1}{xM-yN}
$$

- Multiply the old equation by $u$ to get a new one.
- Solve the new equation.

## Example

$$
\frac{dy}{dx}=-\frac{3xy+y^{2}}{x^{2}+xy}
$$

### Step 1

Rewriting the equation

$$
(3xy+y^{2})dx+(x^{2}+xy)dy=0
$$

$$
M(x,y)=3xy+y^{2}
$$

$$
N(x,y)=x^{2}+xy
$$

### Step 2

$$
\frac{\partial M}{\partial y}=3x+2y, \quad \frac{\partial N}{\partial x}=2x+y
$$

$$
\therefore \quad \frac{\partial M}{\partial y}\ne\frac{\partial N}{\partial x}
$$

### Step 3

$$
\frac{\frac{\partial M}{\partial y}-\frac{\partial N}{\partial x}}{N}=\frac{1}{x}
$$

### Step 4

$$
u(x)=e^{\int\frac{1}{x}dx}=e^{ln(x)}=x
$$

### Step 5

$$
(3x^{2}y+xy^{2})dx+(x^{3}+x^{2}y)dy=0
$$

### Step 6

$$
\frac{\partial M}{\partial y}=3x^{2}+2xy=\frac{\partial N}{\partial x}
$$

### Step 7

$$
\begin{cases}
\frac{\partial F}{\partial x}=3x^{2}y+xy^{2}\\
\frac{\partial F}{\partial y}=x^{3}+x^{2}y
\end{cases}
$$

### Step 8

$$
F(x,y)=x^{3}y+\frac{x^{2}}{2}y^{2}+\theta(y)
$$

### Step 9

$$
\frac{\partial F}{\partial y}=x^{3}+x^{2}y+\theta'(y)=x^{3}+x^{2}y
$$

Because $\theta^\prime(y)$ is independent of $x$.

$$\theta^\prime = 0$$

### Step 10

`Integration`[^2] with respect to $y$, we get

$$
F(x,y)=x^{3}y+\frac{x^{2}}{2}y^{2}
$$

### Step 11

$$\because F(x, y) = C$$

$$
x^{3}y+\frac{x^{2}y^{2}}{2}=C
$$

> [!note]- Note  
> It is possible that the `integrating factors` may not be unique.

# References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[notes_publisher/docs/Mathematics/Function/Content|functions]].
[^2]: Read more about [[25. Integrations|integration]].
[^3]: Read more about [[notes_publisher/docs/University Notes/semester 5/MTH401 - Differential Equations/4. Homogeneous Differential Equations/Lecture|homogeneous differential equations]].