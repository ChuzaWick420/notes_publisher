---
tags:
  - university-notes
  - integral
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Volume by Slicing, Disks and Washers

## Cylinders

![[Pasted image 20240927211619.png]]  
Imagine we have a `circle` in `2D` (the $xy$ `plane`[^1]).  
In `3d`, it would look something like this  
![[Pasted image 20240927212132.png]]  
And if we start scaling it into the $3rd$ axis which is $z$, we will get a `cylinder`.  
![[Pasted image 20240927212453.png]]

If the `circle` had a hole inside it, the `cylinder` would have it too.  
To find the volume of this `cylinder`, we can use the formula  

$$V = A \cdot h$$

Where $A$ is the `area` of the `circle` and $h$ is the unit `height` in `z axis`.

> This formula can work for any shape which is extended in `z axis` in similar fashion.

## Slicing Method

![[Pasted image 20240927214122.png]]  
We can bound this shape on `x axis` by $x = a$ and $x = b$.  
![[Pasted image 20240927213741.png]]  
Notice how the `cross sectional area` is uniform across the shape if we look at the `surface` perpendicular to the `x - axis`.  
![[Pasted image 20240927214328.png]]

Therefore, we can define its `volume` to be a `sum` of the `areas` of these `surfaces` which come up as a result of slicing the shape into $n$ chunks.  

$$V \approx \sum_{i = 1}^{n} A(x_i) \Delta x_i$$

To get more accuracy, we can make the slices as thin as possible.

$$V = \lim_{max(\Delta x_i \to 0)}\sum_{i = 1}^{n} A(x_i) \Delta x_i = \int_a^b A(x) dx$$

### Definition

Let $S$ be a solid bounded by two `parallel planes`[^1] perpendicular to the `x-axis` at $x = a$ and $x = b$. If , for each $x$ in $[a,b]$, the `cross-sectional area` of $S$ perpendicular to the `x-axis` is $A(x)$, then the `volume` of the solid is

$$V =  \int_a^b A(x) dx$$

This definition also works if we replace `x axis` with `y axis`.

## Volumes of Solids of Revolution by Disks Perpendicular to `x axis`

Imagine we have a `continuous function`[^2] defined over the `interval`[^3] $[a, b]$  
![[Pasted image 20240927215552.png]]

After the rotation, we get a solid which looks like this  
![[Pasted image 20240927215700.png]]  
Notice how if we look perpendicular to the `x axis`, we would find the `cross sections` to be `circles`.  
Therefore,  

$$V = \int_a^b A(x) dx = \int_a^b \pi \left(f(x)\right)^2 dx$$

$$\because A = \pi \cdot r^2$$

### Example

Find formula for `volume` of a `sphere`.

#### Solution

We can get a `sphere` by revolving a `semi circle` around the `x axis`.  
![[Pasted image 20240927220336.png]]  
First, let's figure out equation for this `semi circle`.  
We know that a `circle` consists of 2 `semi circles` which reflect each other across the `x-axis`.  
If $r$ is the `radius` of the `circle` then.  

$$x^2 + y^2 = r^2$$

$$y^2 = r^2 - x^2$$

$$f(x) = y = \pm \sqrt{r^2 - x^2}$$

This gives us equations for both `semi circles` but we care about only one.  

$$f(x) = \sqrt{r^2 - x^2}$$

The `interval`[^3] is $[-r, r]$ and therefore,  

$$A(x) = \pi \cdot \left(\sqrt{r^2 - x^2}\right)^2$$

$$V = \int_{-r}^{r} \pi \cdot (r^2 - x^2) dx = \frac 4 3 \pi r^3$$

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/3. Coordinate Planes and Graphs/Lecture|plane]].
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/12. Continuity/Lecture|continuity]].
[^3]: Read more about [[1. Coordinates, Graphs, Lines|intervals]].