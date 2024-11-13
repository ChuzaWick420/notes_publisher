---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-13
---

<span style="color: gray;">Dated: 13-11-2024</span>

# Divide and Conquer Strategy

Divide-and-conquer, inspired by ancient Roman strategy, involves breaking a large problem into smaller pieces, solving them individually, and combining their solutions.  
This recursive process continues until the pieces are trivial to solve (e.g., one or two items).  
Summarizing, the main elements to a divide-and-conquer solution are:

## Divide

Divide the problem into a small number of pieces

## Conquer

solve each piece by applying divide and conquer to it recursively

## Combine

Combine the pieces together into a global solution.

## Merge Sort

Divide-and-conquer applies to many computational problems. A key example is sorting, where a sequence $A[1 .. n]$ is rearranged to output the elements in increasing order.  
Here is how the merge sort algorithm works

### Divide

Split $A$ down the middle into two subsequences, each of size roughly $\frac n 2$.

### Conquer

Sort each subsequence by calling `merge sort` recursively on each.

### Combine

Merge the two sorted subsequences into a single sorted list.

---

To design `mergeSort`, we recursively sort sub-arrays and merge them. The procedure `mergeSort(A, p, r)` sorts $A[p:r]$.  
If $r=p$, the sub-array has one element and is already sorted.  
Otherwise, compute $q=\lfloor(p+r)/2\rfloor$, split into $A[p:q]$ and $A[q+1:r]$, recursively sort both, and merge the results into a single sorted array.

```
mergeSort(array A, int p, int r)
	if (p < r)
	then 
		q <- (p + r) / 2
		mergeSort(A, p, q)     // sort A[p .. q]
		mergeSort(A, q + 1, r) // sort A[q + 1 .. r]
		merge(A, p, q, r)      // merge two pieces
```

![[Pasted image 20241113095239.png]]  
/// caption  
Merge Sort: Divide Phase  
///

### Merging

The `merge(A, p, q, r)` procedure merges two sorted sub-arrays $A[p:q]$ and $A[q+1:r]$ into a temporary array $B[p:r]$.  
Using indices $i$ and $j$, we compare elements from both sub-arrays, placing the smaller into $B$ at position $k$, and increment the respective index.  
When one sub-array is exhausted, we copy the remaining elements of the other into $B$.  
Finally, $B$ is copied back into $A$.  
Temporary arrays are a minor limitation of `MergeSort`.

```
merge(array A, int p, int q, int r)
	int B[p .. r]
	int i <- k <- p
	int j = q + 1
	
	while(i <= q) and (j <= r)
	do 
		if (A[i] <= A[j])
		then
			B[k++] <- A[i++]
		else
			B[k++] <- A[j++]

	while(i <= q)
	do
		B[k++] <- A[i++]
	while(j <= r)
	do
		B[k++] <- A[j++]
	for i <- p to r
	do
		A[i] <- B[i]
```

![[Pasted image 20241113103316.png]]  
/// caption  
Merge Sort: Merge Phase  
///

### Analysis of Merge Sort

The `merge(A, p, q, r)` procedure runs in $\Theta(n)$, where $n = r − p + 1$, as its loops process each of the $n$ elements once.  
The `worst-case` running time of `mergeSort` is given by a recurrence relation.  
Let $T(n)$ denote this time for an array of size $n$.  
For $n=1$, $T(n)=1$.  
For $n>1$, `mergeSort` divides the array into two sub-arrays of sizes $\lfloor \frac n 2 \rfloor$ and $\lceil \frac n 2 \rceil$, sorts them recursively, and merges them in $n$ time, leading to the recurrence:  

$$T(n) = T\left(\left\lfloor \frac n 2 \right\rfloor\right) + T\left(\left\lceil \frac n 2 \right\rceil\right) + n$$

Therefore,

$$
T(n) = 
\begin{cases}
1 \quad \text{ if } n = 1, \\
T\left(\left\lfloor \frac n 2 \right\rfloor\right) + T\left(\left\lceil \frac n 2 \right\rceil\right) + n \quad \text{otherwise}
\end{cases}
$$

This is a `recurrence relation`, a recursively defined `function`.[^1]  
Let us expand the terms.

$$T(1) = 1$$

$$T(2) = T(1) + T(1) + 2 = 1 + 1 + 2 = 4$$

$$T(3) = T(2) + T(1) + 3 = 4 + 1 + 3 = 8$$

$$T(4) = T(2) + T(2) + 4 =4 +4 +4 =12$$

$$T(5) = T(3) + T(2) + 5 = 8 + 4 + 5 = 17$$

What is the pattern here?  
Let us consider the ratios $\frac {T(n)} n$ for the powers of $2$.  

$$\frac {T(1)}{1} = 1$$

$$\frac {T(2)}{2} = 2$$

$$\frac {T(4)}{4} = 3$$

This suggests  

$$\frac {T(n)} n = \log n + 1$$

$$\implies T(n) = n \log n + n$$

$$\implies \Theta(n \log n)$$

### The Iteration Method for Solving Recurrence Relations

The `floor` and `ceilings` are pain to deal with.  
If $n$ is assumed to be a power of $2$ such that $2^k = n$, this simplifies the recurrence to

$$
T(n) =
\begin{cases}
1 \quad \text{ if } n = 1, \\
2T\left(\frac n 2 \right) + n \quad \text{otherwise}
\end{cases}
$$

The iteration method turns this recurrence to `summation`.  

$$T(n) = 2 T \left(\frac n 2 \right) + n$$

$$= 2 \left(2 T \left(\frac n 4\right) + \frac n 2\right) + n$$

$$= 4 T\left(\frac n 4\right) + n + n$$

if $n$ is a power of $2$ such that $2^k = n$ then $k = \log_2 n$.  

$$T(n) = 2^kT\left(\frac n {2^k}\right) + (n + n + \ldots + n)$$

$$= 2^kT\left(\frac n {2^k}\right) + kn$$

$$= 2^{\log n}T\left(\frac n {2^{\log n}}\right) + n \log n$$

$$= n T(1) + n \log n$$

$$= n + n \log n$$

### Visualizing Recurrences Using the Recursion Tree

Iteration is a powerful method for solving recurrences, but it can be complex.  
A helpful way to visualize this is using a tree, where each recurrence expansion represents a deeper level.  
For `mergeSort`, we simplified the recurrence by assuming $n$ is a power of $2$, allowing us to drop floors and ceilings.

$$
T(n) =
\begin{cases}
1 \quad \text{ if } n = 1, \\
2T\left(\frac n 2 \right) + n \quad \text{otherwise}
\end{cases}
$$

In the recursion tree for `mergeSort`, each merge node is labeled with the time it takes to merge two lists.  
Merging two lists of size $\frac m 2$ into a list of size $m$ takes $\Theta(m)$ time.  
The recursion tree illustrates this process.  
![[Pasted image 20241113110432.png]]  
/// caption  
Merge Sort: Recurrence Tree  
///

### A Messier Example

$$
T(n) =
\begin{cases}
1 \quad \text{ if } n = 1, \\
3 T\left(\frac n 2\right) + n \quad \text{ otherwise}
\end{cases}
$$

Assume $n$ to be power of $4$. $n = 4^k$ and $k = \log_4n$  

$$T(n) = 3T\left(\frac n 4\right) + n$$

$$
= 3
\left(
3 T \left(
	\frac n {16}
	\right)
\right)
+ \left(
\frac n 4
\right)
+
n
$$

$$
=
9 T
\left(
	\frac n {16}
\right)
+
3
\left(
	\frac n 4
\right)
+
n
$$

$$
=
3^k T
\left(
\frac n {4^k}
\right)
+
3^{k - 1}
\left(
	\frac n {4 ^ {k - 1}}
\right)
+
\ldots
+
9
\left(
	\frac n {16}
\right)
+
3
\left(
	\frac n 4
\right)
+
n
$$

$$
=
3^kT
\left(
	\frac n {4^k}
\right)
+
\sum_{i = 0}^{k - 1}
\frac {3^i}{4^i} n
$$

With $n = 4^k$ and $T(1) = 1$

$$T(n) = 3^k T(\frac{n}{4^k}) + \sum_{i=0}^{k-1} \frac{3^i}{4^i} n$$

$$T(n) = 3^{\log_{4}n}T(1) + \sum_{i=0}^{(\log_{4}n)-1} \frac{3^i}{4^i}n$$

$$T(n) = n^{\log_{4}3} + \sum_{i=0}^{(\log_{4}n)-1} \frac{3^i}{4^i} n$$

$$T(n) = n^{\log_{4}3} + n \sum_{i=0}^{(\log_{4}n)-1} \left(\frac{3}{4}\right)^i$$

The `sum`[^2] is a `geometric series`.  
Recall that $x \ne 1$  

$$\sum_{i=0}^{m} x^i = \frac{x^{m+1}-1}{x-1}$$

In case of $x = \frac 3 4$ and $m = \log_4 n - 1$, we get  

$$T(n) = n^{\log_4 3} + n \frac{(\frac 3 4)^{\log_4 n + 1} - 1}{(\frac 3 4) - 1}$$

$$\left(\frac 3 4\right)^{\log_{4}n} = n^{\log_{4}(3/4)} = n^{\log_{4}3 - \log_{4}4} = n^{\log_{4}3 - 1}$$

$$= \frac {n ^ {\log_4 3}} n$$

Plugging it back, we get  

$$T(n) = n^{\log_{4}3} + n \frac{\frac{n^{\log_{4}3}}{n}-1}{(\frac 3 4)-1}$$

$$T(n) = n^{\log_{4}3} + \frac{n^{\log_{4}3} - n}{-\frac 1 4}$$

$$T(n) = n^{\log_{4}3} + 4(n - n^{\log_{4}3})$$

$$T(n) = 4n - 3n^{\log_4 3}$$

With $\log_4 3 \approx 0.79$, we have  

$$T(n) = 4n - 3n^{\log_4 3} \approx 4n - 3n^{0.79} \in \Theta(n)$$

## Selection Problem

The `rank` of an element in a `set`[^3] of $n$ numbers is its position in the sorted order, with the minimum rank being $1$ and the maximum being $n$.  
For the set $\{5,7,2,10,8,15,21,37,41\}$, the `rank` corresponds to each number's position when sorted.

| Position | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Number   | 2   | 5   | 7   | 8   | 10  | 15  | 21  | 37  | 41  |

Example: `rank` of $8$ is $4$.

Given a `set`[^3] $A$ of $n$ distinct numbers and an `integer` $k$, $1 \le k \le n$, output element of $A$ of `rank` $k$.

The `median` of a `set`[^3] is the element with `rank` $\frac {(n + 1)} 2$ for odd $n$, or the average of the two middle elements for even $n$.  
`Medians` are useful for measuring central tendency, especially in skewed distributions.  
For example, with 7 households earning 2000, 5000, 7000, 8000, 10000, 15000, and 16000, the `median` is 8000, while the average is 9000.  
If the highest income rises to 450,000, the `median` remains 8000, but the average increases to 71,000, demonstrating the `median`'s robustness.

The selection problem can be solved by sorting, but this requires $\Theta(n \log n)$ time.  
The challenge is to find a solution in $\Theta(n)$ time, and it is indeed possible, though not obvious.

### Sieve Technique

The sieve technique is a special case of `divide-and-conquer` where only one subproblem is solved.  
It applies to finding a single item from a set of $n$ items.  
After some analysis, we eliminate a significant fraction of the items that cannot be the desired value (e.g., $\frac n 2$, $\frac n 3$), and then recursively solve the problem on the remaining items.  
Each recursive step eliminates another fraction of the remaining `set`.[^3]

### Applying the Sieve to Selection

To apply the sieve technique to the selection problem, we start with the array $A[1 .. n]$ and select a `pivot` element $x$, chosen randomly.

We then _partition_ $A$ into 3 parts.

1. $A[q]$ contains the `pivot` element $x$.
2. $A[1 .. q - 1]$ will contain all the elements that are less than $x$.
3. $A[q + 1 .. n]$ will contains all elements that are greater than $x$.

![[Pasted image 20241113121351.png]]  
/// caption  
$A [p .. r]$ partitioned about the `pivot` $x$.  
///

### Selection Algorithm

The `rank` of the `pivot` $x$ is $q - p + 1$.  
If $k = \text{rank}(x)$, $x$ is the $k\text{-th}$ smallest.  
If $k < \text{rank}(x)$, search $A[p .. q - 1]$.  
If $k > \text{rank}(x)$, search $A[q + 1 .. r]$ and find the element of `rank` $(k - q)$, since $q$ smaller elements are eliminated.

```
select(array A, int p, int r, int k)
	if (p = r)
	then
		return A[p]
	else
		x <- choose_pivot(A, p, r)
		q <- partitian(A, p, r, x)
		rank_x <- q - p + 1
		if (k = rank_x)
		then
			return x
		if (k < rank_x)
		then
			return select(A, p, q - 1, k)
		else
			return select(A, q + 1, r, k - q)
```

![[Pasted image 20241113130859.png]]  
/// caption  
Sieve example: Select $6^{\text{th}}$ smallest element  
///

### Analysis of Selection

For now, we will assume that choosing `pivot` and partition takes $\Theta(n)$ time, without going into detail.  
If $x$ is the largest or smallest then we can eliminate only one element.

$$5, 9, 2, 6, 4, 1 , 3, 7$$

Selecting $1$ as `pivot` and after partition, we have  

$$1 , 5, 9, 2, 6, 4, 3, 7$$

Ideally, $x$ should be the `rank`, meaning not too small nor large.  
Assume we choose a `pivot` which causes one half of the array to be eliminated in each phase.  

$$
T(n) = 
\begin{cases}
	1 \quad \text{ if } n = 1, \\
	T\left(\frac n 2\right) + n \quad \text{otherwise}
\end{cases}
$$

If we expand, we get  

$$T(n) = n + \frac n 2 + \frac n 4 + \ldots$$

$$\le \sum_{i=0}^{\infty} \frac{n}{2^i}$$

$$= n \sum_{i=0}^{\infty} \frac{1}{2^i}$$

For infinite `geometric series`, $|c| < 1$  

$$\sum_{i=0}^{\infty} c^i = \frac{1}{1-c}$$

$$T(n) \le 2n \in \Theta(n)$$

The $\Theta(n)$ selection algorithm may require up to $\log n$ passes.  
However, eliminating a constant fraction of the array each phase leads to a convergent geometric series, proving the total runtime is _linear_.  
This highlights that linear time can be achieved in unexpected ways.

## References

[^1]: Read more about [[notes_publisher/docs/Mathematics/Function/Content|functions]].
[^2]: Read more about [[notes_publisher/docs/University Notes/semester 1/MTH101 - Calculus and Analytical Geometry/27. Sigma Notation/Lecture|summation]].
[^3]: Read more about [[notes_publisher/docs/Mathematics/Set/Content|sets]].