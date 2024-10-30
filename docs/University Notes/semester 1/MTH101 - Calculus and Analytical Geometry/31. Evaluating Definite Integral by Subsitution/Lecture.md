---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Evaluating Definite Integrals Using Substitution

## Substitution

We can evaluate  

$$\int_a^b f(x) dx$$

by following ways

### Method 1

First, evaluate the `indefinite integral`[^1] $\int f(x) dx$ and then use the relationship  

$$\int_a^b f(x) dx = \int f(x) dx \bigg]_a^b$$

### Method 2

We can write the equation in following form

$$\int_a^b f(x) \, dx = \int_a^b h(g(x)) g'(x) \, dx$$

Then assume $u = g(x)$, we get  

$$\frac{du}{dx} = g^{\prime}(x)$$

$$du = g^{\prime}(x) dx$$

Also, $u = g(a)$ if $x = a$ and $u = g(b)$ if $x = b$.  
Substitute these in our original equation, we get  

$$\int_a^b f(x) \, dx = \int_{g(a)}^{g(b)} h(u) du$$

### Example

Evaluate 

$$\int_0^2 x (x^2 + 1)^3 \, dx$$

#### Method 1

Assume $u = (x^2 + 1)$, then $\frac{du}{dx} = 2x \implies \frac{du}{2x} = dx$  
Substitute these values and we will get

$$\int x(x^2 + 1)^3 \, dx = \frac{1}{2} \int u^3 \, du = \frac{u^4}{8} + C = \frac{(x^2 + 1)^4}{8} + C$$

$$ = \frac{(x^2 + 1)^4}{8} \bigg]_0^2 = 78$$

#### Method 2

If $x = 0$ then $u = 1$  
If $x = 2$ then $u = 5$  
Substituting values, we get  

$$\int_{0}^{2}x(x^{2}+1)^{3}dx=\frac{1}{2}\int_{1}^{5}u^{3}du=\frac{u^{4}}{8}\bigg]_{1}^{5}=78$$

## Approximation by Reimann Sums

The `Reimann Sum` is the expression  

$$\sum_{i=1}^{n} f(x_i^*)\Delta x_i$$

If we take the `limit`[^2] of this expression, we get a `definite integral`.[^3]  
However, if we don't but $n$ is relatively pretty large then in that case  

$$\int_{a}^{b}f(x)dx\approx\sum_{i=1}^{n}f(x_{i}^{*})\Delta x_{i}$$

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/25. Integrations/Lecture|integrals]].
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/9. Limits (Intuitive Introduction)/Lecture|limits]].
[^3]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/29. Definite Integral/Lecture|definite integral]].