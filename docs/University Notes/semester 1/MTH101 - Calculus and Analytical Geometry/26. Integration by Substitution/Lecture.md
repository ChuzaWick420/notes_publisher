---
tags:
  - university-notes
  - integral
  - differentiation
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Integration by Substitution

Let's say we have  

$$\frac{d}{du} g(u) = f(u)$$

Then  

$$\int f(u) du = \int \left(\frac{d}{du}g(u)\right) du$$

$$= \int d \,g(u)$$

$$= g(u) + C$$

Now let us assume that $u$ is a `function`[^1] of $x$. i.e. $u(x)$. Then,  

$$\frac{d}{dx} g(u) = \frac{d}{du} g(u) \cdot \frac{du}{dx} = f(u) \cdot \frac{du}{dx}$$

We can use this conclusion in a very specific scenario. Let us take a look

$$\int \left( f(u) \frac{du}{dx} \right) dx = \int \frac{d}{dx} (g(u)) dx = g(u) + C
$$

## Example

$$\int (x^2 + 1)^{50} \cdot 2x \cdot dx$$

Now let us define some `variables`.  

- $$f(u) = u^{50}$$

- $$u = (x^2 + 1)$$

- $$\frac{du}{dx} = 2x$$

So if we replace our data with the `variables`, we get  

$$\int f(u) \cdot \frac{du}{dx} \cdot dx = \int f(u) du$$

This suggests we just need to `integrate`[^2] $f(u)$.  

$$\int f(u) du = \int u^{50} du$$

$$= \frac{u^{50 + 1}}{50 + 1} + C$$

$$= \frac{u^{51}}{51} + C$$

Substituting $u$, we get

$$= \frac{(x^2 + 1)^{51}}{51} + C$$

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[docs/Mathematics/Function/Content|functions]].
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/25. Integrations/Lecture|integration]].