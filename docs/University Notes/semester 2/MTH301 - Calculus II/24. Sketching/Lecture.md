---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Sketching
## Graph of $r = \sin(\theta)$
Let us take some samples.  
For that, we will increment $\theta$ by $\frac \pi 2 30^{\circ}$ and construct a table containing our samples

| $\theta$ (radians) | $0$   | $\frac{\pi}{6}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ | $\frac{2\pi}{3}$ | $\frac{5\pi}{6}$ |
|--------------------|-------|----------------|----------------|----------------|-----------------|-----------------|
| $r = \sin \theta$  | $0$   | $\frac{1}{2}$  | $\frac{\sqrt{3}}{2}$ | $1$          | $\frac{\sqrt{3}}{2}$ | $\frac{1}{2}$  |

| $\theta$ (radians) | $\pi$ | $\frac{7\pi}{6}$ | $\frac{4\pi}{3}$ | $\frac{3\pi}{2}$ | $\frac{5\pi}{3}$ | $\frac{11\pi}{6}$ | $2\pi$ |
|--------------------|-------|-----------------|-----------------|-----------------|-----------------|-------------------|-------|
| $r = \sin \theta$  | $0$   | $-\frac{1}{2}$  | $-\frac{\sqrt{3}}{2}$ | $-1$          | $-\frac{\sqrt{3}}{2}$ | $-\frac{1}{2}$ | $0$   |

![[Pasted image 20241014122859.png]]

To convert the polar coordinates into the cartesian ones, we need to multiply both sides of equation with $r$.

$$\because r = \sin(\theta)$$

$$r^2 = r \cdot \sin(\theta)$$

$$x^2 + y^2 = y$$

$$x^2 + y^2 - y = 0$$

By `completing the square` method, we get  

$$x^2 + \left(y - \frac 1 2\right)^2 = \frac 1 4$$

Hence, it is a `circle` with $radius = \frac 1 2$ centered at $\left(0, \frac 1 2\right)$.

## Limacons
Following form of equations are of `limacons`.  

$$r = a + b \sin (\theta)$$

$$r = a - b \sin (\theta)$$

$$r = a + b \cos (\theta)$$

$$r = a - b \cos (\theta)$$

### Cardioid
Special case for `limacons` in which $a = b$, creates a `cardioid`.  
![[Pasted image 20241014124438.png]]

### Inner Ring
if $b > a$ or $\frac a b < 1$ then the `limacons` have an inner ring.

## Leminscate
There is a greek word called `lemnicos` which means `looped ribon`.  
If $a > 0$ then following are the equations for `leminscate`.

$$r^2 = a^2 \cos 2\theta$$

$$r^2 = -a^2 \cos 2\theta$$

$$r^2 = a^2 \sin 2\theta$$

$$r^2 = -a^2 \sin 2\theta$$

![[Pasted image 20241014124949.png]]

The $a$ determines the `length` of each petal.

## Rose Curve

$$r = a \sin(n \cdot \theta)$$

$$r = a \cos(n \cdot \theta)$$

Where $n \in \mathbb{Z}$.

- If $n$ is even, we get $2n$ petals
- if $n$ is odd, we get $n$ petals

![[Pasted image 20241014125422.png]]

## Spiral

$$r = a \cdot \theta$$

![[Pasted image 20241014125545.png]]

## References
Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].
