---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Theorems
## The First Shift Theorem
If $\mathscr L (F(t)) = f(s)$ then $\mathscr L (e^{-at} F(t)) = f(s + a)$.

### Example

$$\mathscr L (t^2) = \frac 2 {s^3}$$

$$\mathscr L (t^2 e^{4t}) = \frac 2 {(s - 4)^3}$$

Here $a = -4$.

## Multiplying by $t$
If $\mathscr L (F(t)) = f(s)$ then  

$$\mathscr L (F(t)) = - \frac d {ds} (f(s))$$

### Example

$$\mathscr L (\sin 2t) = \frac 2 {s^2 + 4}$$

$$\mathscr L (t \sin 2t) = -\frac d {ds} \left(\frac 2 {s^2 + 4}\right) = \frac {4s} {(s^2 + 4)^2}$$

This theorem can be extended to following  

$$\mathscr{L}(t^{n}F(t))=(-1)^{n}\frac{d^{n}}{ds^{n}}(f(s))$$

## Dividing by $t$
If $\mathscr L (F(t)) = f(s)$ then  

$$\mathscr L \left(\frac {F(t)} t\right) = \int_s^\infty f(s) ds$$

### Example
Determine  

$$\mathscr L \left(\frac{\sin (at)}{t}\right) = \frac a {s^2 + a^2}$$

$$\mathscr{L}\left(\frac{\sin(at)}{t}\right)$$

$$=\int_{s}^{\infty}\frac{a}{s^{2}+a^{2}}ds$$

$$=\left[\tan^{-1}\left(\frac{s}{a}\right)\right]_{s}^{\infty}$$

$$=\frac{\pi}{2}-\tan^{-1}\left(\frac{s}{a}\right)$$

$$=\tan^{-1}\left(\frac{a}{s}\right)$$

## Inverse Transforms

$$\mathscr L (4) = \frac 4 s$$

$$\implies \mathscr L ^{-1} \left(\frac 4 s\right) = 4$$

But what about  

$$\mathscr L ^{-1}\left(\frac{3s}{s^2 - s - 6}\right) = \mathscr L ^ {-1}\left(\frac{1}{s+2} + \frac{1}{s - 3}\right)$$

$$= \mathscr L ^ {-1}\left(\frac{1}{s + 2}\right) + \mathscr L ^ {-1}\left(\frac{1}{s - 3}\right)$$

$$= e^{-2t} + 2 e^{3t}$$

## Rules of Partial Fractions
1. The degree of `numerator` should be lower than degree of `denominator`.
2. Factorize the `denominator` into its `prime factors`. This determines the shapes of the `partial fraction`.
3. A `linear` factor $(s + a)$ gives a `partial fraction` $\frac A {s + a}$.
4. A repeated factor $(s + a)^2$ gives a `partial fraction` $\frac A {s + a} + \frac B {(s + a)^2}$.
5. Similarly, $(s + a)^3$ gives a `partial fraction` $\frac A {s + a} + \frac B {(s + a)^2} + \frac C {(s + a)^3}$.
6. A `quadratic` factor $(s^2 + ps + q)$ gives $\frac{Ps + Q}{s^2 + ps + q}$.
7. Similarly, $(s^2 + ps + q)^2$ gives $\frac{Ps + Q}{s^2 + ps + q} + \frac{Rs + T}{(s^2 + ps + q)^2}$.
8. $\frac{s + a}{(s + b) (s + c)}$ has gives $\frac{A}{s + b} + \frac{B}{s + c}$.
9. $\frac{s + a}{(s + b) (s + c)^2}$ has gives $\frac{A}{s + b} + \frac{B}{s + c} + \frac{C}{(s + c)^2}$.

## Example
Solve the following equation given that $x(0) = 5$ and $\frac{dx}{dt}\bigg|_{t = 0} = 7$  

$$\frac{d^2x}{dt^2} - 3 \frac{dx}{dt} + 2x = 2e^{3t}$$

$$x^{\prime \prime}(t) - 3x^\prime(t) + 2x(t) = 2e^{3t}$$

Taking the `laplace transform`[^1] on both sides

$$\mathscr L (x^{\prime \prime}(t) - 3x^\prime(t) + 2x(t)) = \mathscr L (2e^{3t})$$

$$\mathscr {L}(x^{\prime\prime}(t))-3\mathscr{L}(x^{\prime}(t))+2\mathscr{L}(x(t))=2\mathscr{L}(e^{3t})$$

$$s^2\mathscr L (x(t)) - sx(0) - x^\prime(0) - 3\left(s \mathscr L (x(t)) - x(0)\right) + 2 \mathscr L (x(t)) = \frac 2 {(s - 3)}$$

Plugging the values in, we get  

$$s^2 \mathscr L (x(t)) - s(7) - 7 - 3 \left(s \mathscr L (x(t)) + 3 (5)\right) + 2 \mathscr L (x(t)) = \frac 2 {s - 3}$$

$$s^{2}\mathscr{L}(x(t))-3s\mathscr{L}(x(t))+2\mathscr{L}(x(t))=\frac{2}{s-3}-8+5s$$

$$(s^{2}-3s+2)\mathscr{L}(x(t))=\frac{2-8s+24+5s^{2}-15s}{s-3}$$

$$\mathscr{L}(x(t))=\frac{5s^{2}-23s+24}{(s-1)(s-2)(s-3)}$$

After solving the `partial fraction`, the coefficients we get are $A = 3$, $B = 2$ and $C = 0$  

$$\mathscr{L}(x(t))=\frac{3}{s-1}+\frac{2}{s-2}+\frac{0}{s-3}$$

$$\mathscr{L}(x(t))=\frac{3}{s-1}+\frac{2}{s-2}$$

$$x(t)=\mathscr{L}^{-1}\left(\frac{3}{s-1}\right)+\mathscr{L}^{-1}\left(\frac{2}{s-2}\right)=3e^{t}+2e^{2t}$$

## References
Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 2/MTH301 - Calculus II/44. Laplace Transforms/Lecture|laplace transform]].
