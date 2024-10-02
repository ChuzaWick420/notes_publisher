---
tags:
  - university-notes
  - limits
  - sigma
university-name: Virtual University of Pakistan
---

# Area as Limits
## Definition of Area
Let us define `area` under a curve, to be a `sum` of areas of `rectangles` which are created as a result of dividing the `interval`[^1] $[a, b]$ into $n$ slices.  
![[Pasted image 20240926095520.png]]  
We are taking $[a, b]$ into consideration. The `width` of this slice is $b - a$.  
Then we divide this `width` into $n$ slices. The `width` of each slice will be $\frac{b - a}{n}$  
![[Pasted image 20240926100353.png]]  
Then we take the `sum` of `areas` of these `rectangles`.  
If $R_n$ is the `nth rectangle` and $R$ is the whole region which comes out as a result of `summation` then  

$$A = area(R) = \lim_{n \to \infty} area(R_n)$$

The `width` of each `rectangle` would be $\Delta x = \frac{b - a}{n}$.  
The `height` of each `rectangle` would be $f(x_i)$ where $i$ is the `index`, pointing to each `rectangle` at a time.  
Hence, `area` of `ith rectangle` is $f(x_i) \cdot \Delta x$  

$$area(R_n) = f(x_1) \cdot \Delta x + f(x_2) \cdot \Delta x + \ldots + f(x_n) \cdot \Delta x$$

$$= \Delta x \left(f(x_1) + f(x_2) + \ldots + f(x_n)\right)$$

$$= \Delta x \sum_{i = 1}^{n} f(x_i)$$

$$\because A = area(R) = \lim_{n \to \infty} area(R_n)$$

$$A = \lim_{n \to \infty} \sum_{i = 1}^{n} f(x_i) \cdot \Delta x$$

## Example
### Problem
Find `area` under the `line`[^2] $y = x$ over the `interval`[^1] $[a, b]$.  
![[Pasted image 20240926101918.png]]

### Solution
#### Approach 1
As we know, the graph creates a `triangle`, we can divide it into pieces  
![[Pasted image 20240926102212.png]]  
Then, to find the desired area, we perform the following  
![[Pasted image 20240926102359.png]]  
The bigger `triangle` has `base` $2 - 0 = 2$ and `height` being $2$.  
Therefore, $A_1 = \frac 1 2 (2) (2) = 2$  
The smaller `triangle` has `base` $1 - 0 = 0$ and `height` being $1$ as well.  
Therefore, $A_2 = \frac 1 2 (1)(1) = \frac 1 2$  
The `area` of our desired section is $A_3 = A_1 - A_2$.  

$$A_3 = 2 - \frac 1 2 = \frac 3 2 = 1.5$$

#### Approach 2
We will use our previous conclusion  

$$A = \lim_{n \to \infty} \sum_{i = 1}^{n} f(x_i) \cdot \Delta x$$

Here $\Delta x = \frac{2 - 1}{n} = \frac 1 n$  
Let's discuss $f(x_i)$. Since our equation is $f(x) = y = x$, therefore, $f(x_i) = x_i$.  
We know that the `width` is $\Delta x = \frac 1 n$ and each $x_i$ is apart by $\Delta x$ distance.  
Hence, we can select each slice using $i \cdot \frac 1 n$.  
We will also _add_ $1$ which acts as our `offset` because the `interval`[^1] starts from $1$.  

$$\therefore f(x_i) = 1 + \frac i n$$

Plug these values in the equation above,

$$A = \lim_{n \to \infty} \sum_{i = 1}^{n} \left(1 + \frac i n\right) \frac 1 n$$

Using the properties of `sigma`[^3]

$$= \lim_{n \to \infty} \frac 1 n \sum_{i = 1}^{n} \left(1 + \frac i n\right)$$

$$= \lim_{n \to \infty} \frac 1 n \left(\sum_{i = 1}^{n} 1 + \sum_{i = 1}^{n} \frac i n\right)$$

$$= \lim_{n \to \infty} \frac 1 n \left(n + \frac 1 n \sum_{i = 1}^n i\right)$$

$$= \lim_{n \to \infty} \frac 1 n \left(n + \frac 1 n \cdot \frac{n (n + 1)}{2} \right)$$

$$= \lim_{n \to \infty} \frac 1 n \left(n + \frac{(n + 1)}{2} \right)$$

$$= \lim_{n \to \infty} \frac 1 n \left(\frac{2n + (n + 1)}{2} \right)$$

$$= \lim_{n \to \infty} \frac 1 n \left(\frac{3n + 1}{2} \right)$$

$$= \lim_{n \to \infty} \left(\frac{3n + 1}{2n} \right)$$

$$= \lim_{n \to \infty} \left(\frac{3}{2} + \frac{1}{2n} \right)$$

$$\because \lim_{n \to \infty} \frac{1}{2n} = 0$$

$$= \lim_{n \to \infty} \left(\frac{3}{2} + \frac{1}{2n} \right) = \frac 3 2 = 1.5$$

## References
Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/1. Coordinates, Graphs, Lines/Lecture|intervals]].
[^2]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/4. Lines/Lecture|lines]].
[^3]: Read more about [[semester 1/MTH101 - Calculus and Analytical Geometry/27. Sigma Notation/Lecture|sigma]].
