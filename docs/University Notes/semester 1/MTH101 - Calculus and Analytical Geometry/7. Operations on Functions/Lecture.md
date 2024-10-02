---
tags:
  - university-notes
  - composite-functions
  - function-operations
  - sigma
university-name: Virtual University of Pakistan
---

# Operations on Functions
## Operations
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

$$f^n(x) = \prod^n f(x) = f(x) \times f(x) \times \ldots \times f(x)$$

## Division

$$\frac{f(x)}{g(x)} = \left(\frac{f}{g}\right)(x) = \frac{x^2}{x + 1}$$

The `domain`[^2] of these `functions`[^1] which result after operations, is the `intersection`[^3] of the `domains`[^2] of $f(x)$ and $g(x)$.  
Basically saying that we need certain `set`[^4] of values which work for both `functions`[^1].

## Composition

$$f(g(x)) = (fog)(x) = (x+1)^2$$

$$g(f(x)) = (gof)(x) = x^2 + 1$$

Therefore,  

$$(fog)(x) \ne (gof)(x)$$

## Decomposition
Similarly, `functions`[^1] can be decomposed as well.  

$$h(x) = (x+1)^2$$

$$h(x) = (fog)(x) = f(g(x))$$

## Classification of Functions
### Constant
The `functions`[^1] whose `range`[^5] is equal to a `constant number` is called a `constant function`.

### Monomial in $x$
Anything of the form  

$$f(x) = cx^n ; x \in \mathbb{Z}^+ + \{0\}$$

### Polynomial in $x$
Anything of the form  

$$f(x) = \sum_{i = 0}^n a_ix^i = a_0 + a_1x^1 + \ldots + a_nx^n$$

## References
Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[Mathematics/Function/Content|functions]].
[^2]: Read more about [[Mathematics/Function/Content|domain]].
[^3]: Read more about [[Mathematics/Set/Content|intersection]].
[^4]: Read more about [[Mathematics/Function/Content|range]].
[^5]: Read more about [[Mathematics/Set/Content|sets]].
