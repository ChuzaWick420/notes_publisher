You can do `vector graphics` by using:

```tex
\usepackage{tikz}
```

The environment is uses is:

```tex
\begin{tikzpicture}
	
\end{tikzpicture}
```

to draw something, we use `\draw` command (or `\filldraw`):

```tex
\draw[OPTIONS] (START_COORDS) SHAPE (END_COORDS);
```

The `OPTIONS` include:
1. color
2. style
3. thickness

# Colors
1. white
2. black
3. red
4. green
5. blue
6. cyan
7. magenta
8. yellow

# Thickness
1. ultra thin
2. very thin
3. thin
4. thick
5. very thick
6. ultra thick

if you want to add text to the `END_COORDS` point, you can do so by doing:

```tex
\draw[OPTIONS] (START_COORDS) SHAPE (END_COORDS) node[anchor=POS_OF_POINT] {TEXT_TO_SHOW};
```

# Examples

```tex
\draw[red, dashed] (0, 0) rectangle (2, -2) node[anchor=north west, blue] {Hello};
```

![[Pasted image 20240404174511.png]]

```tex
\draw[red, dashed, ultra thick] (0, 0) circle (2);
```

![[Pasted image 20240404174839.png]]

---

# Nodes

```tex
% preamble
\usetikzlibrary{positioning}
% doc starts

\begin{tikzpicture}[
NODE_TYPE/.style={SHAPE, draw=COLOR!INTENSITY, fill=COLOR!INTENSITY, THICKNESS, minimum size=WIDTH},
]
	\node[NODE_TYPE] (NODE_NAME_1)                       {NODE_LABEL};
	\node[NODE_TYPE] (NODE_NAME_2) [below of=NODE_NAME_1]{NODE_LABEL};

	\draw[->] (NODE_NAME.DIRECTION) -- (NODE_NAME.DIRECTION);
\end{tikzpicture}
```

Let me explain those placeholders now.
- `NODE_TYPE` are the identifiers you assign to uniquely identify the nodes in dealing with `\node`.
- `NODE_NAME_1` is the name you assign to node and is used in dealing with `\draw` statement.
- `SHAPE` can be `circle`, `rectangle` etc.
- `THICKNESS` can be:
	- `ultra thin`
	- `very thin`
	- `thin`
	- `thick`
	- `very thick`
	- `ultra thick`
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
