---
tags:
  - university-notes
  - integral
  - differentiation
university-name: Virtual University of Pakistan
---

# Second Fundamental Theorem of Calculus

## Dummy Variable
If we change the `letter` for the `variable` of `integration`[^1] but don't change the `limits`, then values of `definite integrals`[^2] remains the same  

$$\int_{1}^{2}x^{2}dx=\frac{x^{3}}{3}\bigg]_{1}^{2}=\frac{26}{3}$$

$$\int_{1}^{2}f(t)dt=\frac{t^{3}}{3}\bigg]_{1}^{2}=\frac{26}{3}$$

$$\int_{1}^{2}f(y)dy=\frac{y^{3}}{3}\bigg]_{1}^{2}=\frac{26}{3}$$

## `Definite integral`[^2] With Variable Upper Limit
If we have an `integral`[^1] of the form  

$$\int^x_a$$

Then we have to use different letter for the `variable` of `integration`[^1] to differentiate it from the `upper limit`. Such as

$$\int_{2}^{x}t^{2}dt$$

## The Theorem

$$A(x)=\int_{a}^{x}f(t)dt$$

$$\frac{d}{dx}(A(x))=A'(x)=\frac{d}{dx}\left(\int_{a}^{x}f(t)dt\right)=f(x)$$

If the `integrand`[^1] is `continuous`[^3], then the `derivative`[^4] of a `definite integral`[^2] with respect to its `upper limit` is equal to the `integrand`[^1] evaluated at the `upper limit`.  

$$\frac{d}{dx}\left(\int_{a}^{x}f(t)dt\right)=f(x)$$

## References
Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/25. Integrations/Lecture|integration]].
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/29. Definite Integral/Lecture|definite integrals]].
[^3]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/12. Continuity/Lecture|continuity]].
[^4]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/15. The Derivative/Lecture|derivatives]].
