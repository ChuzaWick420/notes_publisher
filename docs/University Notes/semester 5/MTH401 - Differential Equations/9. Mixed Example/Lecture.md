---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-10
---

<span style="color: gray;">Dated: 10-11-2024</span>

# Mixed Examples

## Example

$$y^\prime=\frac{x^2+y^2}{xy}$$

$$\frac{dy}{dx}=\frac{x^2+y^2}{xy}$$

Put $y = wx$ then  

$$\frac{dy}{dx}=w+x\frac{dw}{dx}$$

$$w+x\frac{dw}{dx}=\frac{x^2+w^2x^2}{x\times w}=\frac{1+w^2}{w}$$

$$w+x\frac{dw}{dx}=\frac{1}{w}+w$$

$$wdw=\frac{dx}{x}$$

After `integration`[^1]  

$$\frac{w^2}{2}=\ln x+\ln c$$

$$\frac{y^2}{2x^2}=\ln|xc|$$

$$y^2=2x^2\ln|xc|$$

## Example

$$xe^{2y}\frac{dy}{dx}+e^{2y}=\frac{\ln x}{x}$$

Put $e^{2y} = u$ and we get  

$$2e^{2y}\frac{dy}{dx}=\frac{du}{dx}$$

$$\frac{x}{2}\frac{du}{dx}+u=\frac{\ln x}{x}$$

$$\frac{du}{dx}+\frac{2}{x}u=2\frac{\ln x}{x^{2}}$$

$$u(x) =\exp\left(\int\frac{2}{x}dx\right)=x^{2}$$

$$x^{2}\frac{du}{dx}+2xu=2\ln x$$

$$\frac{d}{dx}(x^{2}u)=2\ln x$$

$$x^{2}u=2[x \ln x-x]+c$$

$$x^{2}e^{2y}=2[x \ln x-x]+c$$

### Example

$$x^4y^2y'+x^3y^3=2x^3-3$$

Put $x^3y^3 = u$ and we get  

$$3x^{2}y^{3}+3x^{3}y^{2}\frac{dy}{dx}=\frac{du}{dx}$$

$$3x^{3}y^{2}\frac{dy}{dx}=\frac{du}{dx}-3x^{2}y^{3}$$

$$x^{4}y^{2}\frac{dy}{dx}=\frac{x}{3}\frac{du}{dx}-x^{3}y^{3}$$

$$\frac{x}{3}\frac{du}{dx}=2x^{3}-3$$

$$\frac{du}{dx}=6x^{2}-\frac{9}{x}$$

`Integrating`[^1] both sides, we get  

$$u=2x^3-9\ln x+c$$

$$x^3y^3=2x^3-9\ln x+c$$

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[notes_publisher/docs/University Notes/semester 1/MTH101 - Calculus and Analytical Geometry/25. Integrations/Lecture|integration]].