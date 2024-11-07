---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-07
---

<span style="color: gray;">Dated: 07-11-2024</span>

# Asymptotic Notation

Given a `function`[^1] $g(n)$, we define $\Theta(g(n))$ to be a `set`[^2] of `functions`[^1] which are asymptotic equivalent to $g(n)$.  

$$\Theta(g(n)) = \{f(n) | \exists c_1, c_2, n_0 \in \mathbb{R}^+ \text{ such that } 0 \le c_1g(n) \le f(n) \le c_2g(n) \text{ for all } n \ge n_0\}$$

This can be written as  

$$f(n) \in \Theta(g(n))$$

Here $f(n)$ and $g(n)$ are both asymptotically equivalent.  
This means that they have same `growth rate` for larger values of $n$.  
All the following `functions`[^1] are asymptotically equivalent

- $$4n^2$$

- $$8n^2 + 2n - 3$$

- $$\frac {n^2} 5 + \sqrt n - 10 \log n$$

- $$n(n - 3)$$

## Lower Boundary

$f(n) = 8n^2 + 2n - 3$ grows asymptotically at least as fast as $n^2$.  

$$f(n) \ge c_1n^2 \text{ for all } n \ge n_0$$

$$f(n)=8n^{2}+2n-3\ge8n^{2}-3$$

$$\because 8n^{2}-3=7n^{2}+(n^{2}-3)$$

$$\because 7n^{2}+(n^{2}-3) \ge 7n^2$$

$$\therefore f(n)=8n^{2}+2n-3\ge8n^{2}-3 \ge 7n^2$$

Thus $c_1 = 7$  
We implicitly assumed that $2n \ge 0$ and $n^2 - 3 \ge 0$.  
These are not true for all $n$ but is for $n \ge \sqrt 3$.  
Therefore, $n_0 = \sqrt 3$.  
Hence,

$$f(n) \ge c_1n^2 \text{ for all } n \ge n_0$$

In our example, $c_1 = 7$ and $n_0 = \sqrt 3$.

## Upper Boundary

$f(n) = 8n^2 + 2n - 3$ grows no faster asymptotically than $n^2$.  

$$f(n) \le c_2n^2 \text{ for all } n \ge n_0$$

$$f(n) = 8n^2 +2n - 3 \le 8n^2 + 2n \le 8n^2 + 2n^2 = 10n^2$$

Thus, $c_2 = 10$  
We have made the assumption $2n \le 2n^2$ which is not true for all $n$ but is true for $n \ge 1$.  
Therefore $n_0 = 1$  
Hence,

$$f(n) \le c_2n^2 \text{ for all } n \ge n_0$$

![[Pasted image 20241107183020.png]]  
/// caption  
Asymptotic Notation Example  
///

We have established that $f(n) \in n^2$.  

We need to remember that $f(n)$ cannot belong to different classes though.

### Class $n$

Let us show  

$$f(n) \notin \Theta(n)$$

For this, we would have to satisfy both boundaries.  
The lower one is satisfied that $f(n) = 8n^2 + 2n - 3$ grows at least as fast asymptotically as $n$.  
But the upper bound is false.  

$$f(n) \le c_2n \text{ for all } n \ge n_0$$

$f(n)$ will exceed $n$ no matter how large $c_2$ is.

#### Proof by Contradiction

Let us assume the following statement _is_ true.  

$$f(n) \le c_2n \text{ for all } n \ge n_0$$

Since it is true for all large values of $n$ so we should have no problem as $n \to \infty$.  
Dividing both sides by $n$, we get  

$$\lim_{n\to\infty}\left(8n+2-\frac{3}{n}\right)\le c_{2}$$

It is clear that the left side approaches to $\infty$, hence the assumption is false.  
Therefore,  

$$f(n) \notin \Theta(n)$$

### Class $n^3$

In this case, the lower bound is violated

$$f(n) \ge c_1n^3 \text{ for all } n \ge n_0$$

#### Proof by Contradiction

Dividing both sides by $n^3$  

$$\lim_{n\to\infty}\left(\frac{8}{n}+\frac{2}{n^{2}}-\frac{3}{n^{3}}\right)\ge c_{1}$$

This is clear that the left side approaches to 0, hence contradicting the assumption to be true.  
Only way it remains true is if $c_1 = 0$.

## The $\Omega$ and $O$ Notations

Since $\Theta()$ relies on both, upper and lower bounds, we can divide it into following

### $O$ Notation

It is used to state only the asymptotic upper bound.  

$$O(g(n)) = \{f(n) | \exists c, n_0 \in \mathbb{R}^+ \text{ such that } 0 \le f(n) \le cg(n) \text{ for all } n \ge n_0\}$$

### $\Omega$ Notation

It is used to state only the asymptotic lower bound.  

$$\Omega(g(n)) = \{f(n) | \exists c, n_0 \in \mathbb{R}^+ \text{ such that } 0 \le cg(n) \le f(n) \text{ for all } n \ge n_0\}$$

## Using Limits to Define Asymptotic Behavior

### $\Theta$ Notation

$$\lim_{n\to\infty}\frac{f(n)}{g(n)}=c$$

### $O$ Notation

$$\lim_{n\to\infty}\frac{f(n)}{g(n)}=c$$

### $\Omega$ Notation

$$\lim_{n\to\infty}\frac{f(n)}{g(n)}\ne c$$

## List of Common Asymptotic Running times

### $\Theta(1)$

Constant time, cannot beat it.

### $\Theta(\log n)$

- Inserting into `binary tree`.
- Time to find an item in a sorted `array` of length $n$ using `binary search`.

### $\Theta(n)$

About the fastest that an algorithm can run.

### $\Theta(n \log n)$

Best sorting algorithms.

### $\Theta(n^2)$, $\Theta(n^3)$

- Polynomial time.
- Acceptable when $n \le 1000$.

### $\Theta(2^n)$, $\Theta(3^n)$

- Exponential time.
- Acceptable when $n \le 50$.

### $\Theta(n!)$, $\Theta(n^n)$

- Acceptable when $n \le 20$.

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[notes_publisher/docs/Mathematics/Function/Content|functions]].
[^2]: Read more about [[notes_publisher/docs/Mathematics/Set/Content|sets]].