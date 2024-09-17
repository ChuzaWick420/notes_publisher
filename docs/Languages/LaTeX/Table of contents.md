`Table of contents` can be printed by:

```tex
\begin{document}
\tableofcontents
\end{document}
```

What will be shown in the table depends on the `depth` that has been set.

| depth_value | included       |
| ----------- | -------------- |
| 1           | sections       |
| 2           | subsections    |
| 3           | subsubsections |
| 4           | paragraphs     |
| 5           | subparagraphs  |

the `depth` can be set by doing something like:

```tex
% preamble area
\setcounter{tocdepth}{value}
```

![[Pasted image 20240403001311.png]]

if the spacing between the contents of the table is annoying, you can use:

```tex
\usepackage{setspace}

\begin{document}
\doublespacing
\tableofcontents
\singlespacing
\end{document}
```

it will look something like this:  
![[Pasted image 20240403001254.png]]
