---
tags:
  - university-notes
  - line-integral
  - integral
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Line Integral

## Example

Evaluate $\int_C (x + 3y) dx$ from $A(0, 1)$ and $B(2, 5)$ along the curve $y = 1 + x^2$

### Solution

$$I = \int_C (P dx + Q dy)$$

$$\because Q = 0$$

$$\because C: y = 1 + x^2$$

$$\therefore I = \int_0^2 (x + 3(1 + x^2)) dx$$

$$= \int_0^2 (x + 3 + 3x^2)dx$$

$$=\left[\frac{x^{2}}{2}+3x+x^{3}\right]_{0}^{2}=16$$

## Example

Evaluate the following from $O(0, 0)$ to $A(1, 0)$ along the `line`[^1] $y = 0$ and then from $A(1, 0)$ to $B(1, 4)$ along the `line`[^1] $x = 1$.

$$I=\int_{C}((x^{2}+2y)dx+xydy)$$

### Solution

$$I_C = I_{c_1} + I_{c_2}$$

$$C = \overline{OA} + \overline{AB}$$

$$c_1: y = 0 \therefore dy = 0$$

$$c_2: x = 1 \therefore dx = 0$$

Substituting these values in our `integral`,[^2] we get  

$$I_{c_1}=\int_{0}^{1}x^{2}dx=\left[\frac{x^{3}}{3}\right]_{0}^{1}=\frac{1}{3}$$

Similarly,  

$$I_{c_2}=\int_{0}^{4}ydy=\left[\frac{y^{2}}{2}\right]_{0}^{4}=8$$

$$\therefore I = 8 + \frac 1 3 = \frac {25} 3$$

## Properties of line Integrals

1. $$\int_{C}Fds=\int_{C}\{Pdx+Qdy\}$$

2. $$\int_{AB}Fds=-\int_{BA}Fds$$

3. We can have paths which are parallel to the axes.
	1. For being parallel to $y$ axis, $\int_C P dx = 0$ and $I_c = \int_c Q dy$
	2. For being parallel to $x$ axis, $\int_C Q dy = 0$ and $I_c = \int_c P dx$
4. We can divide a path into sub paths. Such as $I_{AB} = I_{AK} + I_{KB}$

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[4. Lines|lines]].
[^2]: Read more about [[25. Integrations|integrals]].