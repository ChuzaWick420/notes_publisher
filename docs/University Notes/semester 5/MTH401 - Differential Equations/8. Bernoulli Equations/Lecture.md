---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-10
---

<span style="color: gray;">Dated: 10-11-2024</span>

# Bernoulli Equations

Any differential equation of the form  

$$\frac{dy}{dx}+p(x)y=q(x)y^n$$

is called `Bernoulli equation`.

## Method of Solution

- For $n = 0, 1$, the equation reduces to `first order linear differential equation`.[^1]
- For $n \ne 0, 1$ we divide by $y^n$  

$$y^{-n}\frac{dy}{dx}+p(x)y^{1-n}=q(x)$$

- Substitute  

$$v=y^{1-n}$$

- `Differentiate`[^2] with respect to $x$.  

$$v^\prime=(1-n)y^{-n}y^\prime$$

$$\frac{dv}{dx}+(1-n)p(x)v=(1-n)q(x)$$

After solving, we will get  

$$y=v^{\frac{1}{1-n}}$$

if $n > 0$ then we will add $y = 0$ to the solution.

## Example

$$\frac{dy}{dx}=y+y^3 \quad p(x) = -1, q(x) = 1, n = 3$$

### Step 1

$$\frac{dy}{dx}-y=y^3$$

### Step 2

Dividing by $y^3$  

$$y^{-3}\frac{dy}{dx}-y^{-2}=1$$

### Step 3

$$v=y^{1-3}=y^{-2}$$

### Step 4

$$y^{-3}\frac{dy}{dx}=-\frac{1}{2}\left(\frac{dv}{dx}\right)$$

$$\frac{dv}{dx}+2v=-2$$

### Step 5

$$u(x)=e^{\int2dx}=e^{2x}$$

### Step 6

$$v=\frac{\int u(x)q(x)dx+c}{u(x)}=\frac{\int e^{2x}(-2)dx+c}{e^{2x}}$$

$$\because \int e^{2x}(-2)dx=-e^{2x}$$

$$v=\frac{-e^{2x}+C}{e^{2x}}=Ce^{-2x}-1$$

### Step 7

$$y=\pm(Ce^{-2x}-1)^{-\frac{1}{2}}$$

Therefore the solutions are

$$
\begin{cases}
	y=0 \\
	y=\pm(Ce^{-2x}-1)^{-\frac{1}{2}}
\end{cases}
$$

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[notes_publisher/docs/University Notes/semester 5/MTH401 - Differential Equations/7. First Order Linear Equation/Lecture|first order differential equation]].
[^2]: Read more about [[notes_publisher/docs/University Notes/semester 1/MTH101 - Calculus and Analytical Geometry/15. The Derivative/Lecture|differentiation]].