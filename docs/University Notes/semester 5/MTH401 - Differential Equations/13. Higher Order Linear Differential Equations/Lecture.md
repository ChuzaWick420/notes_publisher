---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date:
---

<span style="color: gray;">Dated: 15-11-2024</span>

# High order Linear Differential Equations

The equations of the form

$$
a_{n}(x)\frac{d^{n}y}{dx^{n}}+a_{n-1}(x)\frac{d^{n-1}y}{dx^{n-1}}+\cdot\cdot\cdot+a_{1}(x)\frac{dy}{dx}+a_{0}(x)y=g(x)
$$

or

$$
a_{n}(x)y^{(n)}+a_{n-1}(x)y^{(n-1)}+\cdot\cdot\cdot+a_{1}(x)y^\prime+a_{0}(x)y=g(x)
$$

where $a_0(x), a_1(x), \ldots, a_n(x), g(x)$ are `functions`,[^1] are called `higher order linear differential equations` with variable coefficients.  
First, we will study the ones with constant coefficients which look like

$$
a_{n}\frac{d^{n}y}{dx^{n}}+a_{n-1}\frac{d^{n-1}y}{dx^{n-1}}+\cdot\cdot\cdot+a_{1}\frac{dy}{dx}+a_{0}y=g(x)
$$

if $g(x) = 0$ then this equation is called `associated homogeneous differential equation`.

## Initial Value Problem

Solve

$$
a_{n}(x)\frac{d^{n}y}{dx^{n}}+a_{n-1}(x)\frac{d^{n-1}y}{dx^{n-1}}+\cdot\cdot\cdot+a_{1}(x)\frac{dy}{dx}+a_{0}(x)y=g(x)
$$

Subject to the following arbitrary constants called the initial conditions

$$y(x_0) = y_0, y^\prime(x_0) = y^\prime_0, \ldots y^{n-1}(x) = y_0^{n - 1}$$

is called the `initial value problem`.

### Solution

A `function`[^1] satisfying the `differential equation` on $I$ whose graph passes through $(x_0, y_0)$ such that the `slope`[^2] of the curve at the point is the number $y_0^\prime$ is called solution of the `initial value problem`.

#### Theorem

Let the `variable coefficients` be `continuous`[^3] over the interval $I$ and let $a_n(x) \ne 0, \forall x \in I$.  
If $x = x_0 \in I$ then a solution $y(x)$ of the `initial value problem` exists on $I$ and is unique.

#### Example

Consider the `function`[^1]  

$$y = cx^2 + x + 3$$

With `initial value problem`

$$
x^2y^{\prime\prime}-2xy^{\prime}+2y=6
$$

$$y(0) = 3, y^\prime(0) = 1$$

Then  

$$y^\prime = 2cx + 1$$

and  

$$y^{\prime\prime} = 2c$$

Therefore,

$$
x^2y^{\prime\prime}-2xy^{\prime}+2y=x^2(2c)-2x(2cx+1)+2(cx^2+x+3)
$$

$$
=2cx^2-4cx^2-2x+2cx^2+2x+6
$$

$$= 6$$

Also  

$$y(0) = 3 \implies c(0) + 0 + 3 = 3$$

and  

$$y^\prime(0) = 1 \implies 2c(0) + 1 = 1$$

So for any choice of $c$, the $y(x)$ satisfied the differential equation and initial conditions.  
Therefore the solution to the equation is not unique.

##### Note that

- The equation is `linear differential equation`.[^4]
- The coefficients being polynomials are `continuous`[^3] everywhere.
- The `function`[^1] being constant is constant everywhere.
- The leading coefficient $a_2(x) = x^2 = 0$ at $x = 0 \in (-\infty, \infty)$.

Hence $a_2(x)$ brought non uniqueness in the solution.

## Boundary Value Problem (BVP)

For a 2nd order linear differential equation the problem of solving

$$
a_{2}(x)\frac{d^{2}y}{dx^{2}}+a_{1}(x)\frac{dy}{dx}+a_{0}(x)y=g(x)
$$

subject to following `boundary conditions`  

$$y(a) = y_0, \quad y(b) = y_1$$

is called a `boundary value problem`.

### Solution

A solution of the `boundary value problem` is a `function`[^1] satisfying the `differential equation` on some `interval`[^5] $I$ , containing $a$ and $b$, whose graph passes through two points $(a, y_0)$ and $(b, y_1)$.

#### Example

Consider the `function`[^1]  

$$y=3x^2-6x+3$$

We can prove that this `function`[^1] is the solution to following `boundary value problem`  

$$x^2y^{\prime\prime}-2xy^\prime+2y=6$$

$$y(1) = 0, y(2) = 3$$

Since  

$$\frac {dy}{dx} = 6x - 6$$

and  

$$\frac {d^2y}{dx^2} = 6$$

Therefore,  

$$x^2\frac{d^2y}{dx^2}-2x\frac{dy}{dx}+2y=6x^2-12x^2+12x+6x^2-12x+6=6$$

Also  

$$y(1) = 3 - 6 + 3 = 0$$

$$y(2) = 12 - 12 + 3 = 3$$

Therefore, $y(x)$ satisfies both, the `differential equation` and `boundary conditions`.

### Possible Boundary Conditions

- $$y(a) = y_0, \quad y(b) = y_1$$

- $$y^\prime(a) = y^\prime_0, \quad y(b) = y_1$$

- $$y(a) = y_0, \quad y^\prime(b) = y^\prime_1$$

- $$y^\prime(a) = y^\prime_0, \quad y^\prime(b) = y^\prime_1$$

### In General

The above possible `boundary conditions` are just a special case of the general boundary conditions  

$$\alpha_1y(a) + \beta_1y^\prime(a) = \gamma_1$$

$$\alpha_2y(a) + \beta_2y^\prime(a) = \gamma_2$$

where  

$$\alpha_1, \alpha_2, \beta_1, \beta_2 \in \{0, 1\}$$

> [!NOTE] A `boundary value problem` may have  
> Several Solutions  
> A unique solution  
> No solution at all

### Example 1

Consider the `function`[^1]  

$$y = c_1\cos (4x) + c_2 \sin (4x)$$

and the `boundary value problem`  

$$y^{\prime\prime} + 16 y = 0, y(0) = 0, y\left(\frac \pi 2 \right) = 0$$

Then  

$$y^{\prime} = -4c_1 \sin 4x + 4c_2 \cos 4x$$

$$y^{\prime\prime} = -16(c_1 \cos 4x + c_2 \sin 4x)$$

$$y^{\prime\prime} = -16y$$

$$y^{\prime\prime} + 16y = 0$$

Therefore, the `function`[^1] satisfied the differential equation.  
Apply the condition  

$$y(0) = 0$$

We obtain  

$$0 = c_1 \cos 0 + c_2 \sin 0$$

$$\implies c_1 = 0$$

So that  

$$y = c_2 \sin (4x)$$

But when we apply the 2nd condition  

$$y\left(\frac \pi 2\right) = 0$$

We have  

$$0 = c_2 \sin (2 \pi)$$

$$\because \sin(2 \pi) = 0$$

The condition is satisfied for any choice of $c_2$.  
Solution is  

$$y = c_2 \sin (4 \pi)$$

Hence there are an _infinite_ number of solutions for the boundary value problem.

### Example 2

Solve  

$$y^{\prime\prime} + 16y = 0$$

$$y(0) = 0, y\left(\frac \pi 8\right) = 0$$

#### Solution

From the previous example, we know the following `function`[^1] satisfied the problem

$$y = c_1\cos (4x) + c_2 \sin (4x)$$

Apply the conditions  

$$y(0) = 0 \implies 0 = c_1 + 0$$

$$y\left(\frac \pi 8\right) = 0 \implies 0 = c_2 + 0$$

So  

$$c_1 = c_2 = 0$$

Therefore, the only solution is  

$$y = 0$$

### Example 3

Same problem as previous one but with conditions  

$$y(0) = 0, y \left(\frac \pi 2\right) = 1$$

For the $y(0)$, it is same, $c_1 = 0$.  
So that  

$$y = c_2 \sin(4x)$$

But  

$$y\left(\frac \pi 2\right) = 1$$

$$\implies c_2 \sin(2 \pi) = 1$$

$$\because \sin(2 \pi) = 0$$

But  

$$c_2 \cdot 0 = 1$$

which is a contradiction, hence there is no solution.

## Linear Dependence

A `set`[^6] of `functions`[^1]  

$$\{f_1(x), f_2(x), \ldots, f_n(x)\}$$

is said to be `linearly dependent` on an `interval`[^5] $I$ if there exists constants $c_1, c_2, \ldots, c_n$ not all zeros such that  

$$c_1f_1(x)+c_2f_2(x)+\cdots+c_nf_n(x)=0, \quad \forall x \in I$$

## Linear Independence

Same thing as `linear dependence` but only when  

$$c_1 = c_2 = \cdots = c_n = 0$$

## Case of Two Functions

If $n = 2$ then the `set`[^6] of `functions`[^1] becomes  

$$\{f_1(x), f_2(x)\}$$

If we suppose that  

$$c_1f_1(x)+c_2f_2(x)=0$$

and that the `functions`[^1] are `linearly dependent` on an `interval`[^5] $I$ then either $c_1 \ne 0$ or $c_2 \ne 0$.  
Let us assume that $c_1 \ne 0$ then  

$$f_1(x) = - \frac{c_2}{c_1}f_2(x)$$

Conversely, if we suppose  

$$f_1(x) = c_2f_2(x)$$

Then  

$$(-1)f_{1}(x)+c_{2}f_{2}(x)=0, \quad \forall x \in I$$

So that the functions are `linearly dependent` because $c_1 = -1$.

### Conclusion

- $f_1(x)$ and $f_2(x)$ are `linearly dependent` on an `interval`[^5] $I$ if and only if one is the constant multiple of other.
- $f_1(x)$ and $f_2(x)$ are `linearly independent` on an `interval`[^5] $I$ if neither is the constant multiple of other.
- In general, a `set`[^6] of $n$ `functions`[^1] is linearly dependent if at least one of them can be expressed as a linear combination of the remaining.

### Example

Consider the `functions`[^1]  

$$f_{1}(x)=1+x, \quad \forall x \in (-\infty, \infty)$$

$$f_{2}(x)=x, \quad \forall x \in (-\infty, \infty)$$

$$f_{3}(x)=x^{2}, \quad \forall x \in (-\infty, \infty)$$

Then  

$$c_1f_1(x)+c_2f_2(x)+c_3f_3(x)=0$$

means that  

$$c_1(1+x)+c_2x+c_3x^2 = 0$$

or  

$$c_1+(c_1+c_2)x+c_3x^2 = 0$$

Equating the coefficients of $x$ and $x^2$ constant terms, we obtain  

$$c_1=0=c_3$$

$$c_1+c_2=0$$

Therefore  

$$c_1=c_2=c_3=0$$

This shows that they all are `linearly dependent`.

## Wronskian

Suppose the `functions`[^1] $f_1(x), f_2(x), \ldots, f_n(x)$ possess at least $n - 1$ derivatives then the following `determinant` is called `wronskian` of `functions`.[^1]

$$
\begin{vmatrix}
	f_1 & f_2 & \cdots & f_n \\
	f_1' & f_2' & \cdots & f_n' \\
	\vdots & \vdots & \ddots & \vdots \\
	f_1^{(n-1)} & f_2^{(n-1)} & \cdots & f_n^{(n-1)} 
\end{vmatrix}
$$

and is denoted by  

$$W(f_1(x), f_2(x), \ldots, f_n(x))$$

## Theorem

The `functions`[^1] $f_1(x), f_2(x), \ldots, f_n(x)$ are `linearly independent` on the `interval`[^5] $I$ if for at least one point on $I$ such that

$$W(f_1(x), f_2(x), \ldots, f_n(x)) \ne 0$$

Also if

$$W(f_1(x), f_2(x), \ldots, f_n(x)) = 0$$

then they are `linearly dependent` but the converse of this is not true.

### Example

The following `functions`[^1] are `linearly dependent`

$$f_{1}(x)=\sin^{2}x$$

$$f_{2}(x)=1-\cos2x$$

because  

$$\sin^{2}x=\frac{1}{2}(1-\cos2x)$$

We observe that for all $x \in (-\infty, \infty)$

$$
W(f_1(x), f_2(x)) = 
\begin{vmatrix}
	\sin^2(x) & 1 - \cos(2x) \\
	2 \sin(x) \cos(x) & 2 \sin(2x)
\end{vmatrix}
$$

$$=2\sin^{2}x\sin2x-2\sin x\cos x+2\sin x\cos x\cos2x$$

$$=\sin2x[2\sin^{2}x-1+\cos2x]$$

$$=\sin2x[2\sin^{2}x-1+\cos^{2}x-\sin^{2}x]$$

$$=\sin2x[\sin^{2}x+\cos^{2}x-1]$$

$$=0$$

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[notes_publisher/docs/Mathematics/Function/Content|functions]].
[^2]: Read more about [[4. Lines|slopes]].
[^3]: Read more about [[12. Continuity|continuous]].
[^4]: Read more about [[notes_publisher/docs/University Notes/semester 5/MTH401 - Differential Equations/7. First Order Linear Equation/Lecture|linear differential equations]].
[^5]: Read more about [[notes_publisher/docs/University Notes/semester 1/MTH101 - Calculus and Analytical Geometry/1. Coordinates, Graphs, Lines/Lecture|intervals]].
[^6]: Read more about [[notes_publisher/docs/Mathematics/Set/Content|sets]].