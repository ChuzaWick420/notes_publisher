---
tags:
  - university-notes
  - differentiation
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Applications of Differentiation

## Related Rates

We come across a lot of problems in world related to _related rates_.  
We want to know how one _quantity_ changes with respect to another _quantity_.

### Example

Imagine a `5 ft` ladder leaning against a wall, with a base of `4 ft`, sliding off at `2 ft / sec` speed.  
We are interested to know at which speed, the top of the ladder is falling down at that instant.  
![[Pasted image 20240906152849.png]]

#### Solution

Let us first assign some variables.  
Let us say, $h = 5$ (`hypotenus`), $x$ being the `base` and $y$ being the `height`.  
We know that ladder, being a concrete object, will not change its `length` as it falls down.  
Therefore, we can create a `function`[^1] using the `Pythagorus Theorem` as such:  

$$y^2 + x^2 = 5^2$$

Before touching this equation, let us look at more data.  
We know that the `base` of the ladder at the captured instant is moving at the rate of `2 ft / sec`.  
Since `displacement` or increase in `base` is a `function`[^1] of `time`, we can write the rate of change as such:

$$\frac{dx}{dt} = \frac{2 sec}{ft}$$

And we are asked to find same but for the vertical direction, which would be:  

$$\frac{dy}{dt}$$

Using the `implicit differentiation`[^2] with respect to `t` on the original equation,  

$$2x\frac{dx}{dt}+2y\frac{dy}{dt}=0$$

After simplification, we get  

$$\frac{dy}{dt}=-\frac{x}{y}\frac{dx}{dt}$$

We already know that `x = 4`, to know the value of `y` at that instance, we use our equation which we discussed in the beginning.  

$$y^2 + x^2 = 5^2$$

$$y = \sqrt{25 - 16}$$

$$y = \sqrt{9}$$

$$y = 9$$

Now, we can plug these value inside our equation which we got by differentiation.  

$$\frac{dy}{dt}|_{x=4}=-\frac{4}{3}(2)$$

$$= - \frac{8 ft}{3 sec}$$

## Increasing Functions

In the context of talking over a specific `interval`,[^3] a `function`[^1] is called `increasing` if its `y` value _increases_ as `x` value increases over that `interval`.[^3]

## Decreasing Functions

Similarly, a `function`[^1] is called `decreasing` if its `y` value _decreases_ as the `x` value increases over the `interval`.[^3]

## Constant Functions

If the `y` value of a `function`[^1] remains the same over the `interval`[^3] then it is called `constant function`.

![[Pasted image 20240906163602.png]]

## Theorems

1. if $f^{\prime}(x) > 0$ for all values of $x$ in $(a, b)$ then $f(x)$ is an `increaing function`.
2. if $f^{\prime}(x) < 0$ for all values of $x$ in $(a, b)$ then $f(x)$ is an `decreasing function`.
3. if $f^{\prime}(x) = 0$ for all values of $x$ in $(a, b)$ then $f(x)$ is an `constant function`.

### Example

Find the `intervals`[^3] where the graph of $f(x) = x^2 - 4x + 3$ is _increasing_ and _decreasing_.

#### Solution

First, we `differentiate`[^4] the `function`.[^1]  

$$f^{\prime}(x) = 2x - 2 = 2(x - 2)$$

##### Decreasing Interval

$$f'(x) < 0 \Rightarrow 2(x-2) < 0 \Rightarrow -\infty < x < 2$$

$$(-\infty, 2]$$

##### Increasing Interval

$$f'(x) > 0 \Rightarrow 2(x-2) > 0 \Rightarrow 2 < x < +\infty$$

$$[2, \infty)$$

## Concavity of Functions

Let $f(x)$ be `differentiable` on an `interval`[^3] then.

1. $f(x)$ is _concave up_ if it is _increasing_ on the `interval`[^3]
2. $f(x)$ is _concave down_ if it is _decreasing_ on the `interval`[^3]

### Theorems

1. If $f^{\prime \prime}(x) > 0$ on an `open interval`[^3] $(a, b)$ then $f(x)$ is _concave up_ on that `interval`.[^3]
2. If $f^{\prime \prime}(x) < 0$ on an `open interval`[^3] $(a, b)$ then $f(x)$ is _concave down_ on that `interval`.[^3]

#### Example

$$f(x) = x^2 - 4x + 4$$

$$f^{\prime}(x) = 2x - 4$$

$$f^{\prime \prime}(x) = 2$$

Since $f^{\prime \prime}(x) > 0$ for all $x$, the graph is _concave up_ at interval $(-\infty, +\infty)$.

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[Mathematics/Function/Content|functions]].
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/19. Implicit Differentiation/Lecture|implicit differentiation]].
[^3]: Read more about [[1. Coordinates, Graphs, Lines|intervals]].
[^4]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/15. The Derivative/Lecture|differentiation]].