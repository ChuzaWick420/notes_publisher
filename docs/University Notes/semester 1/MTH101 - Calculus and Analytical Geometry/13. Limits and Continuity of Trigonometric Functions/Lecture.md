---
tags:
  - university-notes
  - trigonometry
  - circle
  - inequalities
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Continuity of Trigonometric Functions

Let us define a constant $h = x - c$ such that $x = h + c$.  
The benefit of doing so is to give us the ability to replace $x \rightarrow c$ with $h \rightarrow 0$.  

$$\because \lim_{x \rightarrow 0} \sin(x) = 0$$

$$\because \lim_{x \rightarrow 0} \cos(x) = 1$$

So to prove the continuity of $\cos$ and $\sin$ functions, we will modify our definition of `continuity`.[^1]
1. $f(c)$ is defined.
2. $\lim_{h \rightarrow 0} f(h + c)$ exists.
3. $\lim_{h \rightarrow 0} f(h + c) = f(c)$

## Proofs

$$\lim_{h \rightarrow 0} \sin(h + c) = \sin(c)$$

$$\lim_{h \rightarrow 0} \sin(h + c) = \lim_{h \rightarrow 0}\left( \sin(h) \cdot \cos(c) + \sin(c) \cdot \cos(h) \right)$$

$$ = \cos(c) \cdot \lim_{h \rightarrow 0} \sin(h) + \sin(c) \cdot \lim_{h \rightarrow 0} \cos(h)$$

$$= \cos(c) \cdot (0) + \sin(c) \cdot (1)$$

$$= \sin(c)$$

## Squeeze Theorem

Let us have 3 `functions`[^2] such that

$$g(x) \le f(x) \le h(x)$$

If $\lim_{x \rightarrow a} g(x) = \lim_{x \rightarrow a} h(x) = L$ then $\lim_{x \rightarrow a} f(x) = L$.

### Use case

Let us try to prove why the `area of a sector` is defined to be:  

$$Area = \frac 1 2 r^2 \cdot \theta$$

Where $r$ is the `radius` of the `circle`.  
![[Pasted image 20240815230447.png]]  
Let us say, the `area` of this `triangle` is $A_1 = \frac 1 2 \cdot 1 \cdot \sin(x)$ that is $\frac {\sin(x)}{2}$ .  
Recall,  

$$Area = \frac 1 2 \times base \times perp$$

 $$\because base = 1$$

 $$\because perp = \sin(\theta)$$

Then there is `area of the sector` that is $A_2 = \frac 1 2 \cdot 1^2 \cdot x$ that is $\frac x 2$.

Then there is another `triangle`.  
![[Pasted image 20240815231728.png]]  
The `area` of this `triangle` is $A_3 = \frac 1 2 \cdot 1 \cdot \tan(x)$ that is $\frac{\tan(x)}{2}$.  
The `base` is $\tan(x)$ because  

$$\because \tan(x) = \frac {perp}{base}$$

$$\because base = 1$$

  $$\therefore \tan(x) = perp$$

From visual aids, it is clear that $A_1 \le A_2 \le A_3$.  

$$\frac{sin(x)}{2} \le \frac x 2 \le \frac{\tan(x)}{2}$$

Multiplying all sides by $\frac{2}{\sin(x)}$.  

$$1 \le \frac{x}{\sin(x)} \le \frac{1}{\cos(x)}$$

Taking reciprocals and applying the theorem of `inequalities`.[^3]  

$$1 \ge \frac{x}{\sin(x)} \ge \cos(x)$$

Applying our `squeezing theorem`, we get  

$$\lim_{x \rightarrow 0} 1 \ge \lim_{x \rightarrow 0} \frac{x}{\sin(x)} \ge \lim_{x \rightarrow 0} \cos(x)$$

$$1 \ge 1 \ge 1$$

Hence, the formula for `area of the sector` of a `circle` holds true.

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/12. Continuity/Lecture|continuity]].
[^2]: Read more about [[Mathematics/Function/Content|functions]].  
[^3]: Read more about [[1. Coordinates, Graphs, Lines|inequalities]].