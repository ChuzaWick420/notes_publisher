---
tags:
  - university-notes
  - sequences
  - "limits"
university-name: Virtual University of Pakistan
---

# Sequences and Monotone Sequences
## Definition of a Sequence
A `sequence` is a succession of `numbers`.

### Example

$$1, 2, 3, \ldots$$

Each `number` is called `term` of the `sequence`.  
Each `term` has a _positional_ name as well such as `1st term`, `2nd term` etc.  
We write them as  

$$a_1, a_2, \ldots$$

### Example

Let us say we have a `sequence` $$2, 4, 6, \ldots$$

Then we can also write it as  

$$\{2^n\}^{+\infty}_{n = 1}$$

### Generalized
Therefore, we can write a `sequence` of the form $a_1, a_2, \ldots$ as  

$$\{a_n\}^{+\infty}_{n = 1}$$

## Formal Definition
A `sequence` or a `infinite sequence` is a `function`[^1] whose domain is a `set`[^2] of `positive integers` ($\mathbb{Z^+}$).  
We have 2 notations for this

- $$\{a_n\}_{n = 1}^{+\infty}$$

- $$f(n) = a_n; n \in \mathbb{Z^+}$$

## Graphs of Sequences
Imagine we have $f(x) = x^2$  
Then if the `domain`[^1] is $x \in \{\mathbb{R^+} + \{0\}\}$ then the graph would look something like  
![[Pasted image 20240930165630.png]]  
But if the `domain` is $x \in \{\mathbb{Z}^+ + \{0\}\}$ then graph would be  
![[Pasted image 20240930165957.png]]

> These graphs only are captured inside the `interval`[^3] $[0, 2]$

## `Limits`[^4] For Sequence
A `sequence` $\{a_n\}$ is said to _converge_ to the `limit`[^4] $L$ if given any $\epsilon > 0$ there is $N$ such that $\lvert a_n - L\rvert < \epsilon$ for $n \ge N$.  
In this case we write  

$$\lim_{n \to + \infty} a_n = L$$

A `sequence` which does not _converge_ is said to _diverge_.

### Geometric Intuition
![[Pasted image 20240930171329.png]]  
After $n > 5$, our values start to approach $L$.

### Theorems

- $$\lim_{n \to +\infty} c = c$$

- $$\lim_{n \to +\infty}c a_n = c \lim_{n \to +\infty} a_n= c L_1$$

- $$\lim_{n \to +\infty} (a_n + b_n) = \lim_{n \to + \infty} a_n + \lim_{n \to +\infty} b_n = L_1 + L_2$$

- $$\lim_{n \to +\infty} (a_n - b_n) = \lim_{n \to + \infty} a_n - \lim_{n \to +\infty} b_n = L_1 - L_2$$

- $$\lim_{n \to +\infty} (a_n \cdot b_n) = \lim_{n \to + \infty} a_n \cdot \lim_{n \to +\infty} b_n = L_1 \cdot L_2$$

- $$\lim_{n \to +\infty}\left(\frac{a_n}{b_n}\right) = \frac{\lim_{n \to +\infty} a_n}{\lim_{n \to +\infty} b_n} = \frac{L_1}{L_2}$$

### Example
Determine if the following `sequence` _converges_ or _diverges_.  

$$\left\{\frac{n}{2n+1}\right\}_{n=1}^{+\infty}$$

#### Solution
Divide the `numerator` and `denominator` by $n$.  

$$\lim_{n\rightarrow+\infty}\frac{n}{2n+1} = \lim_{n\rightarrow+\infty}\frac{1}{2+1/n} $$

$$= \frac{\lim_{n\rightarrow+\infty}1}{\lim_{n\rightarrow+\infty}(2+1/n)} = \frac{1}{2}$$

## Recursive Sequence
There are some `sequences` which are defined by providing an _initial_ value and by giving a formula which relates each subsequent `term` to the `term` that precedes it.  
These `sequences` are called `recursive sequences`.

### Example
For $n \ge 1$  

$$a_{n+1} = \frac 1 2 \left(a_n + \frac {3}{a_n}\right)$$

## Monotonicity
A `sequence` $\{a_n\}$ is called 

### Increasing

If $$a_1 < a_2 < \ldots < a_n < \ldots$$

#### Difference of `terms`

$$a_{n + 1} - a_n > 0$$

#### Ratio of `terms`

$$\frac{a_{n + 1}}{a_n} > 1$$

#### Derivative of $f(x) = a_n$

$$f^{\prime}(x) > 0$$

### Decreasing

If $$a_1 > a_2 > \ldots > a_n > \ldots$$

#### Difference of `terms`

$$a_{n + 1} - a_n < 0$$

#### Ratio of `terms`

$$\frac{a_{n + 1}}{a_n} < 1$$

#### Derivative of $f(x) = a_n$

$$f^{\prime}(x) < 0$$

### Non Increasing

If $$a_1 \ge a_2 \ge \ldots \ge a_n \ge \ldots$$

#### Difference of `terms`

$$a_{n + 1} - a_n \le 0$$

#### Ratio of `terms`

$$\frac{a_{n + 1}}{a_n} \le 1$$

#### Derivative of $f(x) = a_n$

$$f^{\prime}(x) \le 0$$

### Non Decreasing

If $$a_1 \le a_2 \le \ldots \le a_n \le \ldots$$

#### Difference of `terms`

$$a_{n + 1} - a_n \ge 0$$

#### Ratio of `terms`

$$\frac{a_{n + 1}}{a_n} \ge 1$$

#### Derivative of $f(x) = a_n$

$$f^{\prime}(x) \ge 0$$

A `sequence` that is either `non decreasing` or `non increasing` is called a `monotone`.  
A `sequence` that is either `decreasing` or `increasing` is called a `strictly monotone`.

### Example
Prove that the `sequence`  

$$\frac 1 2, \frac 2 3, \ldots , \frac{n}{n+1}, \ldots$$

is an `increasing sequence`.

#### Solution

$$a_n = \frac{n}{n+1}$$

$$a_{n + 1} = \frac{n + 1}{n+2}$$

Now from here, we can take either the `difference` route or `ratio` route.

##### Difference

$$a_{n+1} - a_n = \frac{n+1}{n+2} - \frac{n}{n+1}$$

$$= \frac{n^2 + 2n + 1 - n^2 - 2n}{(n+1)(n+2)}$$

$$= \frac{1}{(n+1)(n+2)} > 0$$

##### Ratio

$$\frac{a_{n+1}}{a_n} = \frac{(n+1)/(n+2)}{n/(n+1)}$$

$$= \frac{n+1}{n+2} \cdot \frac{n+1}{n} $$

$$= \frac{n^2 + 2n + 1}{n^2 + 2n} > 1$$

### Eventually Monotonic
A `sequence` is called `eventually monotonic` for some $n = N$, the `sequence` becomes a `monotone`.

## Theorems
## Non Decreasing
1. There is a `constant` $M$ such that $a_n \le M$ for all $n$ then the `sequence` _converges_ to a `limit`[^4] satisfying $L \le M$.

2. There is no upper bound in case of  

$$\lim_{n \to +\infty}a_n = +\infty$$

## Non Increasing
1. There is a `constant` $M$ such that $a_n \ge M$ for all $n$ then the `sequence` _converges_ to a `limit`[^4] satisfying $L \ge M$.

2. There is no lower bound in case of  

$$\lim_{n \to +\infty}a_n = -\infty$$

## References

[^1]: Read more about [[Mathematics/Function/Content|functions]].
[^2]: Read more about [[Mathematics/Set/Content|sets]].
[^3]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/1. Coordinates, Graphs, Lines/Lecture|interval]].
[^4]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/9. Limits (Intuitive Introduction)/Lecture|limits]].
