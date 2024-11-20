---
tags:
  - university-notes
  - extrema
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Extreme Valued Theorem

## Theorem

If a `function`[^1] is `continuous`[^2] over the `closed interval`[^3] $[a, b]$ then the `function`[^1] has `absolute maximum`[^4] and `absolute minimum`[^4] values over that `interval`.[^3]

## Steps

If $f(x)$ is `continuous`[^2] over $[a, b]$ then

1. Find `critical points`[^4] and their corresponding $f(x)$ values.
2. Find $f(a)$ and $f(b)$.
3. Largest among all these values is `absolute maximum` and smallest is `absolute minimum`.

### Example

$$f(x) = x^3 + x^2 - x + 1 \text { on } \left[-2 , \frac 1 2\right]$$

$$f^{\prime}(x) = 3x^2 + 2x - 1$$

$$\because \text{For critical points } f^{\prime}(x) = 0$$

$$0 = 3x^2 + 2x - 1$$

Simplify and we get  

$$x = -1 , \frac 1 3$$

Putting all these values in $f(x)$, we get  

$$f(-2) = (-2)^3 + (-2)^2 - (-2) + 1 = -1$$

$$f(-1) = (-1)^3 + (-1)^2 - (-1) + 1 = 2$$

$$f\left(\frac 1 3\right) = \left(\frac 1 3\right)^3 + \left(\frac 1 3 \right)^2 - \left(\frac 1 3 \right) + 1 = \frac{22}{27}$$

$$f\left(\frac 1 2\right) = \left(\frac 1 2\right)^3 + \left(\frac 1 2 \right)^2 - \left(\frac 1 2 \right) + 1 = \frac{7}{8}$$

This shows that `absolute maximum` is $2$ present at $x = -1$ and `absolute minimum` is $-1$ present at $x = -2$.

## Steps for `function`[^1] of 2 Variables

1. Find `critical points`[^4] of $f$ that lie in the interior of $R$.
2. Find all boundary points where `absolute extrema` can occur.
3. Evaluate $f(x, y)$ at these points. The largest of them is `absolute maximum` and the smallest being `absolute minimum`.

### Example

Find `absolute minimum` and `absolute maximum` values over first `quadrant`[^5] within the triangular region $R$ bounded by $x = 0$, $y = 0$ and $y = 9 - x$ where `function`[^1] is

$$f(x, y) = 2 + 2x + 2y - x^2 - y^2$$

#### Solution

<iframe src="../figures/extrema.html"></iframe>
From the equation $y = 9 - x$, we get 3 corners, $(0, 0)$, $(9, 0)$ and $(0, 9)$.
To find other points
$$f_x(x, y) = 2 - 2x$$
$$f_y(x, y) = 2 - 2y$$
Assuming $f_x = 0$ and $f_y = 0$, we get $(1, 1)$.

Now we try to look at the sides of the triangle  
For the `x axis`, we have $f(x, 0) = 2 + 2x - x^2$.  

$$f^{\prime}(x, 0) = 2 - 2x$$

$$\because f^{\prime}(x, 0) = 0$$

$$0 = 2 - 2x$$

This gives us $(1, 0)$  
Similarly, $f^{\prime}(0, y)$ will give us $(0, 1)$

For the side $y = 9 - x$,  

$$f(x, 9 - x) = 2 + 2x + 2(9 - x) -x^2 - (9 - x)^2$$

$$f^{\prime}(x, 9 - x) = 18 - 4x$$

Therefore, we have $x = \frac 9 2$  
Similarly, we will get $y = \frac 9 2$

| $(x, y)$                 | $f(x, y)$        |
| ------------------------ | ---------------- |
| $(0, 0)$                 | $2$              |
| $(9, 0)$                 | $-61$            |
| $(1, 0)$                 | $3$              |
| $(\frac 9 2, \frac 9 2)$ | $\frac {-41}{2}$ |
| $(0, 9)$                 | $-61$            |
| $(0, 1)$                 | $3$              |
| $(1, 1)$                 | $4$              |

Therefore, the `absolute minimum` is $-61$ existing at $(0, 9)$ and $(9, 0)$ and `absolute maximum` is $4$ existing at $(1, 1)$.

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[Mathematics/Function/Content|functions]].
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/12. Continuity/Lecture|continuity]].
[^3]: Read more about [[1. Coordinates, Graphs, Lines|intervals]].
[^4]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/22. Relative Extrema/Lecture|extreme values]].
[^5]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/3. Coordinate Planes and Graphs/Lecture|quadrants]].