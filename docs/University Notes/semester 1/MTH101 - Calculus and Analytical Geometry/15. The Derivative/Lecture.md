---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# The Derivative
We know that  

$$m_{tan} = \lim_{x_1 \rightarrow x_0} \frac{f(x_1) - f(x_0)}{x_1 - x_0}$$

Let us define a `constant` $h = x_1 - x_0$ such that $x_1 = h + x_0$.  
Substitute values and we will get  

$$m_{tan} = \frac{dy}{dx} =  \lim_{h \rightarrow 0} \frac{f(h + x_0) - f(x_0)}{h}$$

## Equation of Tangent line
Following is the equation of `tangent line` at a point $P(x_0, x_1)$.

$$y - y_0 = m(x - x_0)$$

We first find a $m$ from the `derivative` equation and then plug the values in to get the equation for `tangent`.

## Derivative Notation
The process of finding the `derivative` is called `differentiation`.  
The `derivative` of $f(x)$ with respect to $x$ can be written as.  

$$\frac{d}{dx}\left(f(x)\right) = f^{\prime}(x)$$

### Example

$$\left. \frac{d}{dx}\sqrt{x} \right|_{x = x_0} = \left. \frac{1}{2 \sqrt{x}} \right|_{x = x_0} = \frac{1}{2 \sqrt{x_0}} $$

## Existence of Derivatives
There are some situations when we can say that the `derivative` does not exist at a certain point for a `function`[^1].
1. The graph has _vertical `tangents`_.
2. The graph has _point of discontinuity_.
3. The graph has corners (can be made through `piece wise functions`[^1]).

## References

[^1]: Read more about [[Mathematics/Function/Content|functions]].
