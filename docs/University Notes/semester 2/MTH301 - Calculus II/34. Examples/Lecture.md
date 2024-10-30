---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Examples

## Example

Evaluate the following `integral`[^1] around the region $R$ bounded by the curves $y = x^2$ and $x = y^2$ by using `green's theorem`.[^2]  

$$I = \oint_C (xy dx+ (2x - y) dy)$$

### Solution

First of all, for the boundaries of `integral`,[^1] we need to find the `intersection points`.  

$$\because y^2 = x$$

$$\therefore y = \sqrt x$$

We will ignore the $-\sqrt x$ because we only care about first `quadrant`.[^3]  
We know that the $y$ values will be the same for both equations at the intersections.  
Therefore,  

$$\sqrt x = x^2$$

Squaring both sides, we get  

$$x = x^4$$

$$0 = x^4 - x$$

$$0 = x(x^3 - 1)$$

$$x = 0 \text{ and } x^3 - 1 = 0$$

$$\implies x^3 = 1$$

$$x = 1$$

We can put $x = 0, 1$ in either equation and we will get $y = 0, 1$.  
Therefore, our intersection points are $(0, 0)$ and $(1, 1)$.

$$\because I = \oint_C (xy dx+ (2x - y) dy)$$

$$\therefore P = xy \implies \frac{\partial P}{\partial y} = x$$

$$\therefore Q = 2x - y \implies \frac{\partial Q}{\partial x} = 2$$

Using the `green's theorem`[^2]  

$$= - \iint_R \left(\frac{\partial P}{\partial y} - \frac{\partial Q}{\partial x}\right)dxdy$$

$$= - \iint_R (x - 2)dxdy$$

$$= - \int_0^1\int_{y = x^2}^{y = \sqrt x} (x - 2) dy dx$$

$$= - \int_0^1 (x - 2) \left[y\right]_{x^2}^{\sqrt x}dx$$

$$=-\int_{0}^{1}(x-2)(\sqrt{x}-x^{2})dx$$

$$=\int_{0}^{1}(x^{\frac 3 2}-x^{3}-2x^{\frac 1 2}+2x^{2})dx$$

$$=-\left[\frac{2}{5}x^{\frac 5 2}-\frac{1}{4}x^{4}-\frac{4}{3}x^{\frac 3 2}+\frac{2}{3}x^{3}\right]_{0}^{1}$$

$$= \frac {31}{60}$$

## Gradient of a Scalar `Function`[^4]

If $\phi$ is a scalar `function`[^4] then its `gradient` is  

$$\nabla \phi = \left(\hat i \frac {\partial}{\partial x} + \hat j \frac {\partial}{\partial y} + \hat k \frac {\partial}{\partial z}\right) \phi$$

$$= \hat i \frac {\partial \phi}{\partial x} + \hat j \frac {\partial \phi}{\partial y} + \hat k \frac {\partial \phi}{\partial z}$$

## Divergence of a Vector Function

If $\vec A(a_1, a_2, a_3) = a_1 \hat i + a_2 \hat j + a_3 \hat k$  
then  

$$\nabla \cdot \vec A=\left(\hat{i}\frac{\partial}{\partial x}+\hat{j}\frac{\partial}{\partial y}+\hat{k}\frac{\partial}{\partial z}\right)\cdot(\hat{a}_{1}\hat{i}+\hat{a}_{2}\hat{j}+\hat{a}_{3}\hat{k})$$

$$=\frac{\partial a_{1}}{\partial x}+\frac{\partial a_{2}}{\partial y}+\frac{\partial a_{3}}{\partial z}$$

## Curl of a Vector Function

If $\vec A(a_1, a_2, a_3) = a_1 \hat i + a_2 \hat j + a_3 \hat k$  
then

$$\nabla \times \vec A=\left(\hat{i}\frac{\partial}{\partial x}+\hat{j}\frac{\partial}{\partial y}+\hat{k}\frac{\partial}{\partial z}\right)\times(\hat{a}_{1}\hat{i}+\hat{a}_{2}\hat{j}+\hat{a}_{3}\hat{k})$$

$$
=
\left|
\begin{matrix}
	\hat i & \hat j & \hat k \\
	\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
	a_1 & a_2 & a_3
\end{matrix}
\right|
$$

$$\nabla\times \vec A=\hat{i}\left(\frac{\partial a_{3}}{\partial y}-\frac{\partial a_{2}}{\partial z}\right)+\hat{j}\left(\frac{\partial a_{1}}{\partial z}-\frac{\partial a_{3}}{\partial x}\right)+\hat{k}\left(\frac{\partial a_{2}}{\partial x}-\frac{\partial a_{1}}{\partial y}\right)$$

After playing around with these, you will come across following results

1. $$\nabla \times (\nabla \phi) = 0$$

2. $$\nabla \cdot (\nabla \times \vec A) = 0$$

3. $$\nabla \cdot (\nabla \phi) = \frac{\partial^{2}\phi}{\partial x^{2}}+\frac{\partial^{2}\phi}{\partial y^{2}}+\frac{\partial^{2}\phi}{\partial z^{2}}$$

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/25. Integrations/Lecture|integrals]].
[^2]: Read more about [[semester 2/MTH301 - Calculus II/33. Examples/Lecture|green's theorem]].
[^3]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/3. Coordinate Planes and Graphs/Lecture|quadrants]].
[^4]: Read more about [[Mathematics/Function/Content|functions]].