# Figures

`Figures` can be used in two different ways:

- non-wrap
- wrap

## Non-wrap

You can use:

```tex
\usepackage{graphicx}
\begin{document}
	\begin{figure}[FLOAT_VALUE]
		\includegraphics[width=UNIT]{IMAGE_PATH}
		\caption{CAPTION_TO_APPEAR_UNDER_IMAGE}
		\label{LABEL_TO_BE_REFERED}
	\end{figure}
\end{document}
```

The `float values` are used to control where the figure appears within the document. Counter intuitively, the `figures` inside the document don't appear in correspondence to their code's position.

Following are the `float values`:

- `h` - same location as in code.
- `t` - top of the page.
- `b` - bottom of the page.
- `p` - on an extra page.
- `!` - override, will force the specified location.

## Wrap

```tex
\usepackage{wrapfig}
```

```tex
\begin{wrapfigure}{LOCATION}{WIDTH}
\end{wrapfigure}
```

The `LOCATION` parameter can be `r` for `right` or `l` for `left`.

---

## Subfigures

```tex
\usepackage{subcaption}
```

```tex
\begin{figure}
	\begin{subfigure}[FLOAT_VALUE]{WIDTH}
		\includegraphics[width=WIDTH_RELATIVE_TO_SUBFIG]{IMAGE_PATH}
	\end{subfigure}
\end{figure}
```

---

## List of Figures

```tex
\begin{appendix}
	\listoffigures
\end{appendix}
```
