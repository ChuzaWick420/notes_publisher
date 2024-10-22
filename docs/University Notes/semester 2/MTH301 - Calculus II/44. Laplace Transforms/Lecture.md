---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Laplace Transform

$$\mathscr L (e^{3t}) = \frac {1} {s - 3}$$

$$\implies \mathscr L^{-1} \left(\frac 1 {s - 3}\right) = e^{3t}$$

$$\mathscr L (t^3) = \frac{3!}{s^4}$$

$$\implies \mathscr L^{-1} \left(\frac{3!}{s^4}\right) = t^3$$

## Definition
The `laplace transform` of a `function`[^1] $F(t)$ denotes as $\mathscr L (F(t))$ is defined as  

$$\mathscr L (F(t)) = \int_0^\infty e^{-st} F(t) dt$$

In all cases, the parameter $s$ is assumed to be positive and large enough to ensure that the product $F(t) \cdot e^{-st}$ converges to $0$ as $t \to \infty$

## Example

$$\mathscr L (a) = \int_0^\infty a e^{-st} dt$$

$$= a \int_0^\infty e^{-st} dt$$

$$=a\frac{e^{-st}}{-s}\bigg|_{0}^{\infty}=-\frac{a}{s}(0-1)=\frac{a}{s}$$

## Complex Numbers
A number of the following form is called a `complex number`.  

$$z = a + b\iota$$

where $a$ is the `real` part and $b$ is the `imaginary` part.

## Conjugate of Complex Numbers
If $z = a + b \iota$ is a [complex number](#complex-numbers) then its `conjugate` will be $\overline z = \overline{a + b \iota} = a - b \iota$ 

## Several Standard Results

- $$\mathscr L (a) = \frac a s$$

- $$\mathscr L (e^{at}) = \frac 1 {s - a}$$

- $$\mathscr L (t^n) = \frac{n!}{s^{n+1}}$$

- $$\mathscr L (\sin (at)) = \frac{a}{s^2 + a^2}$$

- $$\mathscr L (\sinh (at)) = \frac{a}{s^2 - a^2}$$

- $$\mathscr L (\cos (at)) = \frac{s}{s^2 + a^2}$$

- $$\mathscr L (\cosh (at)) = \frac{s}{s^2 - a^2}$$

## References
Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[Mathematics/Function/Content|functions]].
