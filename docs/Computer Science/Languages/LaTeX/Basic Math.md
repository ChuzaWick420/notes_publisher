This note covers:
- Inline Math
- Equations
- Fractions
- Matrices

# Inline
The math syntax is enclosed between `$`.

```tex
$\int_a^b f^{'}(x)dx = f(x)$
```

produces result:  
$\int_a^b f^{'}(x)dx = f(x)$

# Equation
You can write equations which take the whole line.

```tex
\begin{equation}
	\int_a^b f^{'}(x)dx = f(x)
\end{equation}
```

produces result:  
![[Pasted image 20240402232017.png]]

Notice the `(1)` on the side.  
if you want to remove it, you can use:

```tex
\usepackage{amsmath}
%--
\begin{equation*}
%--
\end{equation*}
%--
```

# Fractions
Just like other math structures, this one is also a structure.

```tex
\frac{numerator}{denominator}
```

# Matrices
you can make matrices using the `matrix` environment (either inside `equation` environment or `inline` mode).

```tex
\begin{matrix}
	1 & 0\\
	0 & 1
\end{matrix}
```

The `\\` is used for `new line`.  
It produces the result:  
![[Pasted image 20240402232803.png]]  
and for the `[]` around the entries, you can do:

```tex
\left[
\begin{matrix}
%--
\end{matrix}
\right]
```

the `left` and `right` make sure the parenthesis _scale_ up according to whatever is enclosed.
