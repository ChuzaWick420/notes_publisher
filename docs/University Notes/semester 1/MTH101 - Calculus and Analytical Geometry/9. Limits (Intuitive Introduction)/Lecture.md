---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Tangent Problem
![[Pasted image 20240814164829.png]]  
Given a `graph` and a `point`, find `tangent` to the `graph` at that `point`.

The problem gave rise to `differential calculus`.

# Area Problem
![[Pasted image 20240814165139.png]]  
Given a `graph`, find area under it in interval $[a, b]$.

This problem gave rise to `integral calculus`.

# Area as a Limit
We can find the area under a `curve` by dividing it into smaller and smaller `rectangles`.  
And then taking the _sum_ of these `rectanlges`, we get our `area`.  
![[Pasted image 20240814171719.png]]  

# Limits

Imagine a function  

$$f(x) = \frac{\sin(x)}{x}$$

Notice how it is `undefined` at $x = 0$.  
This is where the `Limit` comes into play.  

$$\frac{\sin(x)}{x} = undefined$$

To check if a `limit` exists, meaning _what_ does the `function`[^1] approaches, we check from both _left_ and _right_ directions.

## From Right
What does the `function`[^1] approaches as $x$ approach to `0` from right direction.  

$$\lim_{x \rightarrow 0^+}\frac{\sin(x)}{x} = 1$$

## From Left
What does the `function`[^1] approaches as $x$ approach to `0` from left direction.  

$$\lim_{x \rightarrow 0^-}\frac{\sin(x)}{x} = 1$$

Therefore, to check the _existence_ of `lim`, 

$$\lim_{x \rightarrow 0^-}\frac{\sin(x)}{x} = \lim_{x \rightarrow 0^+}\frac{\sin(x)}{x} = 1$$

# References

[^1]: Read more about [[notes_publisher/docs/Mathematics/Function/Content|functions]].  
