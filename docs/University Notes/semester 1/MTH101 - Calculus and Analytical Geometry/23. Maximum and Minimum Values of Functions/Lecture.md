---
tags:
  - university-notes
  - extrema
university-name: Virtual University of Pakistan
---

# Maximum and Minimum Values of Functions
## Absolute Extrema
These are either the _highest_ peaks in the mountain range or the _deepest_ of valleys.

### Absolute Minimum
If $f(x_0) \le f(x)$ for all $x$ in domain of $f(x)$ then $f(x_0)$ is called `absolute minimum` of $f(x)$.

### Absolute Maximum
If $f(x_0) \ge f(x)$ for all $x$ in domain of $f(x)$ then $f(x_0)$ is called `absolute maximum` of $f(x)$.

### Example
![[Pasted image 20240923082008.png]]

This is graph of `function`[^1] defined to be $f(x) = 2x + 1$ over an `interval`[^2] $[0, 3)$.  

> $x = 3$ is excluded from the domain, the maximum value for $x$ is $x < 3$.  

The `absolute minima` for this `function`[^1] is $1$.

> You might think the `absolute maxima` for this `function`[^1] is $7$ but it is actually not. Reason behind it is that the `function`[^1] never becomes equal to $7$ since $x$ never becomes $3$, though, they are very close.

## Theorem
If a $f(x)$ has an extreme value (either maximum or minimum) on an `open interval`[^2] $(a, b)$ then these extreme values appear at `critical points`[^3] of $f(x)$.

## Finding Absolute Extrema for a Continuous Function
We can divide this task into following tasks.

1. Find `critical points`[^3] of $f(x)$.
2. Find values of $f(x)$ at `critical points`[^3] and the endpoints of the `interval`[^2] the `function`[^1] is defined at.
3. The largest of the values in Step 2 is `absolute maxima` and the smallest is `absolute minima`.

## Example
Find dimensions of a `rectangle` with $100 ft$ `perimeter` such that it has maximum `area`.

### Solution
We can represent the `perimeter` as:  

$$100 = 2y + 2x$$

$$50 = x + y$$

$$y = 50 - x$$

Then we can represent the `area` which we want to maximize as:  

$$A(x, y) = xy$$

We can re-write the `function`[^1] in terms of $x$.  

$$A(x) = x \cdot (50 - x) = 50x - x^2$$

From the equation above, it is evident that $A(x) = 0$ if $x = 0, 50$.  

> Since `negative lengths` are not realistic, $x$ cannot go below $0$ and if $x > 50$ then the `area` becomes `negative` which is not realistic either. Hence, our `interval`[^2] is $[0, 50]$.

Then we find the `absolute maxima`. For that, we need to find the `critical points`[^3]. For that, we do our `derivative test`[^4].  

$$A^{\prime}(x) = 50 - 2x$$

$$0 = 50 - 2x$$

$$2x = 50$$

$$x = 25$$

So our values to check are $x = 0, 25, 50$.  

$$A(0) = 50 \cdot 0 - 0^2 = 0$$

$$A(25) = 50 \cdot 25 - {25}^2 = 625$$

$$A(50) = 50 \cdot 50 - {50}^2 = 0$$

So the `absolute maximum` lies at $x = 25$.  
Put this in the `perimeter` equation.  

$$y = 50 - x$$

$$y = 50 - 25 = 25$$

Hence, the dimensions of the `rectangle` with maximum `area` are $25 \times 25$.

## References

[^1]: Read more about [[Mathematics/Function/Content|functions]].
[^2]: Read more about [[University Notes/semester 1/MTH101 - Calculus and Analytical Geometry/1. Coordinates, Graphs, Lines/Lecture|intervals]]
[^3]: Read more about [[University Notes/semester 1/MTH101 - Calculus and Analytical Geometry/22. Relative Extrema/Lecture|critical points]]
[^4]: Read more about [[University Notes/semester 1/MTH101 - Calculus and Analytical Geometry/22. Relative Extrema/Lecture|derivative tests]]
