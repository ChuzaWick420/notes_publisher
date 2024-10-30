---
tags:
  - university-notes
  - differentiation
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Implicit Differentiation

Imagine we have a `function`[^1] defined as:  

$$yx = 1$$

We can `differentiate` it by solving for `y` first.  

$$y = \frac{1}{x}$$

$$\frac{d}{dx} y = \frac{d}{dx} \left(\frac{1}{x}\right)$$

$$\frac{dy}{dx} = -\frac{1}{x^2}$$

Alternatively, we can also do it by _without_ solving for `y`.  

$$yx = 1$$

Applying `chain rule`.[^2]  

$$x\frac{d}{dx}(y)+y\frac{d}{dx}(x)=0$$

$$x\frac{dy}{dx}+y(1)=0$$

$$x\frac{dy}{dx}=-y$$

$$\frac{dy}{dx}=-\frac{y}{x}$$

Then we find the value of `y` and substitute it.  
From the original equation, we get:  

$$y = \frac{1}{x}$$

Place it in the previous equation and we get.

$$\frac{dy}{dx} = -\frac{1}{x^2}$$

This method of `differentiation` without finding value of `y` is called `implicit differentiation`.

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[Mathematics/Function/Content|functions]].
[^2]: Read more about [[docs/University Notes/semester 1/MTH101 - Calculus and Analytical Geometry/18. The Chain Rule/Lecture|chain rule]].