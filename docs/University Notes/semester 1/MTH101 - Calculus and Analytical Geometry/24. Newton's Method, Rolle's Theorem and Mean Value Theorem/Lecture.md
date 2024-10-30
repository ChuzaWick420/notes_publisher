---
tags:
  - university-notes
  - tangent
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Newton's Method, Rolle's Theorem and Mean Value Theorem

## Newton's Method for Approximating Solutions for $f(x) = 0$

Let us first describe what does $f(x) = 0$ even means.  
It means we are looking for those values of $x$ where $f(x) = y = 0$.  
These are the values where the graph of `function`[^1] crosses the `x axis`.

They way it works is as follows:

1. Choose an arbitrary $x_1$.
2. Draw the `tangent` to $f(x_1)$
3. If the `tangent` is not parallel to `x axis` i.e. $f^{\prime}(x_1) \ne 0$ then then `tangent` line intercepts at `x axis` at $(x_2, 0)$.
4. Select $x_2$ and repeat from Step 2 until the new $x$ values slowly seem to approach a certain value.  
![[Pasted image 20240923163535.png]]  
We start with $x_1$.  
To draw `tangent` at $f(x_1)$, we are going to use the definition of `slope`.  

$$m = f^{\prime}(x_1)$$

$$run = x_2 - x_1$$

$$rise = 0 - f(x_1)$$

$$\because m = \frac{rise}{run}$$

$$f^{\prime}(x_1) = \frac{0 - f(x_1)}{x_2 - x_1}$$

$$f^{\prime}(x_1) \cdot (x_2 - x_1) = -f(x_1)$$

$$x_2 - x_1 = \frac{-f(x_1)}{f^{\prime}(x_1)}$$

$$x_2 = x_1 - \frac{f(x_1)}{f^{\prime}(x_1)}$$

Then we can generalize the equation from here  

$$x_{n+1} = x_n - \frac{f(x_n)}{f^{\prime}(x_n)}$$

### Limitations

- Does not always work.
- It might involve division by $0$. Hence rendering us unable to continue the process. This case can occur if he `slope` is $0$ at any point.
- Sometimes, the approximations do not converge to a solution.

## Rolle's Theorem

If $f(x)$ is differentiable over an `interval`[^2] $(a, b)$ and `continous`[^3] over the `interval`[^2] $[a, b]$ then there exists $c \in \{x \in \mathbb{R}: a < x < b\}$ such that $f^{\prime}(c) = 0$.

### General Equation

$$\because \frac{y - y_1}{x - x_1} = \frac{y_2 - y_1}{x_2 - x_1}$$

$$\frac{y - f(a)}{x - a} = \frac{f(b) - f(a)}{b - a}$$

$$y - f(a) = \frac{f(b) - f(a)}{b - a} \cdot (x - a)$$

$$y = \frac{f(b) - f(a)}{b - a} \cdot (x - a) + f(a)$$

## Mean Value Theorem

If the conditions are right, the `secant line` will have same `slope` as the `tangent line`.

If $f(x)$ is differentiable over an `interval`[^2] $(a, b)$ and `continous`[^3] over the `interval`[^2] $[a, b]$ then there exists $c \in \{x \in \mathbb{R}: a < x < b\}$ such that $f^{\prime}(c) = \frac{f(b) - f(a)}{b - a}$.

### Proof

![[Pasted image 20240925103021.png]]

We can define a `function`[^1] $v(x)$ which represents the `distance` between the curve and the `secant line`.  
From `Rolle's Theorem`  

$$v(x) =f(x) - \left(\frac{f(b) - f(a)}{b - a} \cdot (x - a) + f(a)\right)$$

$$v^{\prime}(x) = f^{\prime}(x) - \left(\frac{f(b) - f(a)}{b - a}\right)$$

Since, $v(a) = v(b) = 0$, it satisfies `rolle's theorem` and there is a point $c$ where $v^{\prime}(c) = 0$

$$v^{\prime}(c) = f^{\prime}(c) - \left(\frac{f(b) - f(a)}{b - a}\right)$$

$$0 = f^{\prime}(c) - \left(\frac{f(b) - f(a)}{b - a}\right)$$

$$f^{\prime}(c) = \left(\frac{f(b) - f(a)}{b - a}\right)$$

## Reference

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[Mathematics/Function/Content|functions]].
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/1. Coordinates, Graphs, Lines/Lecture|intervals]].
[^3]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/12. Continuity/Lecture|continuity]].