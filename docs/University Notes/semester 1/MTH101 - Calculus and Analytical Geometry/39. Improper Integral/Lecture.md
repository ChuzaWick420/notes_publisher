---
tags:
  - university-notes
  - integral
  - "limits"
university-name: Virtual University of Pakistan
---

# Improper `Integrals`[^1]
## Integrals over Infinite `interval`[^2]
The `improper integral`[^1] is of the form  

$$\int_a^{+\infty} f(x) dx$$

or

$$\int_{-\infty}^b f(x) dx$$

## What Does it Mean?

$$\int_{a}^{+\infty}f(x)dx=\lim_{l\to+\infty}\int_{a}^{l}f(x)dx$$

1. If the `limit`[^3] exists then we say the `improper integral` _converges_ to a finite value.
2. If the `limit`[^3] does not exist then we say the `improper integral` _diverges_ and no finite value can be assigned.

### Example

Evaluate $$\int_{1}^{+\infty}\frac{1}{x^{2}}dx$$

#### Solution

$$\int_{1}^{+\infty}\frac{1}{x^{2}}dx$$

$$=\lim_{l\to+\infty}\int_{1}^{l}\frac{1}{x^{2}}dx$$

$$=\lim_{l\to+\infty}\left(1-\frac{1}{l}\right)$$

$$=1-\frac{1}{\infty}=1-0=1$$

### Example

Evaluate  

$$\int_{1}^{+\infty}\frac{1}{x}dx$$

#### Solution

$$\int_{1}^{+\infty}\frac{1}{x}dx$$

$$= \lim_{l \to +\infty} \int_1^l \frac{1}{x} dx$$

$$= \lim_{l \to +\infty} \bigg[\ln \lvert x \rvert\bigg]_1^l$$

$$\lim_{l \to +\infty} \ln \lvert l \rvert = + \infty$$

---

If $f(x)$ is not bound on `interval`[^2] then $f(x)$ is not `integratable` over $[a, b]$.  
We can get around this problem

- If $f(x)$ is `continuous`[^4] over the `interval`[^2] $[a, b)$ and does not have a `limit`[^3] from the _left_ then we can define an `improper integral` in following way $$\int_a^b f(x) dx = \lim_{l \to b^-} \int_a^l f(x) dx$$

- If $f(x)$ is `continuous`[^4] over the `interval`[^2] $(a, b]$ and does not have a `limit`[^3] from the _right_ then we can define an `improper integral` in following way $$\int_a^b f(x) dx = \lim_{l \to a^+} \int_l^b f(x) dx$$

If  

- $f(x)$ is `continuous`[^4] over the `interval`[^2] $[a, b]$ except for the point $c$  
- $a < c < b$  
- $f(x)$ goes `infinite` as $x^+ \to c$ and $x^- \to c$  
- both `improper integrals`, which are $\int_a^c f(x) dx$ and $\int_c^b f(x) dx$, _converge_  

then  

$$\int_{a}^{b}f(x)dx=\int_{a}^{c}f(x)dx+\int_{c}^{b}f(x)dx$$

## Example
Evaluate  

$$\int_{1}^{4}\frac{dx}{(x-2)^{2/3}}$$

### Solution
The `integrand`[^1] approaches to $+ \infty$ as $x \to 2$. Therefore,  

$$\int_{1}^{4}\frac{dx}{(x-2)^{2/3}} = \int_{1}^{2}\frac{dx}{(x-2)^{2/3}} + \int_{2}^{4}\frac{dx}{(x-2)^{2/3}}$$

$$\int_{1}^{4}\frac{dx}{(x-2)^{2/3}} $$

$$= \lim_{l\to 2^{-}}\int_{1}^{l}\frac{dx}{(x-2)^{2/3}} $$

$$= \lim_{l\to 2^{-}}\left[3(l-2)^{1/3}-3(1-2)^{1/3}\right] $$

$$= 3$$

$$\lim_{l\to 2^{+}}\int_{l}^{4}\frac{dx}{(x-2)^{2/3}} $$

$$= \lim_{l\to 2^{+}}\left[3(4-2)^{1/3}-3(l-2)^{1/3}\right] $$

$$= 3\sqrt[3]{2}$$

## References

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/25. Integrations/Lecture|integrals]].
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/1. Coordinates, Graphs, Lines/Lecture|intervals]].
[^3]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/9. Limits (Intuitive Introduction)/Lecture|limits]].
[^4]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/12. Continuity/Lecture|continuity]].
