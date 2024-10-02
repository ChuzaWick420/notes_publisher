---
tags:
  - university-notes
  - linear-equations
  - geometry
university-name: Virtual University of Pakistan
---

# Lines
## Slopes
![[Pasted image 20240812131250.png]]

If $\overline{AB}$ is a line then, its `slope` is defined to be the `ratio` from `rise` to `run`.  

$$m = \frac{y_2 - y_1}{x_2 - x_1}$$

## Angle of Inclination
From the slope, we can fine the `angle of inclination` by using $\tan^{-1}{(m)}$.  
![[Pasted image 20240812132611.png]]

## Parallel and Perpendicular Lines
### Parallel
For `parallel` lines, if $m_1$ and $m_2$ are `slopes` of each line then

$$m_1 = m_2$$

### Perpendicular
For `perpendicular` lines,  

$$m_1 = \frac{-1}{m_2}$$

![[Pasted image 20240812134340.png]]

To prove:  

$$\tan(\theta_1) \cdot \tan(\theta_2) = -1$$

$$\because \theta_2 = \theta_2 + 90\degree$$

$$\tan(\theta_1) \cdot \tan(\theta_1 + 90) = -1$$

$$\tan(\theta_1) \cdot - \cot(\theta_1 ) = -1$$

The `-` sign comes from the fact that `rise` is in $y^+$ and `run` is in $x^-$ .  

$$\because \cot(\theta) = \frac{1}{\tan{\theta}}$$

$$\tan(\theta_1) \cdot \frac{-1}{\tan(\theta_1 )} = -1$$

$$-1 = -1$$

## Equations of Lines
### Lines Parallel to Coordinate Axes
#### `x-axis`
![[Pasted image 20240812135906.png]]

More generally,  

$$x = a$$

 Where $a$ is a `constant`.

#### `y-axis`
If we take `y` in terms of `function` then notice how it does not depend on `x`, hence it is a `constant`.  
![[Pasted image 20240812135733.png]]

More generally,  

$$y = a$$

 Where $a$ is a `constant`.

### Slope - Point Form
if we are given `slope` of a line along with single point $P(x_1, y_1)$ which lies on that line then we can construct the equation for it.  

$$m = \frac{y - y_1}{x - x_1}$$

$$y - y_1 = m \cdot (x - x_1)$$

Here, the $P(x, y)$ is any arbitrary point.

### Slope - Intercept Form
#### Relative to `x-axis`
If we have an `x intercept` called $a$ then the previous equation takes form of  

$$y - 0 = m \cdot (x - a)$$

#### Relative to `y-axis`
If we have an `y intercept` called `b` then the previous equation takes form of  

$$y - b = m \cdot (x - 0)$$

### General Equation

$$ax + by + c = 0$$

Where `a`, `b` and `c` are `constants`.  
This equation is called `first degree` equation.

## References
Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].
