`Figures` can be used in two different ways:
- non-wrap
- wrap

# Non-wrap
You can use:

```tex
\usepackage{graphicx} %for \includegraphics
\begin{figure}
	\includegraphics[width=UNIT]{IMAGE_PATH}
	\caption{CAPTION_TO_APPEAR_UNDER_IMAGE}
	\label{LABEL_TO_BE_REFERED}
\end{figure}
```

`LaTeX` will try to move the image where it finds it good.  
For example: if the image cannot be fit into the current page, it will be moved onto the next page.  
Resulting into the result of code (written _after_ the image code) to appear before the image itself.

to manipulate the positioning of image, you can use `float values`.

```tex
\begin{figure}[FLOAT_VALUE]
```

Following are the `float values`:
- h - same location as in code.
- t - top of the page.
- b - bottom of the page.
- p - on an extra page.
- ! - override, will force the specified location.

# Wrap
For `wrap` figure, you need:

```tex
\usepackage{wrapfig}
```

It uses `wrapfigure` environment:

```tex
\begin{wrapfigure}{LOCATION}{WIDTH}
\end{wrapfigure}
```

The `LOCATION` parameter can be `r` for `right` or `l` for `left`.

---

There is another additional environment which is used alongside `figures`:

```tex
\begin{center}
\end{center}
```

Alternative to that is to just use:

```tex
\centering
```

---

## Subfigures
You have to use:

```tex
\usepackage{subcaption}
```

The `subfigures` are part of `figure` environment:

```tex
\begin{figure}
	\begin{subfigure}[FLOAT_VALUE]{WIDTH}
		\includegraphics[width=WIDTH_RELATIVE_TO_SUBFIG]{IMAGE_PATH}
	\end{subfigure}
\end{figure}
```

---

You can also use:

```tex
\begin{appendix}
	\listoffigures
\end{appendix}
```
