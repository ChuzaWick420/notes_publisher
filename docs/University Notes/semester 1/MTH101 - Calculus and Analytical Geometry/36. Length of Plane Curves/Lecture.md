---
tags:
  - university-notes
  - integral
  - sigma
  - limits
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Length of Plane Curves

## The Arc Length Problem

The `continuous functions`[^1] are also called `smooth functions` and their `graphs` are called `smooth curves`.  
![[Pasted image 20240928102906.png]]

We can divide the curve into small enough `intervals`[^2] such that the distances between the points on the curve appear to be within a straight `line`.[^3]  
This way, we can cover the whole curve and accurately measure the `arc length`.

![[Pasted image 20240928104406.png]]  
If we want to know the `length` of $\overline{P_0 P_1}$, we can use `pythagorus theorem`.  

$$m\overline{P_0 P_1} = \sqrt{\Delta x^2 + \Delta y^2}$$

$$\because \Delta x = x_1 - x_0$$

$$\because \Delta y = f(x_1) - f(x_0)$$

$$m\overline{P_0 P_1} = \sqrt{(x_1 - x_0)^2 + (f(x_1) - f(x_0))^2}$$

Let's generalize this equation.  

$$L_i = m \overline{P_{i - 1} P_i}$$

$$L_i = \sqrt{(x_{i} - x_{i - 1})^2 + (f(x_i) - f(x_{i - 1}))^2}$$

According to `mean value theorem`[^4]  

$$\frac{f(x_i)-f(x_{i-1})}{x_i-x_{i-1}}=f'(x_i^*)$$

$$\Rightarrow f(x_i)-f(x_{i-1})=f'(x_i^*)(x_i-x_{i-1})=f'(x_i^*)\Delta x_i$$

Plugging these into our equation, we get  

$$L_i=\sqrt{(\Delta x_i)^2+(f'(x_i^*))^2(\Delta x_i)^2}$$

$$L_i=\sqrt{(\Delta x_i)^2(1 + (f'(x_i^*))^2)}$$

$$L_i=\sqrt{1+(f'(x_i^*))^2}\Delta x_i$$

Therefore, for the whole polygonal path, we have  

$$\sum_{i=1}^{n}L_{i}=\sum_{i=1}^{n}\sqrt{1+(f^{\prime}(x_{i}^{*}))^{2}}\Delta x_{i}$$

And we know that our approximation gets better as the distance between the `intervals`[^2] decreases, therefore,  

$$L=\lim_{\max(\Delta x_i\to 0)}\sum_{i=1}^{n}\sqrt{1+(f^{\prime}(x_{i}^{*}))^{2}}\Delta x_{i}$$

Of course, we can re-write it in `integral`[^5] form.  

$$L=\int_{a}^{b}\sqrt{1+(f^{\prime}(x))^{2}}dx$$

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/12. Continuity/Lecture|continuity]].
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/1. Coordinates, Graphs, Lines/Lecture|intervals]].
[^3]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/4. Lines/Lecture|lines]].
[^4]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/24. Newton's Method, Rolle's Theorem and Mean Value Theorem/Lecture|mean value theorem]].
[^5]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/25. Integrations/Lecture|integrals]].