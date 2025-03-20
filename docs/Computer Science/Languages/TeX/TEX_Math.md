# Math

All the symbols can be found [here](http://mirrors.ctan.org/info/symbols/comprehensive/symbols-a4.pdf).

## Inline

For inline structure, the equation needs to be enclosed within `#!tex $` delimiter.

```tex
$\int_a^b f^{\prime}(x)dx = f(x)$
```

And it produces result: $\int_a^b f^{\prime}(x)dx = f(x)$

## Block

These equations take the whole line.

### With Equation Numbers

```tex
\begin{equation}
	\int_a^b f^{'}(x)dx = f(x)
\end{equation}
```

![[Pasted image 20240402232017.png]]  
/// caption  
Equation with equation number  
///

### Without Equation Numbers

Similar to [inline](#inline) version, the equation needs to be enclosed within `$$` delimiters.

```tex
$$\int_a^b f^{\prime}(x)dx = f(x)$$
```

Produces the result:  

$$\int_a^b f^{\prime}(x)dx = f(x)$$

Alternatively, you can use 

```tex
\usepackage{amsmath}

\begin{equation*}
% Equation here
\end{equation*}
```

## Structures

When only _one character_ is required for argument to a command, there is no need for $\{\}$.

### Fractions

```tex
\frac{numerator}{denominator}
```

#### Example

```tex
\frac{1}{2}
% or \frac 1 2
```

Produces:

$$\frac 1 2$$

### Matrices

```tex
\begin{matrix}
	1 & 0\\ % \\ is used for new line
	0 & 1
\end{matrix}
```

Produces:

$$
\begin{matrix}
	1 & 0\\
	0 & 1
\end{matrix}
$$

```tex
\begin{bmatrix}
	1 & 0\\ % \\ is used for new line
	0 & 1
\end{bmatrix}
```

Produces:

$$
\begin{bmatrix}
	1 & 0\\
	0 & 1
\end{bmatrix}
$$

```tex
\begin{vmatrix}
	1 & 0\\ % \\ is used for new line
	0 & 1
\end{vmatrix}
```

Produces:

$$
\begin{vmatrix}
	1 & 0\\
	0 & 1
\end{vmatrix}
$$

### Subscript

The `#!tex _` is used for subscript.

#### Example

```tex
\sum_{i = 0}
```

Produces:

$$
\sum_{i= 0}
$$

### Superscript

The `#!tex ^` is used for subscript.

#### Example

```tex
\sum^\infty
```

Produces:

$$
\sum^\infty
$$