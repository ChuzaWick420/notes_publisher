---
tags:
  - university-notes
  - calculus
university-name: Virtual University of Pakistan
---

# Limit of Multivariable Functions

$$f(x, y) = \sin^{^-1}(x + y)$$

The `domain`[^1] of this `function`[^1] is  

$$-1 \le x + y \le 1$$

We can approach a point in `space` with infinite paths as such  
![[Pasted image 20241005211205.png]]

## Rules for Non Existence of a Limit
If we have  

$$\lim_{(x, y) \to (a, b)} f(x, y)$$

and the `function`[^1] approaches different values as we use different paths then the `limit`[^2] does not exist.

## Rules for `limits`[^2]
If we have the following  

$$\lim_{(x,y) \to (x_0,y_0)} f(x,y) = L_1$$

$$\lim_{(x,y) \to (x_0,y_0)} g(x,y) = L_2$$

then

1. $$\lim_{(x,y) \to (x_0,y_0)} cf(x,y) = cL_1; c \in \mathbb{R}$$

2. $$\lim_{(x,y) \to (x_0,y_0)} (f(x,y) + g(x,y)) = L_1 + L_2$$

3. $$\lim_{(x,y) \to (x_0,y_0)} (f(x,y) - g(x,y)) = L_1 - L_2$$

4. $$\lim_{(x,y) \to (x_0,y_0)} (f(x,y) \cdot g(x,y)) = L_1 \cdot L_2$$

5. $$\lim_{(x,y) \to (x_0,y_0)} \frac{f(x,y)}{g(x,y)} = \frac{L_1}{L_2}$$

6. $$\lim_{(x,y) \to (x_0,y_0)} c = c; c \in \mathbb{R}$$

## References
Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[docs/Mathematics/Function/Content|functions]].
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/9. Limits (Intuitive Introduction)/Lecture|limits]].
