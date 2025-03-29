# Graphs

You can do `vector graphics` by using:

```tex
\usepackage{tikz}
```

```tex
\begin{tikzpicture}
\end{tikzpicture}
```

to draw something, we use `#!tex \draw` command (or `\filldraw`):

```tex
\draw[OPTIONS] (START_COORDS) SHAPE (END_COORDS);
```

The `OPTIONS` include:

1. color
2. style
3. thickness

## Colors

1. white
2. black
3. red
4. green
5. blue
6. cyan
7. magenta
8. yellow

## Thickness

1. ultra thin
2. very thin
3. thin
4. thick
5. very thick
6. ultra thick

## Nodes

> [!NOTE] The capitalized words in the following code block are placeholders which I will describe afterwards.

```tex
% preamble
\usetikzlibrary{positioning}
% doc starts

\begin{tikzpicture}[
NODE_TYPE/.style={SHAPE, draw=COLOR!INTENSITY, fill=COLOR!INTENSITY, THICKNESS, minimum size=WIDTH},
]
	\node[NODE_TYPE] (NODE_NAME_1)                       {NODE_LABEL};
	\node[NODE_TYPE] (NODE_NAME_2) [below = of NODE_NAME_1]{NODE_LABEL};

	\draw[->] (NODE_NAME.DIRECTION) -- (NODE_NAME.DIRECTION);
\end{tikzpicture}
```

Let me explain those placeholders now.

- `NODE_TYPE` is assigned to each node, to identify its type (appearance).
- `SHAPE` can be `circle`, `rectangle` etc.
- `DIRECTION` can be:
	- `east`
	- `west`
	- `north`
	- `south`
	- `north east`
	- `north west`
	- `south east`
	- `south west`
- `--` defines a `line`.
- `->` tells the line has to be pointed.

## Examples

```tex
\draw[red, dashed] (0, 0) rectangle (2, -2) node[anchor=north west, blue] {Hello};
```

![[Pasted image 20240404174511.png]]

```tex
\draw[red, dashed, ultra thick] (0, 0) circle (2);
```

![[Pasted image 20240404174839.png]]

```tex
\begin{tikzpicture}[
roundnode/.style={circle, draw=green!60, fill=green!5, very thick, minimum size=7mm},
squarednode/.style={rectangle, draw=red!60, fill=red!5, very thick, minimum size=5mm},
]
%Nodes
\node[squarednode]      (maintopic)                              {2};
\node[roundnode]        (uppercircle)       [above=of maintopic] {1};
\node[squarednode]      (rightsquare)       [right=of maintopic] {3};
\node[roundnode]        (lowercircle)       [below=of maintopic] {4};

%Lines
\draw[->] (uppercircle.south) -- (maintopic.north);
\draw[->] (maintopic.east) -- (rightsquare.west);
\draw[->] (rightsquare.south) .. controls +(down:7mm) and +(right:7mm) .. (lowercircle.east);
\end{tikzpicture}
```

![[Pasted image 20250329212859.png]]