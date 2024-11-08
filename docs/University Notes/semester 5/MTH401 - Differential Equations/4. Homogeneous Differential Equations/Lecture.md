---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-08
---

<span style="color: gray;">Dated: 08-11-2024</span>

# Homogeneous Differential Equations

A differential equation of the form  

$$\frac{dy}{dx} = f(x, y)$$

is said to be `homogeneous` if $f(x, y)$ is `homogeneous` which means  

$$f(tx, ty) = t^n f(x, y)$$

where $t$ is any number and $n \in \mathbb R$.

## Example

Determine if the following `functions`[^1] are `homogeneous`.

$$
\begin{cases}
	f(x, y) = \frac{xy}{x^2 + y^2} \\
	g(x, y) = \ln\left(- \frac{3x^2y}{x^3 + 4xy^2}\right)
\end{cases}
$$

$f(x, y)$ is `homogeneous` because  

$$f(tx,ty)=\frac{t^{2}xy}{t^{2}(x^{2}+y^{2})}=\frac{xy}{x^{2}+y^{2}}=f(x,y)$$

$g(x, y)$ is also `homogeneous` because  

$$g(tx,ty)=\ln\left(\frac{-3t^{3}x^{2}y}{t^{3}(x^{3}+4xy^{2})}\right)=\ln\left(\frac{-3x^{2}y}{x^{3}+4xy^{2}}\right)=g(x,y)$$

Therefore, the differential equations

$$
\begin{cases}
	\frac{dy}{dx} = f(x, y) \\
	\frac{dy}{dx} = g(x, y)
\end{cases}
$$

are also `homogeneous differential equations`.

## Method of Solution

To solve `homogeneous differential equations`, we we will substitute the following in $f(x, y)$.  

$$v = \frac y x$$

If $f(x, y)$ is `homogeneous` of degree zero, we have.  

$$f(x, y) = f(1, v) = F(v)$$

$$\because y^\prime = xv^\prime + v$$

$$x\frac{dv}{dx}+v=f(1,v)$$

## Summary

- Identify if the equation is `homogeneous` or not.
- Use the substitution $v = \frac y x$.
- Solve $x\frac{dv}{dx}+v=f(1,v)$ to find $v$.
- Find $y$ through $v = \frac y x$.
- If we have an `initial value problem`,[^2] we need to use the initial condition to find the constant of `integration`.[^3]

## Example

$$\frac{dy}{dx}=\frac{-2x+5y}{2x+y}$$

### Step 1

Checking if the $f(x, y)$ is `homogeneous` or not.  

$$\because f(x, y) = \frac{-2x+5y}{2x+y}$$

$$f(tx,ty) = \frac{-2tx+5ty}{2tx+ty}$$

$$ = \frac {t(-2x + 5y)}{t(2x + y)}$$

$$=  \frac{-2x+5y}{2x+y}$$

$$= f(x, y)$$

Hence, $f(x, y)$ is `homogeneous`.

### Step 2

Substituting $v = \frac y x$ in the differential equation.  

$$xv^{\prime}+v=\frac{-2x+5xv}{2x+xv}=\frac{-2+5v}{2+v}$$

$$\frac{dv}{dx}=\frac{1}{x}\left(\frac{-2+5v}{2+v}-v\right)$$

### Step 3

The solutions are  

$$-4\ln(|v-2|)+3\ln|v-1|=\ln(|x|)+C$$

### Step 4

$$-4\ln|y-2x|+3\ln|y-x|=C$$

$$-4\ln\left|\frac{y-2x}{x}\right|+3\ln\left|\frac{y-x}{x}\right|=\ln|x|+c$$

$$\ln\left|\frac{y-2x}{x}\right|^{-4}+\ln\left|\frac{y-x}{x}\right|^{3}=\ln x+\ln c_{1}, c=\ln c_{1}$$

$$\ln\left|\frac{(y-2x)^{-4}}{x^{-4}}\right|+\ln\left|\frac{(y-x)^{3}}{x^{3}}\right|=\ln c_{1}x$$

$$\ln\left|\frac{(y-2x)^{-4}}{x^{-4}}\cdot\frac{(y-x)^{3}}{x^{3}}\right|=\ln c_{1}x$$

$$\frac{(y-2x)^{-4}}{x^{-4}}\cdot\frac{(y-x)^{3}}{x^{3}}=c_{1}x$$

$$(y-2x)^{-4}(y-x)^{3}=c_{1}$$

The implicit equation can be written as  

$$(y - x)^3 = C_1(y - 2x)^4$$

## Equations Reducible to Homogeneous Form

$$\frac{dy}{dx}=\frac{a_{1}x+b_{1}y+c_{1}}{a_{2}x+b_{2}y+c_{2}}$$

This equation is not `homogeneous` but can be reduced to one.

### Case 1

$$\frac {a_1}{b_1} = \frac {a_2}{b_2}$$

First, we will substitute $z = a_1x + b_1y$ which reduces to `separable equation`.[^4]  
After solving the `separable equation`,[^4] put the values of $z$ back.

### Case 2

$$\frac {a_1}{b_1} \ne \frac {a_2}{b_2}$$

In this case, we will substitute  

$$x = X + h, \quad y = Y + k$$

Then the equation becomes

$$
\frac{dY}{dX} = \frac{a_{1}X + b_{1}Y + a_{1}h + b_{1}k + c_{1}}{a_{2}X + b_{2}Y + a_{2}h + b_{2}k + c_{2}}
$$

Choose $h$ and $k$ such that 

$$
\begin{cases}
	a_{1}h + b_{1}k + c_{1} &= 0 \\
	a_{2}h + b_{2}k + c_{2} &= 0
\end{cases}
$$

This reduces to

$$
\frac{dY}{dX} = \frac{a_{1}X + b_{1}Y}{a_{2}X + b_{2}Y}
$$

This one is `homogeneous` and can be solved accordingly.

## Example

$$\frac{dy}{dx} = -\frac{2x + 3y - 1}{2x + 3y + 2}$$

$$\because \frac{a_1}{b_1} = \frac{a_2}{b_2} = 1$$

Substitute  

$$z = 2x + 3y$$

Original differential equation becomes

$$
\frac{dy}{dx} = \frac{1}{3}\left(\frac{dz}{dx} - 2\right)
$$

$$
\frac{1}{3}\left(\frac{dz}{dx} - 2\right) = -\frac{z - 1}{z + 2}
$$

$$
\frac{dz}{dx} = \frac{-z + 7}{z + 2}
$$

$$
\left(\frac{z + 2}{-z + 7}\right) dz = dx
$$

`Integrating`[^3] both sides, we will get

$$
-z - 9\ln(z - 7) = x + A
$$

Put values of $z$ back

$$
-ln(2x+3y-7)^{9} = 3x+3y+A
$$

$$
(2x+3y-7)^{-9} = ce^{3(x+y)}, \quad c = e^{A}
$$

## Example

$$
\frac{dy}{dx} = \frac{(x + 2y - 4)}{2x + y - 5}
$$

Substituting

$$
x = X + h, \quad y = Y + k
$$

Original different equation becomes

$$
\frac{dY}{dX} = \frac{(X + 2Y) + (h + 2k - 4)}{(2X + Y) + (2h + k - 5)}
$$

We choose $h$ and $k$ such that

$$
h + 2k - 4 = 0, \quad 2h + k - 5 = 0
$$

This gives us  

$$h = 2, k = 1$$

$$
\frac{dY}{dX} = \frac{X + 2Y}{2X + Y}
$$

$$
X \frac{dV}{dX} = \frac{1 - V^2}{2 + V}
$$

$$
\left[\frac{2 + V}{1 - V^2}\right] dV = \frac{dX}{X}
$$

`Integrating`[^3] both sides and we get

$$
\int\left[\frac{3}{2(1-V)} + \frac{1}{2(1+V)}\right] dV = \int\frac{dX}{X}
$$

$$
-\frac{3}{2}\ln(1-V) + \frac{1}{2}\ln(1+V) = \ln X + \ln A
$$

$$
\frac{(1-V)^3}{(1+V)} = CX^{-2}, \quad C = A^{-2}
$$

$$
-\frac{3}{2}ln(1-V)+\frac{1}{2}ln(1+V)=ln~X+ln~A
$$

$$
ln(1-V)^{-\frac{3}{2}}+ln(1+V)^{\frac{1}{2}}=ln~XA
$$

$$
ln(1-V)^{-\frac{3}{2}}(1+V)^{\frac{1}{2}}=ln~XA
$$

$$
(1-V)^{-\frac{3}{2}}(1+V)^{\frac{1}{2}}=XA
$$

Raising both sides to power of $-2$.

$$
(1-V)^3(1+V)^{-1} = X^{-2}A^{-2}
$$

Putting $V = \frac Y X$ back

$$
\left(1-\frac{Y}{X}\right)^{3}\left(1+\frac{Y}{X}\right)^{-1} = X^{-2}A^{-2}
$$

$$
\left(\frac{X-Y}{X}\right)^{3}\left(\frac{X+Y}{X}\right)^{-1} = X^{-2}A^{-2}
$$

$$
\frac{(X-Y)^{3}}{X+Y}X^{-3+1} = X^{-2}A^{-2}
$$

$$\because c = A^{-2}$$

$$c = \frac{(X - Y)^3}{X + Y}$$

Put $X = x - 2$ and $Y = y - 1$

$$
\frac {(x+y-1)^{3}}{x+y}-3=c
$$

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[notes_publisher/docs/Mathematics/Function/Content|functions]].
[^2]: Read more about [[notes_publisher/docs/University Notes/semester 5/MTH401 - Differential Equations/2. Fundamentals/Lecture|initial value problem]].
[^3]: Read more about [[notes_publisher/docs/University Notes/semester 1/MTH101 - Calculus and Analytical Geometry/25. Integrations/Lecture|integration]].
[^4]: Read more about [[notes_publisher/docs/University Notes/semester 5/MTH401 - Differential Equations/3. Separable Equations/Lecture|separable equations]].