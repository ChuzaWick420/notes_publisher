---
tags:
  - university-notes
  - extrema
university-name: Virtual University of Pakistan
---

# Relative Extrema
## Relative Maxima
Most of the graphs we have seen have `ups` and `downs`.  
the `ups` or the `hills` are called `relative maxima`.

### Definition
A `function`[^1] $f(x)$ is said to have a `relative maxima` at $x_0$ if $f(x_0) \ge f(x)$ for all $x$ in some `open interval`[^2] $(a, b)$ containing $x_0$.

![[Pasted image 20240906185321.png]]

## Relative Minima
The `downs` and `valleys` are called `relative minima`.

### Definition
A `function`[^1] $f(x)$ is said to have a `relative minima` at $x_0$ if $f(x_0) \le f(x)$ for all $x$ in some `open interval`[^2] $(a, b)$ containing $x_0$.

![[Pasted image 20240906185925.png]]

## Critical Points
These are the points on the graph where there is a transition of `function`[^1] changing its nature from _increasing_ to _decreasing_ or other way around.

![[Pasted image 20240906190510.png]]

## Theorem
If $f(x)$ has a `relative extrema` at $x_0$ then $f^{\prime}(x_0) = 0$ or $f(x)$ is not differentiable at $x_0$.  

>The points where $f^{\prime}(x_0) = 0$ are called `stationary points`.

## First Derivative Test
### Relative Maxima
If $f^{\prime}(x) > 0$ on an `open interval`[^2] starting from $x_0$ and extending to _left_ (towards $-\infty$) $f^{\prime}(x) < 0$ when extending to _right_ (towards $+\infty$) then $f(x)$ is said to have a `relative maxima` at $x_0$.

### Relative Minima
If $f^{\prime}(x) < 0$ on an `open interval`[^2] starting from $x_0$ and extending to _left_ (towards $-\infty$) and $f^{\prime}(x) > 0$ when extending to _right_ (towards $+\infty$) then $f(x)$ is said to have a `relative minima` at $x_0$.

### Infliction point
If the sign of $f^{\prime}(x)$ remains the same at _left_ and _right_ sides of $x_0$ then it means that the graph did not had a `relative extrema` at that point.  
This point is called `infliction point`.

## Second Derivative Test
1. if $f^{\prime \prime}(x) > 0$ then $f(x)$ has `relative minima` at $x_0$.
2. if $f^{\prime \prime}(x) < 0$ then $f(x)$ has `relative maxima` at $x_0$.

### Example
Imagine a `function`[^1] defined as:  

$$f(x) = x^4 - 2x^2$$

Then we `differentiate`[^3] it  

$$f'(x) = 4x^3 - 4x$$

$$= 4x(x-1)(x+1)$$

Taking the `second derivative`, we get  

$$f^{\prime \prime}(x) = 12x^2 - 4$$

Since we know that the `critical points` exist at points where $f^{\prime}(x) = 0$.  
Therefore, to find such points:  

$$0 = 4x(x-1)(x+1)$$

When we work this out, we get 3 points which are:  

$$x = 0, \pm1$$

Now we substitute these values of $x$ in $f^{\prime \prime}(x)$,  

$$f^{\prime \prime}(0) = -4 < 0$$

$$f^{\prime \prime}(1) = 8 > 0$$

$$f^{\prime \prime}(-1) = 8 > 0$$

Hence, $f(x)$ has `relative minima` at $x = \pm 1$ and `relative maxima` at $x = 0$.  
![[Pasted image 20240906220544.png]]

## Graphs of Polynomials
Sometimes, during engineering, it is hard to graph the `functions`[^1].  
But we still need to understand the nature of the `function`[^1] such as `relative extrema` and `concavity` etc.  
For the purposes, assume a `polynomial function` $P(x)$.
- Use $P^{\prime}(x)$ to determine `stationary points` and `intervals`[^2] of _increase_ and _decrease_.
- Use $P^{\prime \prime}(x)$ to determine `infliction points` and `intervals`[^2] where $P(x)$ is _concave up_ and _concave down_.
- Plot all these points and `x` and `y` intercepts as well.

### Example

$$P(x) = y = x^3 - 3x + 2$$

$$\frac{dy}{dx} = 3x^2 - 3 = 3(x-1)(x+1)$$

$$\frac{d^{2}y}{dx^{2}}=6x$$

#### Stationary Points
From the `first derivative test`, we can find the `stationary points` which are at $x = \pm 1$.  
Put these values of $x$ in the original $P(x)$ to get corresponding $y$ values, which are $4$ and $0$.

#### Intercepts
When we try substituting $x = 0$ in $P(x)$ to find `y intercept`, we get $y = 2$.  
When we try substituting $y = 0$ in $P(x)$ to find `x intercept`, we get $x = -2$ and $x = 1$.

Plot the points and we get something like  
![[Pasted image 20240907000035.png]]

#### Concavity
- $P^{\prime \prime}(-1) = -6$ suggests a `relative maxima` at $(-1, 4)$.
- $P^{\prime \prime}(1) = 6$ suggests a `relative minima` at $(1, 0)$.

By considering these facts in mind, we can sketch our graph (an approximation) as:  
![[Pasted image 20240907000635.png]]

## Graphs of Rational Functions
Imagine a `function`[^1] defined as  

$$f(x) = \frac{P(x)}{Q(x)} = \frac{x}{x - 2}$$

This `function`[^1] becomes `undefined` when $x = 2$.  
The graph of this `function`[^1] looks something like this.  
![[Pasted image 20240907001652.png]]

### Horizontal Asymptots
A line $y = y_0$ is called `horizontal asymptots` for the graph of $f(x)$ if
- $\lim_{x \to +\infty} f(x) = y_0$  
or
- $\lim_{x \to -\infty} f(x) = y_0$

In the graph of the `function`[^1] above, $\lim_{x \to + \infty} f(x) = \lim_{x \to - \infty} f(x) = 1$.

### Vertical Asymptots
A line $x = x_0$ is called `vertical asymptots` for the graph of $f(x)$ if
- $\lim_{x \to x_0^-} f(x) = - \infty$  
or
- $\lim_{x \to x_0^+} f(x) = + \infty$  

In the case of graph of the `function`[^1] above, $\lim_{x \to 2^-} f(x) = - \infty$ and$\lim_{x \to 2^+} f(x) = - \infty$. Hence, the `vertical Asymptots` is $2$.

## References

[^1]: Read more about [[Mathematics/Function/Content|functions]].
[^2]: Read more about [[University Notes/semester 1/MTH101 - Calculus and Analytical Geometry/1. Coordinates, Graphs, Lines/Lecture|intervals]].
[^3]: Read more about [[University Notes/semester 1/MTH101 - Calculus and Analytical Geometry/15. The Derivative/Lecture|differentiation]].
