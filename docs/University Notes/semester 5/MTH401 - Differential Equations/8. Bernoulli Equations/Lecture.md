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

## Example

$$y(1+2xy)dx+x(1-2xy)dy=0$$

This equation is not 
- `Separable`[^3]
- `Homogeneous`[^4]
- `Exact`[^5]
- `Linear`[^1]
- `Bernoulli`[^6]

After staring long enough, we notice that  

$$u = 2xy$$

$$y = \frac u {2x}$$

$$\because dy = \frac{xdu - udx}{2x^2}$$

$$2u^2dx+(1-u)xdu=0$$

$$2\ln|x|-u^{-1}-\ln|u|=c$$

$$\ln|\frac{x}{2y}|=c+\frac{1}{2xy}$$

$$\frac{x}{2y}=c_{1}e^{\frac 1 {2xy}}$$

$$x=2c_{1}ye^{\frac 1 {2xy}}$$

## Example

$$\frac{d^{2}y}{dx^{2}}=2x\left(\frac{dy}{dx}\right)^{2}$$

$$u = y^\prime$$

$$\frac{du}{dx}=y^{\prime\prime}$$

$$\frac{du}{dx}=2xu^2$$

$$\frac{du}{u^2}=2xdx$$

$$\int u^{-2}du=\int 2xdx$$

$$-u^{-1}=x^2+c_1$$

$$u^{-1}=\frac{1}{y'}$$

$$\frac{dy}{dx}=-\frac{1}{x^{2}+c_{1}^{2}}$$

$$dy=-\frac{dx}{x^{2}+c_{1}^{2}}$$

$$\int dy=-\int \frac{dx}{x^{2}+c_{1}^{2}}$$

$$y+c_{2}=-\frac{1}{c_{1}}\tan^{-1}\frac{x}{c_{1}}$$

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[notes_publisher/docs/University Notes/semester 5/MTH401 - Differential Equations/7. First Order Linear Equation/Lecture|first order differential equation]].
[^2]: Read more about [[15. The Derivative|differentiation]].
[^3]: Read more about [[notes_publisher/docs/University Notes/semester 5/MTH401 - Differential Equations/3. Separable Equations/Lecture|separable equations]].
[^4]: Read more about [[notes_publisher/docs/University Notes/semester 5/MTH401 - Differential Equations/4. Homogeneous Differential Equations/Lecture|homogeneous differential equations]].
[^5]: Read more about [[notes_publisher/docs/University Notes/semester 5/MTH401 - Differential Equations/5. Exact Differential Equations/Lecture|exact differential equations]].
[^6]: Read more about [[notes_publisher/docs/University Notes/semester 5/MTH401 - Differential Equations/8. Bernoulli Equations/Lecture|bernoulli equation]].