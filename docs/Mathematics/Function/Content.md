---
Topic: Calculus
Sub-Topic: 
tags:
  - "calculus"
  - function
---

# Functions
## Definition
A `function` is a rule relating to 2 `sets`[^1] in such a way that it assigns only 1 element of one `set`[^1] to an element of another `set`[^1]

## Programmatic Intuition
It can be looked at as a `black box` which takes one `input`, does something to it and produces an `output`.  
![[Pasted image 20240812214426.png]]

## Notation
Since `function` is a relation between 2 variables, we can write it as:  

$$y = f(x)$$

Where $x$ is called the `independant variable` because it is our `input` of choice and $y$ is called `dependant variable` since it depends of $x$.

## Domain and Range
### Domain
The $x$ comes from a `set`[^1] that is `Set X` called its `domain`.

#### Types of Domains
##### Natural Domain
This `domain` comes out as a result of the formula of the `function` itself.

###### Example

$$f(x) = \frac{1}{x - 2}$$

Here, the `function` becomes undefined due to `division by zero` at $x = 2$.  
Hence, the `domain` is $\mathbb{R} - \{2\}$ or $(- \infty, 2) \cup (2, \infty)$.  

##### Restricted Domain
Sometimes, the `domain` of a `function` can be altered by doing operations from algebra on the `function` to simplify it. 

###### Example

$$f(x) = \frac{x^2 - 4}{x - 2}$$

We can simplify this and get  

$$h(x) = \frac{(x + 2) \cdot (x - 2)}{x - 2}$$

$$h(x) = x + 2$$

Notice how the `domain` of $f(x)$ excludes `2` but in case of $h(x)$ the `function` is actually defined.  
Therefore, we have to write it as  

$$h(x) = x + 2; x \ne 2$$

### Range
The $y$ comes from a `set`[^1] that is `Set Y` called its `range`.  
One of the techniques in finding `range` is to perform algebraic operations

#### Example

$$y = \frac{x + 1}{x - 1}$$

If we convert this equation to solve for $x$, we get:  

$$x = \frac{y + 1}{y - 1}$$

Clearly, we can see that $y \ne 1$.  
Therefore, the range is:  

$$\{y : y \ne 1\} = (- \infty, 1) \cup (1, +\infty) = \mathbb{R} - \{1\}$$

## Piecewise Function
![[Pasted image 20240812223103.png]]  
The graph of this `function` looks something like this.  
![[Pasted image 20240812223135.png]]

## References

[^1]: Read more about [[notes_publisher/docs/Mathematics/Set/Content|sets]]
