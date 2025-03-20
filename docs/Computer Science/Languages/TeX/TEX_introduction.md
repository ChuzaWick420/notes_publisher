# Introduction

> [!QUOTE]- [Wikipedia](https://en.wikipedia.org/wiki/LaTeX)  
> $\LaTeX$ is a software system for typesetting documents. It uses a macro language called `tex`.

## Installation

### Online

- [Overleaf](https://www.overleaf.com/)

### Offline

Your `tex` code goes inside files with extension `.tex`.  
To produce `PDF` files from these files, you will need a `tex` distribution installed on your system.  
Some popular options are:

- [Tex Live](https://www.tug.org/texlive/)
- [MikTex](https://github.com/MiKTeX/miktex)

> [!TIP] For [VS Code](https://code.visualstudio.com/download), use the `LaTeX WorkShop` extension.

## Syntax

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

![[tex_e_environment_nesting.svg]]

## Basic Structure

```tex
\documentclass{document_class}
% preamble area
% document appearance control commands goes here
\begin{document}
	Hello World.
	% document content goes here
\end{document}
```

Following table is present on [Wikipedia](https://en.wikibooks.org/wiki/LaTeX/Document_Structure#Document_classes)

| Class      | Description                                                                                                                         |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `article`  | For articles in scientific journals, presentations, short reports, program documentation, invitations, …                            |
| `IEEEtran` | For articles with the IEEE Transactions format.                                                                                     |
| `proc`     | A class for proceedings based on the article class.                                                                                 |
| `minimal`  | It is as small as it can get. It only sets a page size and a base font. It is mainly used for debugging purposes.                   |
| `report`   | For longer reports containing several chapters, small books, thesis, …                                                              |
| `book`     | For books.                                                                                                                          |
| `slides`   | For slides. The class uses big sans serif letters.                                                                                  |
| `memoir`   | For sensibly changing the output of the document. It is based on the `book` class, but you can create any kind of document with it. |
| `letter`   | For writing letters.                                                                                                                |
| `beamer`   | For writing presentations (see _LaTeX/Presentations_).                                                                              |

## Additional Features

The document can contain additional features, for which we need to use `#!tex \usepackage` command.

```tex
\usepackage[optional parameters]{package_name}
```
