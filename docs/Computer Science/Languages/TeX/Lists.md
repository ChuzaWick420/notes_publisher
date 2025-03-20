There are 2 types of `lists`:
- Ordered
- Unordered

# Ordered

```tex
\begin{enumerate}
	\item Item_1
	\item Item_2
\end{enumerate}
```

# Unordered

```tex
\begin{itemize}
	\item Item_1
	\item Item_2
\end{itemize}
```

---

The `lists` can be nested as such:

```tex
\begin{enumerate}
	\item One
	\begin{enumerate}
		\item Two
		\item Three
		\item Four
	\end{enumerate}
	\item Five
	\item Six
\end{enumerate}
```

![[Pasted image 20240404151605.png]]

## Bullets
The style of `bullets` can be changed using:

```tex
\usepackage{enumitem}
```

Then chose the `list` type you want and append `[label=TYPE]`:

```tex
\begin{enumerate}[label=(roman*)]
\end{enumerate}
```

---
You can also change the bullets of each `item` to whatever you want:

```tex
\item[$-$]
\item[$\ast$]
\item[$\CHARACTER$]
```

![[Pasted image 20240404152055.png]]  
You can use `\item[\ding{CODE}]` to use the corresponding `bullet`.  
If you don't want to keep writing the code for each `item` separately, you can also use:

```tex
\renewcommand{\labelitemi}{CHARACTER_TO_SHOW}
```

to globally change the bullets shown by `\item` command.

>Note: `\labelitemi` is the first nested level. The 2nd nested level would be `\labelitemii`.

## Labels
- `(\roman*)`
- `\arabic*)`
- `\alph*)`  
![[Pasted image 20240404151209.png]]
