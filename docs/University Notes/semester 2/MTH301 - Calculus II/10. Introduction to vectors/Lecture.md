---
tags:
  - university-notes
  - vectors
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Introduction of Vectors

There are some quantities which can be described completely by `magnitude`.  
These are called `scalar quantities`.  
Some quantities cannot be completely described using only `magnitude` and we also need `direction`.  
There are called `vector quantities`.

## Representation

These are represented as _arrows_ directed in the direction of the action, while the `magnitude` is represented by the `length` of the arrow.  
![[Pasted image 20241008135306.png]]

If $A$ and $B$ are the endpoints of this `vector` then it can be written as:  

$$\vec{v} = \vec{AB}$$

and the `magnitude` can be determined by

$$\lvert \vec{v} \rvert = \lvert \vec{AB} \rvert$$

## Unit Vector

It is a `vector` with `magnitude` $1$.  

$$\hat{v} = \frac{\vec{v}}{\lvert \vec{v} \rvert}$$

## Addition of Vectors

![[Pasted image 20241008141141.png]]  
Imagine we have 2 `vectors` $\vec{OP}$ and $\vec{OQ}$ then the `vector` which comes as the result of $\vec{OP} + \vec{OQ}$ is constructed by joining the tail of either `vector` with the head of other one and then constructing a vector whose tail connects with tail of first `vector` and head with head of second `vector`.  
This new `vector` is called `resultant vector`.

## Equal Vectors

Two `vectors` are equal if they have same `magnitude` and same `direction`.  
![[Pasted image 20241008141903.png]]

## Opposite Vectors

Two `vectors` are called `opposite vectors` if they have same `magnitude` but opposite direction.  
![[Pasted image 20241008142058.png]]

## Parallel Vectors

Two `vectors` are called `parallel vectors` if they got same direction but magnitudes can be different or same.  
![[Pasted image 20241008142324.png]]  
Here $c$ is a `constant`.

![[Pasted image 20241008142744.png]]  
If $\hat{i}, \hat{j} \text{ and } \hat{z}$ are the `unit vectors` then using [vector addition](#addition-of-vectors), we can represent a point using a `vector` relative to the `origin`.

## Subtraction of Vectors

Similar to [vector addition](#addition-of-vectors), `subtraction` also works in similar way except that the direction of the `vector` being subtracted, is _flipped_.

## Scalar or Dot Product

$$\vec{A} \cdot \vec{B} = \lvert \vec{A} \rvert \lvert \vec{B} \rvert \cos (\theta)$$

Where $\theta$ is the angle between $\vec{A}$ and $\vec{B}$.  

$$\vec{A} \cdot \vec{B} = \vec{B} \cdot \vec{A}$$

1. If $\vec{A} \perp \vec{B}$ then $\vec{A} \cdot \vec{B} = 0$
2. If $\vec{A} \parallel \vec{B}$ then $\vec{A} \cdot \vec{B} = 1$

$$\vec{A} = a_1 \hat{i} + a_2 \hat{j} + a_3 \hat{z}$$

$$\vec{B} = b_1 \hat{i} + b_2 \hat{j} + b_3 \hat{z}$$

Then $$\vec{A} \cdot \vec{B} = a_1b_1 + a_2b_2 + a_3b_3$$

## Angle between 2 Vectors

From the definition of `dot product`, the $\theta$ can be found out as follows  

$$\theta = \cos^{-1} \left( \frac{\vec{A} \cdot \vec{B}}{\lvert \vec{A} \rvert \lvert \vec{B} \rvert} \right)$$

## Vector Projection

![[Pasted image 20241009132233.png]]  

$$\cos(\theta) = \frac{\lvert \vec{OC} \rvert}{\lvert \vec{OB} \rvert}$$

$$\lvert \vec{OB} \rvert \cdot \cos(\theta) = \lvert \vec{OC} \rvert$$

$$\frac{\lvert \vec{OB} \rvert \cdot \rvert \vec{OA} \lvert \cdot \cos(\theta)}{\rvert \vec{OA} \lvert} = \lvert \vec{OC} \rvert$$

$$\frac{\vec{OB} \cdot \vec{OA}}{\lvert \vec{OA} \rvert} = \lvert \vec{OC} \rvert$$

$$\vec{OB} \cdot \hat{OA} = \lvert \vec{OC} \rvert$$

This number $\lvert \vec{OB} \rvert \cos(\theta)$ is called the `scalar` component of $\vec{OB}$ in the direction of $\vec{OA}$.

## Cross Product

$$\vec{A} \times \vec{B} = \lvert \vec{A} \rvert \lvert \vec{B} \rvert \sin(\theta) \hat{n}$$

![[Pasted image 20241010121556.png]]

According to `right hand rule`, curl your fingers from _1st_ `vector` towards the _2nd_ `vector`.  
The thumb will point in the direction of $\hat{n}$ which is _perpendicular_ to the `plane`[^1] in which both $\vec{A}$ and $\vec{B}$ are present.

$$\vec{B} \times \vec{A} = - \lvert \vec{A} \rvert \lvert \vec{B} \rvert \sin(\theta) \hat{n}$$

$$\vec{A} \times \vec{B} = - \vec{B} \times \vec{A}$$

## Area of a Parallelogram

$$\text{Area} = \text{base} \times \text{height}$$

![[Pasted image 20241010122439.png]]  

$$\because \text{height} = \lvert \vec{B} \rvert \cdot \sin(\theta)$$

$$\because \text{base} = \lvert \vec{A} \rvert$$

$$\therefore \text{Area} = \lvert \vec{A} \rvert \cdot \lvert \vec{B} \rvert \sin(\theta)$$

$$= \lvert \vec{A} \times \vec{B} \rvert$$

## $\vec{A} \times \vec{B}$ From Components

If  

$$\vec{A} = a_1 \hat{i} + a_2 \hat{j} + a_3 \hat{k}$$

$$\vec{B} = b_1 \hat{i} + b_2 \hat{j} + b_3 \hat{k}$$

then after some multiplication, we get  

$$\vec{A} \times \vec{B} = \hat{i}(a_2b_3 - a_3b_2) - \hat{j}(a_1b_3 - a_3b_1) + \hat{k}(a_1b_2 - a_2b_1)$$

which can be written in more compact form as

$$= \hat{i} 
\left|
\begin{matrix}
a_2 & a_3 \\
b_2 & b_3
\end{matrix}
\right|
- \hat{j}
\left|
\begin{matrix}
a_1 & a_3 \\
b_1 & b_3
\end{matrix}
\right|
+ \hat{k}
\left|
\begin{matrix}
a_1 & a_2 \\
b_1 & b_2
\end{matrix}
\right|
$$

which can further be written as

$$= 
\left|
\begin{matrix}
\hat{i} & \hat{j} & \hat{k} \\
a_1 & a_2 & a_3 \\
b_1 & b_2 & b_3
\end{matrix}
\right|
$$

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[3. Coordinate Planes and Graphs|planes]].