---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Examples

## Sum of `Fourier Series`[^1] at the point of `Discontinuity`[^2]

Let us say we have a point of `discontinuty` at $x = x_1$ such that there is a _jump_ in value of $f(x)$ from $y_1$ to $y_2$.  
To denote this, we say  

### For Left Side

$$f(x) = f(x_1 - 0)$$

### For Right Side

$$f(x) = f(x_1 + 0)$$

When we find the `fourier series`,[^1] it turns out that the `series`[^3] converges to the `average` of $y_1$ and $y_2$.

### Example

Consider the `function`[^4]  

$$f(x) = 0 \quad - \pi < x < 0$$

$$f(x) = a \quad 0 < x < \pi$$

$$f(x) = f(x + 2 \pi)$$

### Solution

#### $a_0$

$$a_{0}=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)dx$$

$$=\frac{1}{\pi}\int_{0}^{\pi}a~dx$$

$$=\frac{1}{\pi}[ax]_{0}^{\pi}=a$$

#### $a_n$

$$a_{n}=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\cos(nx)dx$$

$$=\frac{1}{\pi}\int_{0}^{\pi}a \cdot \cos(nx)dx$$

$$=\frac{a}{\pi}\left[\frac{\sin~nx}{n}\right]_{0}^{\pi}$$

$$= 0$$

#### $b_n$

$$b_{n}=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\sin(nx)dx$$

$$=\frac{1}{\pi}\int_{0}^{\pi}a \cdot \sin(nx)dx$$

$$=\frac{a}{\pi}\left[\frac{-\cos(nx)}{n}\right]_{0}^{\pi}$$

$$=\frac{a}{n\pi}(1-\cos(n\pi))$$

##### If $n$ is even

$$b_n = 0$$

##### If $n$ is Odd

$$b_n = \frac {2a}{n \pi}$$

$$\because f(x)=\frac{1}{2}a_{0}+\sum_{n=1}^{\infty}b_{n} \cdot \sin(nx)$$

$$f(x)=\frac{a}{2}+\frac{2a}{\pi}\left(\sin(x)+\frac{1}{3}\sin(3x)+\frac{1}{5}\sin(5x)+\ldots\right)$$

The point of `discontinuity`[^2] in this `function`[^4] is $x = 0$.  
If we put that in $f(x)$, all the $\sin(x)$ terms vanish and we are left with $\frac a 2$ which is the average between $0$ and $a$.

## Half Range `Series`[^3]

Sometimes, a `function`[^4] is defined over only $0$ to $\pi$ range, not $- \pi$ to $\pi$ or $0$ to $2 \pi$ range.

### Example

Determine a `half range sin series` to represent the following `function`[^4]  

$$f(x) = 1 + x \quad 0 < x < \pi$$

$$f(x) = f(x + 2 \pi)$$

#### Solution

$$\because a_0 = 0 \text{ and } a_n = 0$$

$$b_{n}=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\sin(nx)dx$$

$$b_{n}=\frac{2}{\pi}\int_{0}^{\pi}f(x)\sin(nx)dx$$

$$b_{n}=\frac{2}{\pi}\int_{0}^{\pi}(1+x)\sin(nx)dx$$

$$=\frac{2}{\pi}\left(\left[(1+x)\frac{-\cos(nx)}{n}\right]_{0}^{\pi}+\frac{1}{n}\int_{0}^{\pi}\cos(nx)dx\right)$$

$$=\frac{2}{\pi}\left(-\frac{1+\pi}{n}\cos(n\pi)+\frac{1}{n}+\frac{1}{n}\left[\frac{\sin(nx)}{n}\right]_{0}^{\pi}\right)$$

$$=\frac{2}{\pi}\left(\frac{1}{n}-\frac{1+\pi}{n}\cos(n\pi)\right)$$

$$=\frac{2}{\pi n}(1-(1+\pi)\cos(n\pi))$$

##### If $n$ is even

$$\because \cos(n\pi) = 1$$

$$\therefore b_n = - \frac 2 n$$

##### If $n$ is Odd

$$\because \cos(n\pi) = -1$$

$$\therefore b_n = \frac{4 + 2 \pi}{\pi n}$$

Substituting into the general equation, we have  

$$f(x) = \left(\frac 4 \pi + 2\right)\left(\sin (x) + \frac 1 3 \sin (3x) + \frac 1 5 \sin (5x)\right) - 2 \left(\frac 1 2 \sin(2x) + \frac 1 4 \sin(4x)\right)$$

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 2/MTH301 - Calculus II/40. Fourier Series/Lecture|fourier series]].
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/12. Continuity/Lecture|continuity]].
[^3]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/42. Infinite Series/Lecture|series]].
[^4]: Read more about [[Mathematics/Function/Content|functions]].