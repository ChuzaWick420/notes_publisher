# Complex Numbers

Imagine a `conditional`.  

$$x^2 = -1$$

We cannot find a value for $x$ such that it satisfies this `conditional`.  
This is where `complex numbers` come into play.  

## Complex Planes

`Complex numbers` do not follow order axioms and can be retreated as 2D points on a `plane` called the `complex plane`, `Z plane` or `argand diagram`.  
This `plane` is a result of extending the `number line`[^1] into 2 dimensions.  
![[m_complex_plane_1.svg]]

## Representing `Complex numbers` on Complex Plane

The `complex numbers` has 2 parts, each corresponding to each axis.  
There's the `real` and then there is the `imaginary` part.  
The $\iota$ is used to represent `imaginary` parts.  
$\iota$ is defined to be  

$$\iota^2 = -1 \implies \iota = \sqrt{-1}$$

We can represent them in 2 ways.

### Similarities with Vectors

A `complex number` $z$ may be written as  

$$z = a(1) + b\iota = a + b \iota$$

Here $a$ is the `real` and $b$ is the `imaginary` part.

![[m_complex_plane_2.svg]]  
The $1$ acts like the `unit vector`[^2] $\hat i$ for $x$ axis and $\iota$ acts like the `unit vector`[^2] $\hat j$ for $y$ axis.  
This makes a `complex number` behave like a `position vector`[^2] for a point (the `complex number` itself).

### Ordered Pair

We can use ordered pair to represent the `complex numbers` as points.  

$$(a, b)$$

Here $a$ is the `real` and $b$ is the `imaginary` part.

## Operations

Imagine 2 `complex numbers`.  

$$z_1 = a_1 + b_1\iota$$

$$z_2 = a_2 + b_2\iota$$

### Addition

$$z_1 + z_2 = a_1 + b_1 \iota + a_2 + b_2 \iota$$

$$= (a_1 + a_2) + (b_1 + b_2)\iota$$

### Subtraction

$$z_1 - z_2 = (a_1 + b_1 \iota) - (a_2 + b_2 \iota)$$

$$= a_1 + b_1 \iota - a_2 - b_2 \iota$$

$$= (a_1 - a_2) + (b_1 - b_2) \iota$$

### Multiplication

$$z_1 \times z_2 = (a_1 + b_1 \iota) \times (a_2 + b_2 \iota)$$

$$= a_1(a_2 + b_2 \iota) + b_1\iota(a_2 + b_2\iota)$$

$$= a_1a_2 + a_1b_2\iota + a_2b_1\iota + b_1b_2\iota^2$$

$$= a_1a_2 + b_1b_2(-1) + (a_1b_2 + a_2b_1)\iota \quad \because \iota^2 = -1$$

$$= (a_1a_2 - b_1b_2) + (a_1b_2 + a_2b_1) \iota$$

### Division

$$\frac {z_1}{z_2} = \frac {a_1 + b_1\iota}{a_2 + b_2 \iota}$$

$$= \frac {a_1 + b_1\iota}{a_2 + b_2 \iota} \times \frac {a_2 - b_2\iota}{a_2 - b_2 \iota}$$

$$= \frac{(a_1 + b_1 \iota) \times (a_2 - b_2 \iota)}{(a_2)^2 - (b_2 \iota)^2}$$

$$= \frac{(a_1a_2 + b_1b_2) + (a_1b_1 - a_1b_2) \iota}{a_2^2 + b^2_2}$$

## Properties

### Additive Identity

$$(0, 0)$$

### Additive Inverse

$$(-a, -b)$$

### Multiplicative Identity

$$(1, 0)$$

### Multiplicative Inverse

$$\left(\frac{a}{a^2 + b^2}, \frac{-b}{a^2 + b^2}\right)$$

## References

[^1]: Read more about [[M_Real_Line|number line]].
[^2]: Read more about [[mth301_10|vectors]].