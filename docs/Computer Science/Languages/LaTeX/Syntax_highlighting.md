Syntax highlighting can be achieved by using:

```tex
\usepackage{listings}
```

Then to use it, we can do:

```tex
\begin{lstlisting}[language=c++]
	#include <iostream>
	int main () {
		std::cout << "Hello World!" << std::endl;
		return 0;
	}
\end{lstlisting}
```

But first, we have to set it up:

```tex
\lstdefinestyle[CUSTOM_STYLE_NAME]{
	numbers=left,
	tabsize=4,
	keywordstyle=\color{COLOR},
	commentstyle=\color{COLOR},
	basicstyle=\ttfamily\color{COLOR},
	stringstyle=\color{COLOR},
	showstringspaces=false
}
```

Then:

```tex
\lstset{CUSTOM_STYLE_NAME_IN_DEFINITION}
```

to use `\color` command, you must include:

```tex
\usepackage{color}
```

You can also use:

```tex
\usepackage{xcolor}
```

to define your own color, such as:

```tex
\definecolor{CUSTOM_COLOR_NAME}{COLOR_SCHEME}{COLOR_VALUE}
```
