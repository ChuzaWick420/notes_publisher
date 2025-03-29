# Colors

We can define colors by using `#!tex \definecolor`.

```tex
\usepackage{xcolor}
\definecolor{NAME}{HTML}{VALUE} % (1)!
```

1. `NAME` defines the macro name, it will be replaced with the `VALUE` (a 6 digit `hex` number). The `HTML` just defines the format for the values.

## Example

```tex
\documentclass{article}
\usepackage{xcolor}

\definecolor{test}{HTML}{444400}

\begin{document}

\colorbox{test}{Hello world} % First parameter is a color

\end{document}
```