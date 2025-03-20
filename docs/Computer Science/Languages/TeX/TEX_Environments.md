# Environments

There are quite a lot of useful environments.  

## Align

```tex
\usepackage{amsmath}

\begin{align*}
	2 + 2 &= 4 \\
	4 &= 2 + 2
\end{align*}
```

The `&` is the alignment character.

$$
\begin{align}
	2 + 2 &= 4 \\
	4 &= 2 + 2
\end{align}
$$

## Array

This environment needs to be nested within a math environment, such as `#!tex $$`.

```tex
\begin{array}{ccc}
	2 &= &2 \\
	4 &= &4
\end{array}
```

The `&` _divides_ the equation like slices.  
The $\{ccc\}$ means 3 characters which are _centered_.  
Alternatively, we can write $r$ for _right_ and $l$ for _left_.

$$
\begin{array}{ccc}
	2 &= &2 \\
	4 &= &4
\end{array}
$$