---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-10
---

<span style="color: gray;">Dated: 10-11-2024</span>

# Mixed Examples

## Example

$$y(1+2xy)dx+x(1-2xy)dy=0$$

This equation is not 
- `Separable`[^1]
- `Homogeneous`[^2]
- `Exact`[^3]
- `Linear`[^4]
- `Bernoulli`[^5]

After staring long enough, we notice that  

$$u = 2xy$$

$$y = \frac u {2x}$$

$$\because dy = \frac{xdu - udx}{2x^2}$$

$$2u^2dx+(1-u)xdu=0$$

$$2\ln|x|-u^{-1}-\ln|u|=c$$

$$\ln|\frac{x}{2y}|=c+\frac{1}{2xy}$$

$$\frac{x}{2y}=c_{1}e^{\frac 1 {2xy}}$$

$$x=2c_{1}ye^{\frac 1 {2xy}}$$

## Example

$$\frac{d^{2}y}{dx^{2}}=2x\left(\frac{dy}{dx}\right)^{2}$$

$$u = y^\prime$$

$$\frac{du}{dx}=y^{\prime\prime}$$

$$\frac{du}{dx}=2xu^2$$

$$\frac{du}{u^2}=2xdx$$

$$\int u^{-2}du=\int 2xdx$$

$$-u^{-1}=x^2+c_1$$

$$u^{-1}=\frac{1}{y'}$$

$$\frac{dy}{dx}=-\frac{1}{x^{2}+c_{1}^{2}}$$

$$dy=-\frac{dx}{x^{2}+c_{1}^{2}}$$

$$\int dy=-\int \frac{dx}{x^{2}+c_{1}^{2}}$$

$$y+c_{2}=-\frac{1}{c_{1}}\tan^{-1}\frac{x}{c_{1}}$$

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[notes_publisher/docs/University Notes/semester 5/MTH401 - Differential Equations/3. Separable Equations/Lecture|separable equations]].
[^2]: Read more about [[notes_publisher/docs/University Notes/semester 5/MTH401 - Differential Equations/4. Homogeneous Differential Equations/Lecture|homogeneous differential equations]].
[^3]: Read more about [[notes_publisher/docs/University Notes/semester 5/MTH401 - Differential Equations/5. Exact Differential Equations/Lecture|exact differential equations]].
[^4]: Read more about [[notes_publisher/docs/University Notes/semester 5/MTH401 - Differential Equations/7. First Order Linear Equation/Lecture|first order linear differential equations]].
[^5]: Read more about [[notes_publisher/docs/University Notes/semester 5/MTH401 - Differential Equations/8. Bernoulli Equations/Lecture|bernoulli equation]].