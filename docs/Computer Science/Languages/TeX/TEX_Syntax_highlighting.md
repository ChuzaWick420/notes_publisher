# Syntax Highlighting

## Setup

### Package

```tex
\usepackage{listings}
```

### Definition

```tex
\lstdefinestyle{CUSTOM_STYLE_NAME}{
	language=c++ % could be any language
	numbers=left,
	tabsize=4,
	keywordstyle=\color{COLOR},
	commentstyle=\color{COLOR},
	basicstyle=\ttfamily\color{COLOR},
	stringstyle=\color{COLOR},
	backgroundcolor=\color{COLOR},
	showstringspaces=false
}
```

### Usage

```tex
\begin{lstlisting}[style=CUSTOM_NAME_DEFINED_IN_DEFINITION]
	#include <iostream>
	int main () {
		std::cout << "Hello World!" << std::endl;
		return 0;
	}
\end{lstlisting}
```