---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-10
---

<span style="color: gray;">Dated: 10-11-2024</span>

# Applications of First order Differential Equations

In order to translate a physical phenomena in terms of mathematics, we strive for a set of equations which describe the system adequately.  
This set of equations is called `Model` for the phenomena.

## Steps of Building a Model

1. Clearly state the assumptions on which the model will be based. These assumptions should describe the relationships among quantities to be studied.
2. Completely describe the parameters and variables to be used in the model.
3. Use the assumptions from `step 1` to derive the mathematical equations relating to `parameters` and `variables` from `step 2`.

## Applications

- Orthogonal Trajectories
- Population dynamics
- Radioactivity decay
- Newton's law of cooling
- Carbon dating
- Chemical reactions

We know that solutions to `first order linear differential equations`[^1] can be given by `implicit equations` of the form  

$$F(x, y, C) = 0$$

Where $C$ is a family of `curves`.  
Member `curves` can be obtained by fixing $C$.

Similarly for an $n^{\text{th}}$ order differential equation,  

$$F(x, y, C_1, C_2, \ldots, C_n) = 0$$

Now the question is, can we represent an $n^{\text{th}}$ order differential equation with $n$ parameter family of curves as an $n^{\text{th}}$ order differential equation with no parameters but still representing the family?  
The answer in most cases is yes.

Some clues on how we can proceed.

1. Differentiate with respect to $x$ and get an equation involving $x$, $y$, $\frac{dy}{dx}$ and $C$.
2. Using the original equation, we may be able to eliminate $C$ from the new equation.
3. Do some algebra and re-write the equation in `explicit form`  

$$\frac{dy}{dx} = f(x, y)$$

### Example

Let us say we have following families of `curves`.

$$
\begin{cases}
	y = mx \\
	x^2 + y^2 = C^2
\end{cases}
$$

The first family represents straight `lines`[^2] passing through the `origin`.  
The second family represents `circles` centered at the `origin`.

Something like this  
![[mth401_10_d_1.svg]]

It is clear that the `lines`[^2] are perpendicular to the `tangent lines` to the `circles` at the point of intersections.

### Orthogonal Curves

Two curves $C_1$ and $C_2$ are called `orthogonal` if their `tangent lines` are perpendicular to each other at their point of intersection.

## Orthogonal Trajectories

When all the `curves` of the family  

$$\mathcal F_1 : G(x, y, c_1) = 0$$

orthogonally intersect all curves of another family

$$\mathcal F_2 : H(x, y, c_2) = 0$$

then each curve of a family is said to be orthogonal trajectory of another.

### Occurrences

- Fluid dynamics
- Electricity and magnetism

### Method of Finding Orthogonal Trajectory

Consider a family of `curves` $\mathcal F$ and assume the associated differential equation is  

$$\frac{dy}{dx} = f(x, y)$$

since $\frac {dy}{dx}$ is giving `slopes` to the curves at $(x, y)$.  
Therefore, the differential equation for the family of `curves` having orthogonal `slopes` will be

$$\frac{dy}{dx} = - \frac 1 {f(x, y)}$$

## Summary

- Consider a family of `curves` $\mathcal F$ and the associated differential equations.
- Re-write the differential equation in the form  

$$\frac{dy}{dx}=f(x,y)$$

- Write the differential equation associated with the orthogonal family.  

$$\frac{dy}{dx}=-\frac{1}{f(x,y)}$$

- Solve the equation and the solutions are the families of orthogonal curves.
- A specific curve from the orthogonal family may be required, something like an `initial value problem`.[^3]

### Example

Find the orthogonal trajectory to the family of circles  

$$x^2 + y^2 = C^2$$

#### Solution

$$2y\frac{dy}{dx}+2x=0$$

$$\frac{dy}{dx}=-\frac{x}{y}$$

$$\frac{dy}{dx}=-\frac{1}{- \frac x y}=\frac{y}{x}$$

$$u(x)=e^{-\int\frac{1}{x}dx}=\frac{1}{x}$$

$$y.u(x)=m$$

$$y=\frac{m}{u(x)}=mx$$

## Population Dynamics

The easiest `population dynamics model` is `exponential model`.  
This `model` is based on the following assumption

> [!NOTE]- Assumption  
> The rate of change of the population is proportional to the existing population

If $P(t)$ measures the population at time $t$ then.  

$$\frac{dP}{dt} = kP$$

Where $k$ is the constant of proportionality.  

$$\frac{d}{dt}[Pe^{-kt}]=0$$

`Integrating`[^4] both sides, we get  

$$Pe^{-kt}=C$$

$$P=Ce^{kt}$$

if the initial population is  

$$P(0) = P_0$$

so that  

$$C = P_0$$

then  

$$P(t)=P_{0}e^{kt}$$

Where $k > 0$ for growth and $k < 0$ for decay.

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[notes_publisher/docs/University Notes/semester 5/MTH401 - Differential Equations/7. First Order Linear Equation/Lecture|first order linear differential equations]].
[^2]: Read more about [[4. Lines|lines]].
[^3]: Read more about [[notes_publisher/docs/University Notes/semester 5/MTH401 - Differential Equations/2. Fundamentals/Lecture|initial value problem]].
[^4]: Read more about [[25. Integrations|integration]].