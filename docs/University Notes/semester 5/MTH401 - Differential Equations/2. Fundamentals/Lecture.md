---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-07
---

<span style="color: gray;">Dated: 07-11-2024</span>

# Fundamentals

## Growth Equation

$$\frac{du}{dt} = F(t)G(u)$$

## The Pendulum Equation

$$\frac{d^2\theta}{dt^2} + \frac g l \sin(\theta) = F(t)$$

## The Van Da Pol Equation

$$\frac{d^2y}{dt^2} + \epsilon (y^2 + 1) \frac {dy}{dt} + y = 0$$

## The Lcr Oscillator Equation

$$L \frac{d^2 Q}{dt^2} + R \frac{dQ}{dt} + \frac Q C = E(t)$$

## A Riccati Equation

$$\frac {dp}{dt} = - 2a (t)p + \frac{b(t)^2}{u(t)}p^2 - v(t)$$

## Ordinary Differential Equation

If an equation contains an ordinary `derivative`[^1] of one or more dependent variables then it is called `ordinary differential equation`.

### Example

$$\frac{d^{2}y}{dx^{2}}+5\left(\frac{dy}{dx}\right)^{3}-4y=e^{x}$$

## Partial Differential Equation

If an equation contains a `partial derivative`[^2] of one or more dependent variables then it is called `partial differential equation`.  

$$a^2 \frac{\partial^4 u}{\partial x^4} + \frac{\partial^2 u}{\partial x^2} = 0$$

Imagine if the following `function`[^3] defined over an `interval`[^4] $I$ 

$$f\left(t, y, y^\prime, \ldots, y^{(n)}\right) = 0$$

such that

1. $y(t)$ and its first $n$ `derivatives`[^1] exist over the `interval`[^4] $I$ for all $t$ and its first $n - 1$ `derivatives`[^1] are `continuous`[^5] over $I$.
2. $y(t)$ satisfied the differential equation for all $t$ in $I$.

## Initial Value Problem Examples

### The Logistic Equation

$$p^\prime = ap - bp^2$$

With initial condition $p(t_0) = p_0$ for $p_0 = 10$, the solution is  

$$p(t) = \frac {10 a}{10 b + (a - 10b)e - a(t - t_0)}$$

### The Mass Spring System Equation

$$x^{\prime\prime} + \left(\frac a m \right) x^\prime + \left(\frac k m\right)x = g + \left(\frac{F(t)}{m}\right)$$

## Boundary Value Problem

### Example 1

$$y^{\prime\prime} + 9y = \sin(t)$$

with initial conditions $y(0) = 1, y^\prime(2p) = -1$, solution is  

$$y(t) = \left(\frac 1 8\right)\sin(t) + \cos(3t) + \sin(3t)$$

### Example 2

$$y^{\prime\prime} + p^2y = 0$$

With initial conditions $y(0) = 2, y(1) = -2$, solution would be  

$$y(t) = 2 \cos(pt) + (c) \sin (pt)$$

## Properties

### Linear

If the $nth$ order `differential equation` can be written as following then it is called `linear`  

$$a_n(t)y(n) + a_{n - 1}(t) y (n - 1) + \ldots + a_1y^\prime + a_0(t)y = h(t)$$

### Non Linear

$$x_3(y^{\prime\prime\prime})3 - x_2y(y^{\prime\prime}) + 3xy^\prime + 5y = ex$$

### Super Position

It allows us to decompose a problem into smaller, simpler parts and then combine them to find a solution to the original problem.

## Solutions

### Explicit

$$F\left(x, y, \frac{dy}{dx}, \frac{d^2y}{dx^2}, \ldots, \frac{d^ny}{dx^n}\right) = 0$$

Then the solution of the form $y = f(x)$ is called `explicit solution`.

#### Example

For the following differential equation  

$$\frac{d^2y}{dx^2} - 2\frac{dy}{dx} + y = 0$$

The solution is  

$$y = xex$$

### Implicit

A relation $G(x, y)$ is known as an implicit solution of a differential equation, if it defines one or more explicit solution on $I$.

#### Example

For the differential equation

$$y^\prime = - \frac x y$$

the solution is

$$x^2 + y^2 - 4 = 0$$

$$y = \pm \sqrt {4 - x^2}$$

## References

Read more about [[M_Notations|notations and symbols]].

[^1]: Read more about [[15. The Derivative|derivatives]].
[^2]: Read more about [[notes_publisher/docs/University Notes/semester 2/MTH301 - Calculus II/7. Geometric meaning of partial derivative/Lecture|partial derivatives]].
[^3]: Read more about [[M_Function|functions]].
[^4]: Read more about [[1. Coordinates, Graphs, Lines|intervals]].