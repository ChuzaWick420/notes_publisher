---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-07
---

<span style="color: gray;">Dated: 07-11-2024</span>

# Introduction

## Origin of the Word: Algorithm

It comes from the name of a Muslim author `Abu Ja'far Mohammad ibn Musa al Khawarizmi`.  
He was born in $18^{\text{th}}$ century at `Khwarizm`(`Kheva`), a town south to river Oxus in present `Uzbekistan`.  
`Uzbekistan` is a Muslim country over 1000 years old, was taken by Russians in `1873`.  
He moved to `Baghdad` when he was a child under the Khalifah `Al-Mamun` during 813 to 833 C.E and died around 840 C.E.  
His work was written in a book called al `Kitab al-mukhatasar fi hisab al-jabr wa’l-muqabalah` (The Compendious Book on Calculation by Completion and Balancing).  
The words `Algebra` and `Algorithm` came from the title of this book.

## Algorithm: Informal Definition

An algorithm is a sequence of computation steps which takes a `set`[^1] of inputs and converts them into a `set`[^1] of outputs.

## Algorithms, Programming

Understanding of algorithms is essential for good understanding of programming.  
It is a Mathematical entity which is independent of technology.  
In any major programming project, there are 2 major issues

1. Macro
2. Micro

### Macro Issues

`Macro` issues are subject to software engineering, dealing with how to make the people able to coordinate to make the `software`.

### Micro Issues

`Micro` issues in programming involve how to best deal with these small critical tasks.

Project success may depend on writing code efficiently.  
Often, an inefficient design is chosen first, then optimized with tricks or better hardware, but poor design can't usually be overcome by fine-tuning.

A good design is crucial before implementation.  
Many CS courses explore these concepts in specific applications (e.g., compilers, OS, databases, AI, Computer Graphics).  
Strong algorithm design knowledge is key to understanding computer science and programming.

## Implementation Issues

In this course, `algorithms` are studied as mathematical models, ignoring implementation details like language and hardware, though these can affect performance.  
For instance, `quicksort` outperforms other sorting methods due to better data locality.  
Effective design combines theoretical and practical considerations: first, develop strong mathematical designs, refine based on real-world factors (e.g., data locality), and prototype to optimize performance.  
Use tools like `profilers` to further refine high-cost code sections.

## Course in Review

This course covers four sections: mathematical tools for `algorithm analysis` (`asymptotics`, `summations`, `recurrences`), `sorting algorithms` as a case study, various algorithmic problems and techniques, and an introduction to `NP-completeness`, where efficient solutions are unknown but possibly exist.

## Analyzing Algorithms

To design effective algorithms, we’ll focus on measuring computational resources like time and memory, though factors like disk access or bandwidth may also matter depending on the application.  
Practical algorithm design must also consider debugging, maintenance, and often incomplete specifications.  
Simple, adaptable algorithms are ideal, and most covered in this course are straightforward and modifiable for slight variations.

## Model of Computation

We aim to analyze algorithms independently of hardware and software specifics.  
`Algorithms` are meant for human understanding, so we can omit low-level details.  
To analyze meaningfully, we use a `RAM` (random access machine) model—an idealized, single-processor machine with infinite memory, where each basic operation (e.g., assignment, arithmetic, array access) takes constant time.  
While it doesn’t model all real-world factors, like data locality, the `RAM` model has been a reliable abstraction of modern computers since the 1960s.

## Example: 2 Dimension Maxima

For algorithm analysis, consider choosing a car: you want the fastest and cheapest option, but can't decide which matters more.  
A car that is both faster and cheaper than another "dominates" it.  
Given a set of cars, our goal is to list only those that aren't dominated by any other.  
This illustrates a formal problem model.

Let there be a 2D point $p$ with coordinates $p = (p.x, p.y)$

- A point $p$ is said to be dominated by point $q$ if $p.x \le q.x$ and $p.y \le q.y$.  
- Given a `set`[^1] of points $P =\{p_1, p_2, \ldots, p_n\}$ in 2D, a point $p$ is said to be `maximal` if it dominates every other point in $P$.

Each car is represented by a point $(x, y)$, where xxx is the car’s speed and $y$ is the negation of its price (higher $y$ means cheaper).  
The goal is to maximize both speed and affordability, with the most desirable cars having the highest values for both $x$ and $y$.

![[Pasted image 20241107151730.png]]  
/// caption  
Maximal points in 2D  
///

## Brute-force Algorithm

Consider a `set`[^1]  

$$P = \{p_1, p_2, \ldots, p_n\}$$

Take a point $p_i$ and compare it with all other points $p_j$.  
If $p_i$ is not dominated by $p_j$ then output it.

```
Maxima(int n, Point p[1 ... n])
	for i <- 1 to n
		do 
			maximal <- true
		for j <- 1 to n
		do
			if (i != j) and (P[i].x <= P[j].x) and (P[i].y <= P[j].y)
				then maximal <- false; break
		if (maximal = true)
			then output P[i]
```

`Pseudocode` has no formal syntax rules.  
Details such as type specifications for procedures and `variables`, or definitions for data types, can often be omitted if they are clear from context.  
The level of detail depends on the intended audience, and unnecessary details should be left out to focus on the main algorithm.  
Consistency checks, like ensuring distinct points in a set, are sometimes omitted to keep the `pseudocode` simple, even though they may be important for implementation.

![[Pasted image 20241107152858.png]]  
/// caption  
Points that dominate $(4, 11)$  
///

![[Pasted image 20241107152955.png]]  
/// caption  
Points that dominate $(9, 10)$  
///

![[Pasted image 20241107153102.png]]  
/// caption  
Points that dominate $(7, 7)$  
///

![[Pasted image 20241107153203.png]]  
/// caption  
Points that dominate all points  
///

## Running time Analysis

Our analysis focuses on measuring execution time and space (memory).  
We will ignore technological factors like computer speed, programming language, and compiler optimizations.  
To measure the running time of the brute-force 2-D maxima algorithm, we might count executed steps, element accesses, or comparisons.  
Running time depends on input size and structure, so different inputs of the same size may have varying running times.  
We use two criteria for measuring running time: worst-case time and average-case time.

### Worst case time

It is the maximum running time over all legal inputs of size $n$.  
Let $I$ denote an input instance and let $|I|$ denote its length, and let $T(I)$ denote the running time of an algorithm on input $I$.  
Then  

$$T_{\text{worst}}(n) = \max_{|I| = n} (T(I))$$

### Average case time

It is the average running time over all inputs of size $n$.  
Let $p(I)$ denote the `probability` of seeing this input.  
Then the `average case time` is the weighted sum of the running times with weights being the `probabilities`  

$$T_{\text{avg}}(n) = \sum_{|I| = n} p(I) T(I)$$

### Analysis of the Brute-force Maxima Algorithm

We usually focus on worst-case time, as `average-case` time is harder to compute due to the difficulty of specifying input probability distributions.  
`Worst-case` time gives an upper bound on the running time.


Assume the input size is $n$, and we count the number of times any element of $P$ is accessed.  
The outer loop runs $n$ times, and for each iteration, the inner loop also runs $n$ times.  
The if-statement makes four accesses to $P$, and the output statement makes two accesses for each maximal point, which occurs for each iteration in the worst case.

```
Maxima(int n, Point p[1 ... n])
	for i <- 1 to n    // n times
	do 
		maximal <- true
		for j <- 1 to n    // n times
		do
			if (i != j) and (P[i].x <= P[j].x) and (P[i].y <= P[j].y)    // 4 accesses
				then maximal <- false; break
		if (maximal = true)
			then output P[i].x, P[i].y    // 2 accesses
```

Thus we might express the `worst-case` running time as a pair of nested summations, one for the $i$-loop and the other for the $j$-loop

$$T(n) = \sum_{i=1}^{n} \left( 2 + \sum_{j=1}^{n} 4 \right)$$

$$=\sum_{i=1}^{n} (4n+2)$$

$$=(4n+2)n=4n^{2}+2n$$

For small numbers of $n$, it is fast enough but due to the $n^2$ term, it becomes an issue for running time.  
The worse time is  

$$\Theta (n^2)$$

This is called `asymptotic growth rate` of the `function`[^2] which we will discuss later.

### Arithmetic Series

$$\sum_{i=1}^{n}i=1+2+\ldots+n$$

$$=\frac{n(n+1)}{2}=\Theta(n^{2})$$

### Quadratic Series

$$\sum_{i=1}^{n}i^{2}=1+4+9+\ldots+n^{2}$$

$$=\frac{2n^{3}+3n^{2}+n}{6}=\Theta(n^{3})$$

### Geometric Series

$$\sum_{i=1}^{n}x^{i}=1+x+x^{2}+\ldots+x^{n}$$

$$=\frac{x^{(n+1)}-1}{x-1}=\Theta(n^{2})$$

If $0 < x < 1$ then it is $\Theta(1)$, otherwise if it is $x > 1$ then it is $\Theta(x^n)$

### Harmonic Series

$$H_{n}=\sum_{i=1}^{n}\frac{1}{i}$$

$$=1+\frac{1}{2}+\frac{1}{3}+\ldots+\frac{1}{n}\approx \ln n$$

$$=\Theta(\ln n)$$

## Analysis: a Harder Example

```
for i <- 1 to n
do 
	for j <- 1 to 2i
	do
		k = j ...
		while (k >= 0)
		do k = k - 1 ...
```

### Inner Loop

Consider the inner loop

```
while (k >= 0)
do k = k - 1
```

It is executed for $k = j, j - 1, j - 2, \ldots, 0$  
Time spent inside the `while` loop is constant.  
Let $I()$ be the time spent inside the `while` loop, then

$$I(j)=\sum_{k=0}^{j}1=j+1$$

### Middle Loop

Consider the middle loop  

```
for j <- 1 to 2i
do
```

Let $M()$ be the time  

$$M(i)=\sum_{j=1}^{2i}I(j)$$

$$=\sum_{j=1}^{2i}(j+1)$$

$$=\sum_{j=1}^{2i}j+\sum_{j=1}^{2i}1$$

$$=\frac{2i(2i+1)}{2}+2i$$

$$=2i^{2}+3i$$

### Outer Loop

Consider the outer loop

```
for i <- 1 to n
do 
```

$$T(n)=\sum_{i=1}^{n}M(i)$$

$$=\sum_{i=1}^{n}(2i^{2}+3i)$$

$$=\sum_{i=1}^{n}2i^{2}+\sum_{i=1}^{n}3i$$

$$=2\frac{2n^{3}+3n^{2}+n}{6}+3\frac{n(n+1)}{2}$$

$$=\frac{4n^{3}+15n^{2}+11n}{6}$$

$$=\Theta(n^{3})$$

### 2-dimension Maxima Revisited

We used [brute force algorithm](#brute-force-algorithm) but it uses no intelligence in pruning out decisions.  
The dominance relation is `transitive`, meaning if $p_j$ dominates $p_i$ and $p_k$ dominates $p_j$, then $p_k$ ultimately dominates $p_i$.  
Therefore, $p_i$ is not needed after we find any point which dominates it.

### Plane-sweep Algorithm

To improve running time, we use a plane sweep: sweeping a vertical line across the plane from left to right.  
We start by sorting points by x-coordinate.  
As we move the sweep line from left to right, we update the list of maximal points to the left.  
Points dominated by others appear at the end, so we scan the list from left to right, eliminating points with a lower y-coordinate.  
A stack can efficiently store and update maximal points, with the top of the stack holding the point with the highest x-coordinate.

![[Pasted image 20241107172357.png]]  
/// caption  
Sweep line at $(2, 5)$  
///  
![[Pasted image 20241107172411.png]]  
/// caption  
Sweep line at $(3, 13)$  
///  
![[Pasted image 20241107172426.png]]  
/// caption  
Sweep line at $(4, 11)$  
///  
![[Pasted image 20241107172437.png]]  
/// caption  
Sweep line at $(5, 1)$  
///  
![[Pasted image 20241107172448.png]]  
/// caption  
Sweep line at $(7, 7)$  
///  
![[Pasted image 20241107172459.png]]  
/// caption  
Sweep line at $(9, 10)$  
///  
![[Pasted image 20241107172522.png]]  
/// caption  
Sweep line at $(10, 5)$  
///  
![[Pasted image 20241107172532.png]]  
/// caption  
Sweep line at $(12, 12)$  
///  
![[Pasted image 20241107172547.png]]  
/// caption  
The final maximal set  
///  

```
Plane-Sweep-Maxima(n, P[1 .. n])
	sort P in ascending order by x
	stack s;
	for i <- 1 to n
	do
		while (s.notEmpty() & s.top().y <= P[i].y)
		do s.pop();
		s.push(P[i]);
	output the contents of stack s;
```

### Analysis of Plane-sweep Algorithm

Sorting takes $\Theta (n \log n)$.  
The `for`-loop runs $n$ times, and the inner `while`-loop seemingly runs $n − 1$ times, suggesting $\Theta(n^2)$.  
However, the `while`-loop only runs $n$ times in total, as each element is pushed and popped from the `stack` exactly once.  
Thus, the `for`-loop and `while`-loop together run $\Theta(n)$ times.  
With `sorting`, the total runtime of the `plane-sweep algorithm` is $\Theta(n \log n)$.

### Comparison of Brute-force and Plane Sweep Algorithms

$$\frac{n^{2}}{n \log n}=\frac{n}{\log n}$$

| $n$     | $\log n$ | $\frac n {\log n}$ |
| ------- | -------- | ------------------ |
| 100     | 7        | 15                 |
| 1000    | 10       | 100                |
| 10000   | 13       | 752                |
| 100000  | 17       | 6021               |
| 1000000 | 20       | 50171              |

For $n = 1,000,000$, if plane-sweep takes 1 second, brute-force takes 14 hours.  
This highlights the importance of asymptotic analysis in choosing efficient algorithms for large inputs, where running times become a critical factor.  
Efficient design ensures that users can handle large inputs within a reasonable timeframe.

## References

[^1]: Read more about [[notes_publisher/docs/Mathematics/Set/Content|sets]].
[^2]: Read more about [[notes_publisher/docs/Mathematics/Function/Content|functions]].