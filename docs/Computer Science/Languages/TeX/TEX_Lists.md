# Lists

## Ordered

```tex
\begin{enumerate}
	\item Item_1
	\item Item_2
\end{enumerate}
```

## Unordered

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

### Bullets

The style of `bullets` can be changed using:

```tex
\usepackage{enumitem}
```

#### Default Labels

```tex
\begin{enumerate}[label=(roman*)]
\end{enumerate}
```

- `(\roman*)`
- `\arabic*)`
- `\alph*)`  


![[Pasted image 20240404151209.png]]

#### Custom Labels

You can also change the bullets of each unique `item` to whatever you want:

```tex
\item[$-$]
\item[$\ast$]
```

Also,

```tex
\usepackage{pifont}
\item[\ding{CHARACTER_CODE}]
```

![[Pasted image 20240404152055.png]]  
/// caption  
Characters Codes for reference  
///

If you don't want to keep writing the code for each `item` separately, you can also use:

```tex
\renewcommand{\labelitemi}{CHARACTER_TO_SHOW}
```

to globally change the bullets shown by `\item` command.

> [!TIP]
> - For nested level 1, use `#!tex \labelitemi`.
> - For nested level 2, use `#!tex \labelitemii`.
> - For nested level 3, use `#!tex \labelitemiii`.
