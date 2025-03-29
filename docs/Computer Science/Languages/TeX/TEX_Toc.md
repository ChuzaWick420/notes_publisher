# Table of Contents

`Table of contents` can be printed by:

```tex
\begin{document}
	\tableofcontents
\end{document}
```

## Depth

| depth_value | included sections |
| ----------- | ----------------- |
| 1           | sections          |
| 2           | subsections       |
| 3           | subsubsections    |
| 4           | paragraphs        |
| 5           | subparagraphs     |

```tex
% preamble area
\setcounter{tocdepth}{value} % setting depth value
```

![[Pasted image 20240403001311.png]]  
/// caption  
`depth` value set to $3$.  
///

```tex
\usepackage{setspace}

\begin{document}
	\doublespacing
	\tableofcontents
	\singlespacing
\end{document}
```

![[Pasted image 20240403001254.png]]  
/// caption  
Spacing within sections.  
///