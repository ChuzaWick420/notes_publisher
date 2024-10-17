---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Definite Integral
## Wallis Sine Formula

When $n$ is `even`  

$$= \frac{n - 1}{n} \cdot \frac{n - 3}{n - 2} \cdot \ldots \cdot \frac 3 4 \cdot \frac 1 2 \cdot \frac \pi 2$$

When $n$ is `odd`  

$$\int_0^{\frac \pi 2} \sin^n(x)dx = \int_0^{\frac \pi 2} \cos^n(x)dx = \prod_{i = 0}^{\frac {n - 3} 2} \frac{n - 2i - 1}{n - 2i}$$

$$= \frac{n - 1}{n} \cdot \frac{n - 3}{n - 2} \cdot \ldots \cdot \frac 6 7 \cdot \frac 4 5 \cdot \frac 2 3$$

## Integration by Parts

$$\int UVdx=U\int Vdx-\int\left(\int Vdx\cdot\frac{dU}{dx}\right)dx$$

## Line Integrals
![[Pasted image 20241017153458.png]]  
Let us say we have a curve $C$ defined by $f(x)$ and $P$ be a point on this curve.  
The `position vector`[^1] for $P$ with respect to `origin` will be $\vec P$ or let's say $\vec r$.  
Similarly, now imagine there is another point $Q$ with `position vector`[^1] $\vec Q$  
where $\vec Q = \vec P + \vec {PQ}$.  
Let us say that $\vec {PQ} = \vec dr$

If we divide the curve $f(x)$ into multiple sections then the length of whole curve will be a sum of lengths of each section.  

$$\sum_{p = 1}^n dr_p$$

Here $p$ is just an `index`.  

$$\lim_{dr \to 0} \sum_{p = 1}^n dr_p = \int_c dr$$

## References
Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 2/MTH301 - Calculus II/10. Introduction to vectors/Lecture|vectors]].
