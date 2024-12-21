The bibliographic information is stored inside a `.bib` file.  
The format of the information is as such:

```
@BOOK{KEY_NAME:1,
AUTHOR=    "John Doe",
TITLE=     "The Book without Title",
PUBLISHER= "Dummy Publisher",
YEAR=      "2100",
}
```

or

```
@BOOK{KEY_NAME:1,
AUTHOR=    {John Doe},
TITLE=     {The Book without Title},
PUBLISHER= {Dummy Publisher},
YEAR=      {2100},
}
```

You can then create a `citation` by doing:

```tex
\cite{KEY_NAME:1}
```

> Note: your `value` of the `key` has to be in order, meaning you cannot use a `key` with `value` `2` before using the one with `value` `1`.

```tex
\begin{document}
\bibliography{file_name}
\bibliographystyle{style_name}
\end{document}
```

If you want your `citations` to appear in `footnotes` then you can use:

```tex
\usepackage[backend=bibtex, style=verbose-trad2]{biblatex}
\bibliography
\begin{document}
	\autocite[page_number]{KEY:VALUE}
\end{document}
```

>Note: your `bibliography` command has to be in `preamble` area.

If you want to print the `bibliography` now, you can use `\printbibliography` command inside the `document` environment.
