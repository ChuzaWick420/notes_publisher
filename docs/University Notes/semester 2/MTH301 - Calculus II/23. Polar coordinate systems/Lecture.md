---
tags:
  - university-notes
  - distance
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Polar Coordinate Systems

To form a `polar coordinate system`, we take a fixed point $O$ called `origin` or `pole`.  
Then we construct a `ray` in right direction from it called a `polar axis`.  
After selecting a `unit` for measurement, we may associate any point $P$ in the `plane`[^1] with the pair $(r, \theta)$.  
Here $r$ is the `radial distance` from $O$ to $P$ and $\theta$ is the `angle` between `polar axis` and the `line`[^2] $\overline{OP}$ called `polar angle`.  
![[Pasted image 20241013232007.png]]

## Uniqueness

The `polar coordinates` of a point are _not_ the same.  
A point may be represented as following  

$$(5, 45 \degree)$$

$$(5, 405 \degree)$$

$$(5, -335 \degree)$$

They all represent the same point.  

$$(r, \theta + 360 \degree \cdot n) \text{ where } n \in \mathbb{Z}$$

## Negative Values for $r$

Although `distance` being negative does not make sense but we can have negative values for $r$.  
Here is an example  
![[Pasted image 20241013234035.png]]  
It just means that if we look at $r$ as a `vector`[^3] $\vec{r}$, we are just flipping the signs of its components.

## Relation between Polar and Cartesian Coordinate System

![[Pasted image 20241013235249.png]]  

$$x = r \cdot \cos(\theta)$$

$$y = r \cdot \sin(\theta)$$

$$\tan (\theta) = \frac y x$$

## `Lines`[^4] In Polar Coordinate System

### Horizontal line

$$\because y = a \text{ and } y = r \cdot \sin(\theta)$$

$$r \cdot \sin(\theta) = a$$

### Vertical line

$$\because x = b \text{ and } x = r \cdot \cos(\theta)$$

$$r \cdot \cos(\theta) = b$$

### Along $\overline{OP}$

$$\theta = \theta_{\circ}$$

## General Equation

The general equation for the `line`[^4]  

$$Ax + By + C = 0$$

will take the form  

$$A(r \cdot \cos(\theta)) + B(r \cdot \sin(\theta)) + C = 0$$

$$r \left(A \cdot \cos(\theta) + B \cdot \sin(\theta)\right) + C = 0$$

## Circle in Polar Coordinates

We know that the equation for a `circle` centered at $(x_0, y_0)$ with `radius` $a$ is

$$a^2 = (x - x_0)^2 + (y - y_0)^2$$

Converting $x$ and $y$ into their polar forms, we get  

$$a^2 = (r \cdot \cos(\theta) - r_{\circ} \cdot \cos(\theta_{\circ}))^2 + (r \cdot \sin(\theta) - r_{\circ} \cdot \sin(\theta_{\circ}))^2$$

Expand this and we will get  

$$r^2 - 2 r \cdot r_{\circ} \cdot \cos(\theta - \theta_{\circ}) + r_{\circ}^2 = a^2$$

## Special Cases for `Circle`

If the `circle` is centered at the `origin` then the equations becomes  

$$r^2 = a^2 \implies r = a$$

However, the `circles` with polar coordinates $(a, \frac \pi 2)$ and $(a, - \frac \pi 2)$ are  
![[Pasted image 20241014121834.png]]

In these cases, the equations become  

$$r = 2 a \sin(\theta)$$

$$r = -2 a \sin(\theta)$$

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/3. Coordinate Planes and Graphs/Lecture|planes]].
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/4. Lines/Lecture|line]].
[^3]: Read more about [[semester 2/MTH301 - Calculus II/10. Introduction to vectors/Lecture|vectors]].
[^4]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/4. Lines/Lecture|lines]].