---
tags:
  - university-notes
  - limits
university-name: Virtual University of Pakistan
---

# Limits (Computational Techniques)
## Theorems

1. $$\lim[f(x) + g(x)] = \lim f(x) + \lim g(x)$$

2. $$\lim[f(x) - g(x)] = \lim f(x) - \lim g(x)$$

3. $$\lim[f(x) \cdot g(x)] = \lim f(x) \cdot \lim g(x)$$

4. $$\lim \left[\frac{f(x)}{g(x)}\right] = \frac{\lim f(x)}{\lim g(x)}$$

5. $$\lim_{x \rightarrow a}(x^n) = \left(\lim_{x \rightarrow a} (x)\right)^n = a^n$$

6. $$\lim[k \cdot g(x)] = \lim(k) \cdot \lim g(x) = k \cdot \lim g(x)$$

## Limits of Polynomial
### Example

$$\lim_{x \rightarrow 5}(x^2 - 4x + 3)$$

$$= \lim_{x \rightarrow 5} x^2 - \lim_{x \rightarrow 5} 4x + \lim_{x \rightarrow 5} 3$$

$$= \lim_{x \rightarrow 5} x^2 - 4 \cdot \lim_{x \rightarrow 5} x + \lim_{x \rightarrow 5} 3$$

$$= 5^2 - 4 \cdot 5 + 3$$

$$= 25 - 20 + 3$$

$$= 8$$

### Rules for $x$ Approaching to $\infty$

$$\lim_{x \rightarrow + \infty} \frac{c_0 + c_1 \cdot x^1 + \ldots + c_nx^n}{d_0 + d_1 \cdot x^1 + \ldots + d_nx^n} = \lim_{x \rightarrow + \infty} \frac{c_nx^n}{d_nx^n}$$

$$\lim_{x \rightarrow - \infty} \frac{c_0 + c_1 \cdot x^1 + \ldots + c_nx^n}{d_0 + d_1 \cdot x^1 + \ldots + d_nx^n} = \lim_{x \rightarrow - \infty} \frac{c_nx^n}{d_nx^n}$$

#### Example

$$\lim_{x \rightarrow - \infty} \frac{4x^2 - x}{2x^3 - 5} = \lim_{x \rightarrow - \infty} \frac{4x^2}{2x^3} = \lim_{x \rightarrow - \infty} \frac{2}{x} = 0$$

## References
Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].