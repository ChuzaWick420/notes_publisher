---
tags:
  - university-notes
  - geometry
  - calculus
  - distance
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Polar Coordinates

We were using $x$ and $y$ axes to find `position` of a point on a `plane`.[^1]  
Now we will use $r$ and $\theta$ instead where $r$ is the `distance` from the `origin`, also called `pole` and $\theta$ is the measure of `angle` relative to $x$ axis.

## Conversion from Cartesian to Polar Coordinates

Using the `Pythagorus theorem`.  

$$r^2 = x^2 + y^2$$

Using the `slope`,[^2] we have  

$$\tan (\theta) = \frac y x$$

## Regular Coordinates for 3D Points

These coordinates are called `rectangular` coordinate system.  
A point is represented as  

$$P(x, y, z)$$

<iframe src="../figures/rect_coords.html"></iframe>

## Cylindrical Coordinates for 3D Points

A point in this system is represented as  

$$P(r, \theta, z)$$

Here $r$ is the `distance` in $xy$ plane, $\theta$ is the $\alpha$ and $z$ is the `height` in the `cylinder`.  
![[Pasted image 20241005195736.png]]

## Spherical Coordinates for 3D Points

A point in this system is represented as  

$$P(p, \theta, \phi)$$

Where $p$ is the `distance` to the point from `origin`, $\theta$ is the $\alpha$ and $\phi$ is $\gamma$.

## Conversion between Cylindrical and Rectangular

### Cylindrical to Rectangular

$$(r, \theta, z) \rightarrow (x, y, z)$$

$$x = r \cdot \cos(\theta)$$

$$y = r \cdot \sin(\theta)$$

$$z = z$$

### Rectangular to Cylindrical

$$(x, y, z) \rightarrow (r, \theta, z)$$

$$r = \sqrt{x^2 + y^2}$$

$$\theta = \tan^{-1} \frac y x$$

$$z = z$$

## Conversion between Cylindrical and Spherical

### Cylindrical to Spherical

$$(r, \theta, z) \rightarrow (p, \theta, \phi)$$

$$p = \sqrt{r^2 + z^2}$$

$$\theta = \theta$$

$$\phi = \tan^{-1} \frac r z$$

### Spherical to Cylindrical

$$(p, \theta, \phi) \rightarrow (r, \theta, z)$$

$$r = p \cdot \sin(\phi)$$

$$\theta = \theta$$

$$z = p \cdot \cos (\phi)$$

## Conversion between Spherical and Rectangular

### Spherical to Rectangular

$$(p, \theta, \phi) \rightarrow (x, y, z)$$

$$\because r = p \cdot \sin(\phi)$$

$$\because x = r \cdot \cos (\theta)$$

$$x = p \cdot \sin(\phi) \cdot \cos(\theta)$$

$$\because y = r \cdot \sin(\theta)$$

$$y = p \cdot \sin(\theta) \cdot \sin(\phi)$$

$$z = p \cdot \cos(\phi)$$

### Rectangular to Spherical

$$(x, y, z) \rightarrow (p, \theta, \phi)$$

$$x^2 + y^2 + z^2 = \left(p\sin \phi \cos \theta \right)^2 + \left( p \sin \phi \sin \theta \right)^2 + \left(p \cos \phi \right)^2$$

$$= p^2 \left( \sin^2 \phi \left( \cos^2 \theta + \sin^2 \theta \right) + \cos^2 \phi \right)$$

$$= p^2 \left( \sin^2 \phi + \cos^2 \phi \right) = p^2$$

$$\therefore p = \sqrt{x^2 + y^2 + z^2}$$

$$\theta = \tan^{-1} \frac y x$$

$$\phi = \cos^{-1} \frac{z}{\sqrt{x^2 + y^2 + z^2}}$$

## Constant Surfaces in Rectangular Coordinate System

$$x = x_0$$

$$y = y_0$$

$$z = z_0$$

![[Pasted image 20241005204926.png]]

## Constant Surfaces in Cylindrical Coordinate System

$r = r_0$ defines a `right cylinder`, $z = z_0$ defines a `plane`[^1] and $\theta = \theta_0$ defines a half `plane`[^1] attached to the `z axis`.  
![[Pasted image 20241005205402.png]]

## Constant Surfaces in Spherical Coordinate System

$p = p_0$ defines a `sphere`, $\theta = \theta_0$ defines a half `plane`[^1] and $\phi = \phi_0$ defines a `right cone`.

## Spherical Coordinates in Navigation

Imagine `z axis` going through the `north pole` of the earth, `x axis` going through the `prime meridian`.  
Then, the `longitutde` is specified in `east` and `west` `degrees`, represented by $\theta$ and `latitude` is specified in `north` and `south` `degrees`, represented by $\phi$.  
Where $p$ would be the `radius` of the earth.

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/3. Coordinate Planes and Graphs/Lecture|planes]].
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/4. Lines/Lecture|slopes]].