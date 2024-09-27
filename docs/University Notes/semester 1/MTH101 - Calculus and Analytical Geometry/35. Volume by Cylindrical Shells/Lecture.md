---
tags:
  - university-notes
  - integral
university-name: Virtual University of Pakistan
---

# Volume of Cylindrical Shells
## Cylindrical Shells
![[Pasted image 20240927224304.png]]  
We get this when we extend a `washer`, a `disk` with a hole in it, _up_.  
Just like finding `areas` between 2 curves,  

$$V = (\pi r_2^2 - \pi r_1^2) \cdot h$$

Here $r_2$ is the `radius` of the outer `circle` and $r_1$ is the `radius` of the inner `circle`.  

$$V = \pi (r_2^2 - r_1^2) \cdot h$$

$$=\pi(r_2+r_1)(r_2-r_1)h$$

$$=2\pi\left(\frac{1}{2}(r_2+r_1)\right)h.(r_2-r_1)$$

The $r_2 - r_1$ factor determines the `thickness`.

Let us say there is a region $R$ bounded up by $f(x)$, left and right by $x = a$ and $x = b$ respectively and below by `x-axis`.  
![[Pasted image 20240927225433.png]]  
We can rotate this region $R$ around the `y axis`.  
Then we divide the `interval`[^1] into `subintervals` with points $x_1, x_2, \ldots$  
This will give us a collection of solids similar to `cylindrical shells` but the upper surface will be defined according to $f(x)$.  
![[Pasted image 20240927230317.png]]  
So the whole `volume` of the whole solid can be written as  

$$V(S) = V(S_1) + V(S_2) + \ldots + V(S_n) = \sum_{i = 1}^n S_i$$

Using the formula for `volume` of `cylindrical shells`, we can define volume of any arbitrary sub-solid as follows  

$$V(S_i) = 2\pi \cdot f(x_i^*) \cdot \Delta x_i \cdot x_i^*$$

Here the $x_i^*$ is the `average radius` which is good for approximation of `height` defined by $f(x_i^*)$, when the `thickness` is very small, that is $max(\Delta x_i) \to 0$  

$$V(S)=\lim_{\max(\Delta x_i)\to 0}\sum_{i=1}^{n}2\pi x_i^*f(x_i^*)\Delta x_i=\int_{a}^{b}2\pi xf(x)dx$$
  
![[Pasted image 20240927231333.png]]

## References

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/1. Coordinates, Graphs, Lines/Lecture|intervals]].
