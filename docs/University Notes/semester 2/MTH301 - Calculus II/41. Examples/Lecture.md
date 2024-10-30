---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Examples

## Example

Find the `fourier series`[^1] for the following `function`[^2]  

$$f(x) = -x \quad - \pi < x < 0$$

$$f(x) = 0 \quad 0 < x < \pi$$

$$f(x) = f(x + 2\pi)$$

### Solution

#### $a_0$

$$a_{0}=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)dx$$

$$=\frac{1}{\pi}\left(\int_{-\pi}^{0}(-x)dx+\int_{0}^{\pi}0~dx\right)$$

$$=\frac{1}{\pi}\int_{-\pi}^{0}(-x)dx$$

$$=\frac{1}{\pi}\left[-\frac{x^{2}}{2}\right]_{-\pi}^{0}$$

$$=\frac{\pi}{2}$$

#### $a_n$

$$a_{n}=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\cos(nx)dx$$

$$=\frac{1}{\pi}\int_{-\pi}^{0}(-x)\cos(nx)dx+\frac{1}{\pi}\int_{0}^{\pi}0~dx$$

$$=-\frac{1}{\pi}\int_{-\pi}^{\pi}x \cdot \cos(nx)dx$$

$$=-\frac{1}{\pi}\left(\left[x\frac{\sin(nx)}{n}\right]_{-\pi}^{0}-\frac{1}{n}\int_{-\pi}^{0}\sin(nx)dx\right)$$

$$=-\frac{1}{\pi}\left((0-0)-\frac{1}{n}\left[\frac{-\cos(nx)}{n}\right]_{-\pi}^{0}\right)$$

$$=-\frac{1}{\pi}\left(\frac{1}{n}\left[\frac{\cos(nx)}{n}\right]_{-\pi}^{0}\right)$$

$$=-\frac{1}{\pi n^{2}}\left(\left[\frac{\cos(nx)}{n}\right]_{-\pi}^{0}\right)$$

$$=-\frac{1}{\pi n^{2}}\left(\cos(0)-\cos(n)\pi\right)$$

$$= - \frac 1 {\pi n^2} (1 - \cos (n \pi))$$

##### If $n$ is even

$$a_n = - \frac 2 {\pi n^2}$$

##### If $n$ is Odd

$$a_n = 0$$

#### $b_n$

$$b_{n}=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\sin(nx)dx$$

$$=\frac{1}{\pi}\int_{-\pi}^{0}(-x)\sin(nx)dx$$

$$=-\frac{1}{\pi}\int_{-\pi}^{\pi}x~\sin(nx)dx$$

$$=-\frac{1}{\pi}\left(\left[x\frac{\cos(nx)}{n}\right]_{-\pi}^{0}+\frac{1}{n}\int_{-\pi}^{0}\cos(nx)dx\right)$$

$$=-\frac{1}{\pi}\left(\frac{\pi \cdot \cos(n\pi)}{n}+\frac{1}{n}\left[\frac{\sin(nx)}{n}\right]_{-\pi}^{0}\right)$$

$$=\frac{\cos(n\pi)}{n}$$

##### If $n$ is even

$$b_n = \frac 1 n$$

##### If $n$ is Odd

$$b_n = - \frac 1 n$$

$$\therefore f(x) = \frac \pi 4 - \frac 2 \pi \left(\cos (x) + \frac 1 9 \cos(3x) + \frac 1 {25} \cos(5x) + \ldots \right) + \left(\sin(x) - \frac 1 2 \sin(2x) + \frac 1 3 \sin(3x) + \ldots \right)$$

## Products of `odd` and `even functions`[^2]

Let's say we have 2 `functions`,[^2] $g(x)$ and $f(x)$.

### Both `Even`

If both of them are `even functions`[^2] then the following is also `even function`.[^2]

$$h(x) = f(x) \cdot g(x)$$

### Both `Odd`

If both of them are `odd functions`[^2] then the following is an `even function`.[^2]

$$h(x) = f(x) \cdot g(x)$$

### One `Odd` and other `Even`

If both `functions`[^2] differ from each other in their nature then the following is an `odd function`.[^2]

$$h(x) = f(x) \cdot g(x)$$

## Useful Facts

### For `Even Functions`

$$\int_{-a}^a f(x) dx = 2 \int_{- a}^a f(x) dx$$

### For `Odd Functions`

$$\int_{-a}^a f(x) dx = 0$$

## Theorems

1. If the $f(x)$ is an `even function`[^2] over the `interval`[^3] $[- \pi, \pi]$ then the `fourier series`[^1] consists of only $\cos$ terms.
2. If the $f(x)$ is an `odd function`[^2] over the `interval`[^3] $[- \pi, \pi]$ then the `fourier series`[^1] consists of only $\sin$ terms.

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 2/MTH301 - Calculus II/40. Fourier Series/Lecture|fourier series]].
[^2]: Read more about [[Mathematics/Function/Content|functions]].
[^3]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/1. Coordinates, Graphs, Lines/Lecture|interval]].