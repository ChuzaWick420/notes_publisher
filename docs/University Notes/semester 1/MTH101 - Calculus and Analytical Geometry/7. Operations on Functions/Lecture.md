---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Operations on Functions
Just like `numbers`, we can do operations on `functions`[^1] as well.  
Assume we have `2` `functions`[^1] such as:  

$$f(x) = x^2$$

$$g(x) = x + 1$$

## Addition

$$f(x) + g(x) = (f + g)(x) = x^2 + x + 1$$

## Subtraction

$$f(x) - g(x) = (f - g)(x) = x^2 - (x + 1)$$

## Multiplication

$$f(x) \cdot g(x) = (f \cdot g)(x) = x^2 \cdot (x + 1)$$

### Notation

$$f^n(x) = \prod^n f(x) = f(x) \cdot f(x) \cdot \ldots \cdot f(x)$$

## Division

$$\frac{f(x)}{g(x)} = \left(\frac{f}{g}\right)(x) = \frac{x^2}{x + 1}$$

The `domain`[^2] of these `functions`[^1] which result after operations, is the `intersection`[^3] of the `domains`[^2] of $f(x)$ and $g(x)$.

## Composition

$$f(g(x)) = (fog)(x) = (x+1)^2$$

$$g(f(x)) = (gof)(x) = x^2 + 1$$

Therefore,  

$$(fog)(x) \ne (gof)(x)$$

## Decomposition
Similarly, `functions`[^1] can be decomposed as well.  

$$h(x) = (x+1)^2$$

$$h(x) = (fog)(x) = f(g(x))$$

# Classification of Functions
## Constant
The `functions`[^1] whose `range`[^4] is equal to a `constant number` is called a `constant function`.

## Monomial in `x`
Anything of the form  

$$f(x) = cx^n ; x \in \mathbb{Z}^+ + \{0\}$$

## Polynomial in `x`
Anything of the form  

$$f(x) = \sum_{i = 0}^n a_ix^i = a_0 + a_1x^1 + \ldots + a_nx^n$$

# References

[^1]: [[notes_publisher/docs/Mathematics/Function/Content|Functions]]
[^2]: [[notes_publisher/docs/Mathematics/Function/Content|Domain]]
[^3]: [[notes_publisher/docs/Mathematics/Set/Content|Intersection]]
[^4]: [[notes_publisher/docs/Mathematics/Function/Content|Range]]
