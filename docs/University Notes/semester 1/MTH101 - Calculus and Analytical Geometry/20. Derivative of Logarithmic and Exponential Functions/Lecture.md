---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Derivative of Logarithmic Functions
There is a special `irrational constant` which is defined as:  

$$e = \sum_{n = 0}^\infty \frac{1}{n!}$$

We can alternatively define it in terms of `limits`[^1].  

$$e = \lim_{x \to 0} (1 + x)^{\frac{1}{x}} = \lim_{x \to 0}\left(1 + \frac{1}{x}\right)^x = 2.71\ldots$$

Let us define a `function`[^2] such as  

$$y = \log_b(x)$$

Then it can be `differentiated` as:  

$$\frac{dy}{dx}=\frac{d}{dx}[log_{b}(x)]$$

$$= \lim_{h\to0}\frac{log_{b}(x+h)-log_{b}(x)}{h}$$

Using the `theorems of logarithms`[^3]

$$=\lim_{h\to0}\frac{1}{h}log_{b}\left(\frac{x+h}{x}\right)$$

$$=\lim_{h\to0}\frac{1}{h}log_{b}\left(1+\frac{h}{x}\right)$$

Then we can define $v = \frac{h}{x}$. Substituting it, we get:  

$$=\lim_{v\to0}\frac{1}{vx}log_{b}(1+v)$$

Since the `limit`[^1] is in terms of `v`, therefore, the `x` is now treated as a `constant`.  

$$=\frac{1}{x}\lim_{v\to0}\frac{1}{v}log_{b}(1+v)$$

Using the `theorems of logarithms`[^3] again, we get:  

$$=\frac{1}{x}\lim_{v\to0}log_{b}(1+v)^{\frac{1}{v}}$$

Remember the `constant` we talked about in the beginning?  

$$=\frac{1}{x}log_{b}e$$

Using the `theorems of logarithm`[^3] again, we get  

$$= \frac{1}{x \cdot \ln(b)}$$

>Note: checkout the `logarithmic notation`[^4] to know what $\ln(b)$ means.

# Derivative of Natural Logarithm

$$\frac{d}{dx}[\ln(u)]=\frac{1}{u}\cdot\frac{du}{dx}$$

# Derivative of Exponential Functions

$$y = f(x) = b^x$$

Applying $\ln$ function on both sides  

$$\ln y = \ln b^x$$

$$= x \cdot \ln (b)$$

$$\frac{d}{dx}[\ln y]=\frac{d}{dx}[x \ln b]$$

$$\frac{1}{y}\frac{dy}{dx}=\ln b$$

$$\frac{dy}{dx}=y\cdot \ln b$$

$$= b^x \cdot \ln b$$

## Generalized Form

$$\frac{d}{dx}[b^{u}]=b^{u}\cdot \ln b\cdot\frac{du}{dx}$$

# Inverse Functions
Imagine 2 `functions`[^2], $f(x)$ and $g(x)$.  
If $f(g(x)) = x$ for every $x$ in domain of $g(x)$ and if $g(f(x)) = x$ for every $x$ in domain of $f(x)$, then we say both `functions`[^2] are `inverse` of each other.

## Example

$$f(x) = 2x$$

and there is also  

$$g(x) = \frac{x}{2}$$

Then to check, we try both of our conditions  

### Condition 1

$$f(g(x)) = 2 \left(\frac{x}{2}\right) = x$$

### Condition 2

$$g(f(x)) = \frac{1}{2} \cdot (2x) = x$$

For a `function`[^2] to have an `inverse`, one of the important conditions is that it should be a `one-to-one` function.  

$$y = f^{-1}(x) \implies f(y) = x$$

# Derivative of Inverse Functions

$$(f^{-1})(x) = \frac{1}{f^{'}(f^{-1}(x))}$$

Therefore,  

$$\frac{dy}{dx}=(f^{-1})^{\prime}(x)\Rightarrow\frac{dx}{dy}=f^{\prime}(y)=f^{\prime}(f^{-1}(x))$$

# References

[^1]: Read more about [[notes_publisher/docs/University Notes/semester 1/MTH101 - Calculus and Analytical Geometry/9. Limits (Intuitive Introduction)/Lecture|Limits]].
[^2]: Read more about [[notes_publisher/docs/Mathematics/Function/Content|functions]].
[^3]: Read more about [[notes_publisher/docs/Mathematics/Logarithm/Content|Theorems of logarithm]].
[^4]: Read more about [[notes_publisher/docs/Mathematics/Logarithm/Content|Logarithmic notation]].
