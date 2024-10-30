---
tags:
  - university-notes
  - distance
  - quadratic-formula
  - circle
  - geometry
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Distance, Circle and Quadratic Equations

## Distance Formula

![[Pasted image 20240812144155.png]]

Notice how there is a `triangle`?  
We can find the distance between `A`and `B` by using `Pythagorus thoerem`.  

$$(hyp)^2 = (perp)^2 + (base)^2$$

$$hyp = \sqrt{(perp)^2 + (base)^2}$$

$$distance = \sqrt{(\Delta y)^2 + (\Delta x)^2}$$

$$distance = \sqrt{(y_2 - y_1)^2 + (x_2 - x_1)^2}$$

## Midpoint

The midpoint of $\overline{AB}$ is defined to be $average$ of the coordinate values relative to $axes$.  
![[Pasted image 20240812145906.png]]

## Circle

A `circle` is defined to be a `set`[^1] of points which are equidistant from a certain point called the `center` of the circle.  

$$circle := \{(x, y): r = \sqrt{x^2 + y^2}; r \in \mathbb{R^+}\}$$

![[Pasted image 20240812154939.png]]

### General Form

$$ax^2 + by^2 + dx + ey + f = 0$$

#### Example

Find `radius` and `center` of the circle $x^2 + y^2 - 8x + 2y + 8 = 0$ 

$$x^2 + y^2 - 8x + 2y + 8 = 0$$

$$(x^2 - 8x) + (y^2 + 2y) = -8$$

$$(x^2 - 8x + 16) + (y^2 + 2y + 1) = -8 + 16 + 1$$

$$(x - 4)^2 + (y + 1)^2 = 9$$

$$(x - 4)^2 + (y - (-1))^2 = 3^2$$

$$\because d^2 = r^2 = (x - x_0)^2 + (y - y_0)^2$$

Where $P(x, y)$ will be any arbitrary point and $P_0(x_0, y_0)$ is the `center`.  
So the `radius` is `3` and the center is `(4, -1)`

## Parabola

![[Pasted image 20240812165943.png]]

This `parabola` can be represented by equation:  

$$y = (x - 2) \cdot (x - 5)$$

Notice how $y$ becomes `0` if either of the terms become `0` and for that, we need `x` to be equal to either `2` or `5`.  
Let us try to simplify it  

$$y = x \cdot (x - 5) - 2 \cdot (x - 5)$$

$$y = x^2 - 5x - 2x + 2 \cdot 5$$

$$y = x^2 - x(5 + 2) + 2 \cdot 5$$

$$y = x^2 - Sx + P$$

Where `S` is `sum of the roots` and `P` is `product of the roots`.

### General Equation

$$y = ax^2 + bx + c$$

Notice the resemblance?  
For the `roots`, equation takes form of  

$$0 = x^2 + \frac{b}{a} \cdot x + \frac{c}{a}$$

Where $-\frac{b}{a} = sum$ and $\frac{c}{a} = product$

#### Vertex

The `tip` of the `parabola` is called its `vertex` and it exists in middle of the `roots`  

$$middle = \frac{sum}{2}$$

The `x-coordinate` will be  

$$x = - \frac{b}{2a}$$

And we can get the `y-coordinate` just by putting this in $y = f(x)$

## Reference

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[Mathematics/Set/Content|sets]].