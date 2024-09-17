# Introduction
It is a software system used for typesetting documents.  
Although there do exist online solutions, if you want to use it **offline** along with [VS Code](https://code.visualstudio.com/download), consider downloading [Tex Live](https://www.tug.org/texlive/).  
Also install the `LaTeX WorkShop Extension`.  
The language it uses it called **TeX**.

## Basic Structure

```tex
\documentclass{article}
% preamble area
\begin{document}
	Hello World.
\end{document}
```

## Basic Syntax

```tex
%This is a comment
```

```
\command[optional parameters]{required parameters}
```

```tex
\begin{environment}
\end{environment}
```

Environments are areas within your document. They can be nested and should be closed as they were opened.

The **Correct** way.

```tex
\begin{environment1}
	\begin{environment2}
	\end{environment2}
\end{environment1}
```

The **Wrong** way.

```tex
\begin{environment1}
	\begin{environment2}
	\end{environment1}
\end{environment2}
```

Some of the features come through packages.

```tex
\usepackage[optional parameters]{package_name}
```

Rest of the sections will be discussed in other nodes.
