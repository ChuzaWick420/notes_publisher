---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Periodic Functions

A `function`[^1] is called `periodic function` if its values repeat after regular intervals of the independent `variable`.  
This interval is called `period of oscillations`.  

$$f(x + p) = f(x)$$

## Graph of $y = \sin(x)$

This `function`[^1] repeats its values after $x = 2 \pi$.  
Its `range`[^1] is $[-1, 1]$, meaning it can only produce a maximum `absolute value`[^2] of $1$.  
Therefore, its `amplitude` is $1$.

### Example

| Functions               | Amplitude | Period      |
| ----------------------- | --------- | ----------- |
| $y= 3 \sin(5x)$         | $3$       | $72^\circ$  |
| $y = 2 \cos(\frac x 2)$ | $2$       | $720^\circ$ |

In general if we have something like $y = a \sin (n \cdot x)$ then $a$ is called the `amplitude` and `period` is $\frac{360^\circ}{n}$.

## Useful `Integrals`[^3]

1. $$\int_{- \pi}^\pi \sin(n \cdot x) dx = \left[\frac{- \cos(n \cdot x)}{n}\right]_{- \pi}^\pi = \frac 1 n (- \cos (n \cdot \pi) + \cos(n \cdot x)) = 0$$

2. $$\int_{- \pi}^\pi \cos(n \cdot x) dx = \left[\frac{\sin(n \cdot x)}{n}\right]_{- \pi}^\pi = \frac 1 n (\sin (n \cdot \pi) + \sin(n \cdot x)) = 0$$

3. $$\int_{-\pi}^{\pi}\sin^{2}(n \cdot x)dx=\frac{1}{2}\int_{-\pi}^{\pi}(1-\cos(2n \cdot x))dx=\frac{1}{2}\left[x-\frac{\sin(2n \cdot x)}{2n}\right]_{-\pi}^{\pi}=\pi$$

4. $$\int_{-\pi}^{\pi}\cos^{2}(n \cdot x)dx=\frac{1}{2}\int_{-\pi}^{\pi}(1+\cos(2n \cdot x))dx=\frac{1}{2}\left[x+\frac{\sin(2n \cdot x)}{2n}\right]_{-\pi}^{\pi}=\pi$$

5. $$\int_{-\pi}^{\pi}\sin(n \cdot x)\cos(m \cdot x)dx=\frac{1}{2}\int_{-\pi}^{\pi}(\sin(n+m)x+\sin(n-m)x)dx=\frac{1}{2}(0+0) = 0$$

6. $$\int_{-\pi}^{\pi}\cos(n \cdot x)\cos(m \cdot x)dx=\frac{1}{2}\int_{-\pi}^{\pi}(\cos(n+m)x+\cos(n-m)x)dx=\frac{1}{2}(0+0)=0$$

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[Mathematics/Function/Content|functions]].
[^2]: Read more about [[2. Absolute Value|absolute value]].
[^3]: Read more about [[25. Integrations|integrals]].