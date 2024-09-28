---
tags:
  - university-notes
  - limits
university-name: Virtual University of Pakistan
---

# L'Hopital's Rule
## Indeterminate Forms
### Type $\frac 0 0$
We can have expressions like  

$$\lim_{x \to 2} \frac{x^2 - 4}{x - 2}$$

$$\lim_{x \to 0} \frac{\sin x}{x}$$

Which may or may not _converge_ and what they _do_ converge to is not immediately obvious.  
Therefore, we need `L'Hopital's Rule`.

#### The Rule
If $\lim f(x) = \lim g(x) = 0$ and $\lim \frac{f^{\prime}(x)}{g^{\prime}(x)}$ gives us a _finite_ value $L$ or $+\infty$ or $-\infty$ then  

$$\lim \frac{f(x)}{g(x)} = \lim \frac{f^{\prime}(x)}{g^{\prime}(x)}$$

##### Steps
1. Check if $\lim \frac{f(x)}{g(x)}$ is in `indeterminate` form. If it is _not_ then the rule cannot be used.
2. Differentiate $f(x)$ and $g(x)$ separately.
3. Find $\lim \frac{f^{\prime}(x)}{g^{\prime}(x)}$ and if it is finite, $+\infty$ or $-\infty$ then

$$\lim \frac{f(x)}{g(x)} = \lim \frac{f^{\prime}(x)}{g^{\prime}(x)}$$

#### Example

$$\lim_{x \to 2} \frac{x^2 - 4}{x - 2}$$

##### Step 1

$$\lim_{x \to 2} (x^2 - 4) = 0$$

$$\lim_{x \to 2} (x - 2) = 0$$

##### Step 2

$$\lim_{x \to 2}\frac{(x^{2}-4)}{x-2}$$

$$=\lim_{x \to 2}\frac{\frac{d}{dx}[x^{2}-4]}{\frac{d}{dx}[x-2]} $$

$$=\lim_{x \to 2}\frac{2x}{1}=4$$

##### Step 3

$$\lim_{x \to 2} \frac{x^2 - 4}{x - 2} = 4$$

### Type $\frac \infty \infty$

If $\lim f(x) = \lim g(x) = \infty$ and $\lim \frac{f^{\prime}(x)}{g^{\prime}(x)}$ gives us a _finite_ value $L$ or $+\infty$ or $-\infty$ then  

$$\lim \frac{f(x)}{g(x)} = \lim \frac{f^{\prime}(x)}{g^{\prime}(x)}$$

#### Example
Evaluate  

$$\lim_{x \to +\infty} = \frac {x}{e^x}$$

##### Step 1

$$\lim_{x \to +\infty} x = +\infty$$

$$\lim_{x \to +\infty} e^x = +\infty$$

##### Step 2

$$\lim_{x\rightarrow \infty}\frac{x}{e^{x}}$$

$$=\lim_{x\rightarrow \infty}\frac{\frac{d}{dx}[x]}{\frac{d}{dx}[e^{x}]}$$

$$=\lim_{x\rightarrow \infty}\frac{1}{e^{x}}=0$$

##### Step 3

$$\lim_{x \to +\infty} = \frac {x}{e^x} = 0$$

### Type $0 \cdot \infty$
If we have $f(x) = 0$ and $g(x) = \infty$ then a `product limit`[^1] $\lim f(x) \cdot g(x)$ is of the form $0 \cdot \infty$ and to apply the rule on it, we need to convert it into either $\frac 0 0$ form or $\frac \infty \infty$ form.

- $$\lim f(x) \cdot g(x) = \frac{f(x)}{\frac{1}{g(x)}} = \frac 0 0$$

- $$\lim f(x) \cdot g(x) = \frac{g(x)}{f(x)} = \frac \infty \infty$$

#### Example
Evaluate  

$$\lim_{x \to 0^+} x \ln x$$

##### Step 1

$$\lim_{x \to 0^+} x \ln x = \lim_{x \to 0^+} \frac{\ln x}{\frac 1 x}$$

$$\lim_{x \to 0^+} \ln x = -\infty$$

$$\lim_{x \to 0^+} \frac 1 x = + \infty$$

##### Step 2

$$\lim_{x \to 0^+} \frac{\frac{d}{dx} \ln x}{\frac{d}{dx} \frac{1}{x}}$$

$$= \lim_{x \to 0^+} \frac{1/x}{- 1/x^2} = \lim_{x \to 0^+} (-x) = 0$$

##### Step 5

$$\lim_{x \to 0^+} x \ln x = 0$$

## References

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/9. Limits (Intuitive Introduction)/Lecture|limits]].
