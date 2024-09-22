---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Techniques of Differentiation
## Derivatives of Constant Functions

$$\frac{d}{dx} (c) = 0$$

### Proof

$$\lim_{h \rightarrow 0} \frac{f(h + x) - f(x)}{h}$$

Since we know that $f(h + x) = f(x) = c$.

$$ =\lim_{h \rightarrow 0} \frac{0 - 0}{h}$$

$$= \lim_{h \rightarrow 0} \frac{0}{h}$$

$$ = \lim_{h \rightarrow 0} 0$$

$$ = 0$$

## Power Rule

$$\frac{d}{dx}(x^n) = n \cdot x^{n - 1}$$

### Proof

$$\frac{d}{dx}(x^n) = \lim_{h \rightarrow 0} \frac{f(x+h) - f(x)}{h}$$

$$= \lim_{h \rightarrow 0} \frac{(x + h)^n - x^n}{h}$$

Using `binomial theorem`[^1]  

$$= \lim_{h \rightarrow 0} \frac{\left[x^n + nx^{n-1}h + \ldots + h^n\right] - x^n}{h}$$

$$= \lim_{h \rightarrow 0} \frac{nx^{n-1}h + \ldots + h^n}{h}$$

Taking $h$ as common factor, out  

$$= \lim_{h \rightarrow 0} \frac{h \left(nx^{n-1} + \ldots + h^{n- 1}\right)}{h}$$

$$= \lim_{h \rightarrow 0} \left(nx^{n-1} + \ldots + h^{n - 1}\right)$$

Since all the terms except for _first_ one include some factor of $h$, most of the terms become `null`.  

$$= nx^{n-1}$$

## Sum or Difference of the Functions

$$\frac{d}{dx}\left(f(x) + g(x)\right) = \frac{d}{dx}(f(x)) + \frac{d}{dx}(g(x))$$

### Proof

$$\frac{d}{dx}\left(f(x) + g(x)\right) = \lim_{h \rightarrow 0} \frac{f(x+h) + g(x + h) - f(x) - g(x)}{h}$$

$$\frac{d}{dx}\left(f(x) + g(x)\right) = \lim_{h \rightarrow 0} \frac{f(x+h)  - f(x) + g(x + h) - g(x)}{h}$$

$$\frac{d}{dx}\left(f(x) + g(x)\right) = \lim_{h \rightarrow 0} \frac{f(x+h)  - f(x)}{h} + \lim_{h \rightarrow 0} \frac{g(x + h) - g(x)}{h}$$

$$\frac{d}{dx}\left(f(x) + g(x)\right) = \frac{d}{dx} f(x) + \frac{d}{dx} g(x)$$

## Product

$$\frac{d}{dx}\left(f(x) \cdot g(x)\right) = f(x) \cdot \frac{d}{dx} g(x) + g(x) \cdot \frac{d}{dx} f(x)$$

### Proof

$$\frac{d}{dx}\left(f(x) \cdot g(x)\right) = \lim_{h \rightarrow 0} \frac{f(x + h) \cdot g(x + h) - f(x) \cdot g(x)}{h}$$

$$= \lim_{h \rightarrow 0} \frac{f(x + h) \cdot g(x + h) - f(x) \cdot g(x)}{h}$$

Adding and subtracting $f(x + h) \cdot g(x)$  

$$= \lim_{h \rightarrow 0} \frac{f(x + h) \cdot g(x + h) - f(x + h) \cdot g(x) + f(x + h) \cdot g(x) - f(x) \cdot g(x)}{h}$$

$$= \lim_{h \rightarrow 0} \frac{f(x + h) \cdot \left( g(x + h) - g(x) \right) + g(x) \cdot \left(f(x + h) - f(x) \right)}{h}$$

$$= \lim_{h \rightarrow 0} \frac{f(x + h) \cdot \left( g(x + h) - g(x) \right)}{h} + \lim_{h \rightarrow 0}\frac{g(x) \cdot \left(f(x + h) - f(x) \right)}{h}$$

$$= f(x) \cdot \frac{d}{dx} g(x) + g(x) \cdot \frac{d}{dx} f(x)$$

## Quotient

$$\frac{d}{dx} \left[ \frac{f(x)}{g(x)} \right] = \frac{g(x) \frac{d}{dx}[f(x)] - f(x) \frac{d}{dx}[g(x)]}{[g(x)]^2}
$$

### Proof
![[Pasted image 20240817144720.png]]

## Reciprocal Theorem

$$\frac{d}{dx} \left( \frac{1}{g(x)} \right) = -\frac{\frac{d}{dx} \left( g(x) \right)}{\left( g(x) \right)^2}
$$

## References

[^1]: Read more about [[notes_publisher/docs/Mathematics/Binomial Theorem/Content|binomial theorem]].
