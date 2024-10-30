---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Fourier Series

The `series`[^1] of `trignometrical` `functions`[^2] of the following form is called `fourier series`.  

$$f(x) = A_0 + c_1 \sin(x + \alpha_1) + c_2 \sin(2x + \alpha_2) + \ldots$$

$$= A_0 + \sum_{n=1}^\infty c_n \cdot \sin (n \cdot x + \alpha_n)$$

Here $A_0$ is a `constant`.  
$c_n$ denotes the `amplitude`.  
$\alpha_n$ denotes auxiliary `angles`.

We can expand the term $c_n \cdot \sin (n \cdot x + \alpha_n)$ as follows  

$$c_n \cdot \sin (n \cdot x + \alpha_n) = c_n(\sin (nx) \cdot \cos \alpha_n + \cos(nx) \cdot \sin(\alpha_n))$$

$$ = c_n\sin (nx) \cdot \cos \alpha_n + c_n \cos(nx) \cdot \sin(\alpha_n)$$

$$\text{Let } c_n \sin (nx) = a_n \text{ and } c_n \cos(nx) = b_n$$

Then the `series`[^1] becomes

$$= A_0 + \sum_{n=1}^\infty (a_n \cos (nx) + b_n \sin(nx))$$

## Coefficients of Fourier Series

### $A_0$

To find $A_0$, we will `integrate`[^3] both sides of the `series`.[^1]  

$$f(x) = A_0 + \sum_{n=1}^\infty (a_n \cos (nx) + b_n \sin(nx))$$

$$\int_{- \pi}^\pi f(x)dx = \int_{- \pi}^\pi\left(A_0 + \sum_{n=1}^\infty (a_n \cos (nx) + b_n \sin(nx))\right)dx$$

$$= \int_{- \pi}^\pi A_0 dx + \sum_{n = 1}^\infty \left(\int_{- \pi}^\pi a_n \cos(nx)dx\int_{- \pi}^\pi b_n \sin (nx)dx\right)$$

$$= \left[A_0\right]_{- \pi}^\pi + \sum_{n = 0}^\infty (0 + 0)$$

$$\int_{-\pi}^\pi f(x) = 2 \pi \cdot A_0$$

$$A_0 = \frac 1 {2 \pi} \int_{- \pi}^\pi f(x)$$

### $a_n$

To find $a_n$, we will multiply $f(x)$ by $\cos(mx)$ and `integrate`[^3] from $- \pi$ to $\pi$.  

$$\int_{-\pi}^{\pi}f(x)\cos(mx)dx=\int_{-\pi}^{\pi}A_{0}\cos(mx)dx+\sum_{n=1}^{\infty}\left(\int_{-\pi}^{\pi}a_{n}\cos(nx)\cos(mx)dx+\int_{-\pi}^{\pi}b_{n}\sin(nx)\cos(mx)dx\right)$$

$$=0+a_{n}\pi+0=a_{n}\pi\quad\text{for}~n=m$$

$$\therefore a_{n}=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\cos(nx)dx$$

### $b_n$

To find $b_n$, we will repeat the same process but we will multiply by $\sin(nx)$.

$$\therefore b_{n}=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\sin(nx)dx$$

## Results of Fourier Series

1. $$a_0 = \frac 1 \pi \int_{- \pi}^\pi f(x) dx = 2 \times \text{mean value of } f(x)$$

2. $$a_n = \frac 1 \pi \int_{- \pi}^\pi f(x) \cos(nx) dx = 2 \times \text{mean value of } f(x)\cos(nx)$$

3. $$a_n = \frac 1 \pi \int_{- \pi}^\pi f(x) \sin(nx) dx = 2 \times \text{mean value of } f(x)\sin(nx)$$

4. $$A_0 = \frac 1 2 a_0$$

## Example

Determine the [fourier series](#fourier-series) for the following `function`.[^2]  

$$f(x) = \frac \pi 2 \text{ and } 0 < x < 2\pi$$

$$f(x) = f(x + 2 \pi)$$

### Solution

We will now find the `coefficients`.

#### $a_0$

$$a_{0}=\frac{1}{\pi}\int_{0}^{2\pi}f(x)dx$$

$$=\frac{1}{\pi}\int_{0}^{2\pi}\left(\frac{x}{2}\right)dx$$

$$=\frac{1}{4\pi}\left[x^{2}\right]_{0}^{2\pi}$$

$$=\pi$$

#### $a_n$

$$a_{n}=\frac{1}{\pi}\int_{0}^{2\pi}f(x)\cos(nx)dx$$

$$=\frac{1}{\pi}\int_{0}^{2\pi}\left(\frac{x}{2}\right)\cos(nx)dx$$

$$=\frac{1}{2\pi}\int_{0}^{2\pi}x~\cos(nx)dx$$

$$=\frac{1}{2\pi}\left(\left[\frac{x~\sin(nx)}{n}\right]_{0}^{2\pi}-\frac{1}{n}\int_{0}^{2\pi}\sin(nx)dx\right)$$

$$=\frac{1}{2\pi}\left((0-0)-\frac{1}{n}(0)\right)$$

$$= 0$$

#### $b_n$

$$b_{n}=\frac{1}{\pi}\int_{0}^{2\pi}f(x)\sin(nx)dx$$

$$b_{n}=\frac{1}{\pi}\int_{0}^{2\pi}\left(\frac{x}{2}\right)\sin(nx)dx$$

$$=\frac{1}{2\pi}\left(\left[\frac{x~\cos(nx)}{n}\right]_{0}^{2\pi}+\frac{1}{n}\int_{0}^{2\pi}\cos(nx)dx\right)$$

$$=\frac{1}{2\pi}\left(\left[\frac{x \cdot \cos(nx)}{n}\right]_{0}^{2\pi}+\frac{1}{n}\left[\frac{\sin(nx)}{n}\right]_{0}^{2\pi}\right)$$

$$=\frac{1}{2\pi}\left((2\pi-0)+(0-0)\right)$$

$$=\frac{1}{n}$$

The general expression for [fourier series](#fourier-series) is

$$f(x)= \frac 1 2 a_0 + \sum_{n=1}^\infty (a_n \cos (nx) + b_n \sin(nx))$$

$$f(x) = \frac \pi 2 - \left(\sin (x) + \frac 1 2 \sin(2x) + \ldots\right)$$

## Dirichlet Conditions

If the [fourier series](#fourier-series) is represented as $f(x)$ then $f(x_1)$ will give an infinite `series`[^1] of $x_1$ which converges as more and more terms of the `series`[^1] are evaluated.  
For this to happen, following conditions should be satisfied

1. $f(x)$ must be defined and single valued.
2. $f(x)$ should be `continuous`[^4] or have a finite number of finite `discontinuities`[^4] over the `period`.[^5]
3. $f(x)$ and $f^\prime(x)$ should be piecewise continuous `functions`[^2] in the `periodic interval`.[^5]

## Effect of Harmonics

As more and more terms of [fourier series](#fourier-series) are evaluated, the `graph` of the `series`[^1] approaches the `graph` of the original `function`,[^2] the `series`[^1] represents.

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/42. Infinite Series/Lecture|series]].
[^2]: Read more about [[Mathematics/Function/Content|functions]].
[^3]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/25. Integrations/Lecture|integration]].
[^4]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/12. Continuity/Lecture|continuity]].
[^5]: Read more about [[semester 2/MTH301 - Calculus II/39. Periodic Functions/Lecture|period]].