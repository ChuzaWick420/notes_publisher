---
tags:
  - university-notes
  - integral
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Uses of `Integrals`[^1]

## Area as `Integral`[^1]

Imagine a `triangle` with $base = 4$ on `x axis` in `interval`[^2] $[0, 4]$ and $height = 8$.  
The `hypotenuse` is represented by $y = 2x$.  

$$\int_0^4 2x dx = \left[x^2\right]_0^4$$

$$= 4^2 - 0^2$$

$$= 16$$

We can also use the normal formula  

$$\text{Area} = \frac 1 2 \text{base} \times \text{height}$$

$$= \frac 1 2 (4) \times (8) = 16$$

## Volume as `Integral`[^1]

Similarly, we can use $\iint$ to find `volume`. 

## Properties

1. $$\iint_R cf(x, y) dxdy = c\iint_R f(x, y) dxdy \text{ where } c \text{ is constant}$$

2. $$\iint_R (f(x, y) + g(x, y)) dxdy = \iint_R f(x, y) dxdy + \iint_R g(x, y) dxdy$$

3. $$\iint_R (f(x, y) - g(x, y)) dxdy = \iint_R f(x, y) dxdy - \iint_R g(x, y) dxdy$$

4. $$\iint_R f(x, y) dxdy \ge 0 \text{ if } f(x, y) \ge 0 \text{ on } R$$

5. $$\iint_R f(x, y) dxdy \ge \iint_R g(x, y) dxdy \text{ if } f(x, y) \ge g(x, y)$$

If $f(x, y)$ is a `non negative function`[^3] defined over a region $R$ then sub dividing $R$ into $R_1$ and $R_2$ has effect of dividing the solid bounded by $R$ and $z = f(x,  y)$ into 2 solids.  

$$\iint_R f(x, y) dxdy = \iint_{R_1} f(x, y) dxdy + \iint_{R_2}f(x, y) dxdy$$

## Computing Cross Section Area

Let's say we have $f(x, y)$ bounded within $a \le x \le b$ and $c \le y \le d$.  
Then if we take a certain value of $y$, the $f(x, y_0)$ becomes a `function`[^3] of $x$.  
Thus integrating it gives us `area` under the curve $f(x, y_0)$ in `interval`[^2] $a \le x \le b$.  
Therefore,  

$$A(y) = \int_a^b f(x, y) dx$$

## Double `Integral`[^1] for Non Rectangular Region

Let's say we have a region $R$ bounded by `lines`[^4] $x = a$, $x = b$, $y = g_1(x)$ and $y = g_2(x)$.  
Therefore, our boundaries are $a \le x \le b$ and $g_1(x) \le y \le g_2(x)$.  
This gives us `volume` as  

$$V = \int_a^b \int_{g_1(x)}^{g_2(x)} f(x, y) dydx$$

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/25. Integrations/Lecture|integrals]]. 
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/1. Coordinates, Graphs, Lines/Lecture|intervals]]. 
[^3]: Read more about [[Mathematics/Function/Content|functions]]. 
[^4]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/4. Lines/Lecture|lines]]. 