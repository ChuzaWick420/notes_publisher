---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# The First Fundamental Theorem of Calculus
## Theorem
If $f(x)$ is a `continuous function`[^1] over the `interval`[^2] $[a, b]$ and $F(x)$ is its `anti-derivative`[^3] then

$$\int_a^b f(x) dx = F(b) - F(a)$$

### Proof
Let us divide the `interval`[^2] into $n$ `subintervals`, such that  

$$a < x_1 < x_2 < \ldots < x_{n-1} < b$$

So our `subintervals` are  

$$[a, x_1], [x_1, x_2], \ldots , [x_{n - 1}, b]$$

Let $x_1^*$ be the `midpoint`[^4] of `interval`[^2] $[a, x_1]$ and so on, then using the `mean value theorem`[^5],  

$$F(x_1) - F(a) = F'(x_1^*)(x_1 - a) = f(x_1^*) \Delta x_1$$

$$F(x_2) - F(x_1) = F'(x_2^*)(x_2 - x_1) = f(x_2^*) \Delta x_2$$

And so on, eventually the last one looks like this:  

$$F(b) - F(x_{n-1}) = F'(x_n^*)(b - x_{n-1}) = f(x_n^*)\Delta x_n$$

Adding all these equations together, we will get  

$$F(b) - F(a) = \sum_{i=1}^{n} f(x_i^*)\Delta x_i$$

Now, we will increase the number of slices $n$ in such a way that $max (\Delta x_{i} \to 0)$  

$$F(b) - F(a) = \lim_{max(\Delta x_i \to 0)} \sum_{i=1}^{n} f(x_i^*)\Delta x_i = \int_a^b f(x)dx$$

We can also write it as  

$$\int_{a}^{b} f(x) dx = F(x) \bigg]_{a}^{b}$$

## Example
### The Problem

Evaluate $\int_0^6 f(x) dx$ if 

$$
f (x) = 
\begin{cases}
x^2 & x < 2 \\
3x - 2 & x \ge 2
\end{cases}
$$

### Solution
First thing we notice is that it is a `discontinous function`[^1] and the point of `discontinuity` is $2$.  
We can divide our `interval`[^2] $[0, 6]$ into $[0, 2)$ and $[2, 6]$.  
Then using the `properties of integration`[^3],  

$$\int_0^6 f(x) dx = \int_0^2 f(x) dx + \int_2^6 f(x) dx$$

$$= \int_0^2 x^2 dx + \int_2^6 3x - 2 dx$$

$$= \frac{x^3}{3} \bigg]_0^2 + \bigg[\frac 3 2 x^2 - 2x \bigg]_2^6$$

$$= \left(\frac{2^3}{3} - \frac{0^3}{3}\right) + \left(\left(\frac 3 2 \cdot 6^2 - 2(6)\right) - \left(\frac 3 2 \cdot 2^2 - 2(2)\right)\right)$$

$$= \left(\frac 8 3 - 0\right) + \left( 42 - 2\right)$$

$$= \frac {128}{3}$$

## Mean Value Theorem for Integrals
![[Pasted image 20240927165430.png]]  
Here $M$ is the largest value which $f(x)$ can output and $m$ is the smallest.  
According to `mean value theorem`[^5], there is some value $c$ in $[a, b]$ where,  

$$\int_a^b f(x) dx = f(c) \cdot (b - a)$$

From the diagram,

$$m(b - a) \le \int_a^b f(x) dx \le M(b - a)$$

The `inequality`[^6] suggests a ranking of `areas` in following `descending order`.

1. `Area` of `rectangle` with `width` $b - a$ and `height` $M$.
2. `Area` under the curve $f(x)$.
3. `Area` of `rectangle` with `width` $b - a$ and `height` $m$.

We can re-arrange the `inequality`[^6] as follows:  

$$m \le \frac {1}{b - a}\int_a^b f(x) dx \le M$$

$$\because \int_a^b f(x) dx = f(c) \cdot (b - a)$$

$$\therefore \frac {1}{b - a}\int_a^b f(x) dx = f(c)$$

Here $f(c)$ is also called $f_{avg}$, the average value of $f(x)$ with respect to $x$ over the `interval`[^2] $[a, b]$.

## References

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/12. Continuity/Lecture|continuity]]
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/1. Coordinates, Graphs, Lines/Lecture|intervals]].
[^3]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/25. Integrations/Lecture|anti derivatives]].
[^4]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/5. Distance, Circles, Quadratic Equations/Lecture|midpoint]].
[^5]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/24. Newton's Method, Rolle's Theorem and Mean Value Theorem/Lecture|mean value theorem]].
[^6]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/1. Coordinates, Graphs, Lines/Lecture|inequalities]].
