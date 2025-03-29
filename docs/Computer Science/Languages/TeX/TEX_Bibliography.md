# Bibliography

The bibliographic information is stored inside a `.bib` file.  

## Format

Format is as such:

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

> [!NOTE] The capitalized words in above example can be small cased as well.

```tex
\begin{document}
	\bibliography{file_name}
	\bibliographystyle{style_name}
\end{document}
```

> [!BUG]  
> Unsure about behaviors in other cases but if you are using [vimtex](https://github.com/lervag/vimtex) and you are having issues with compilation, try following steps:
> - Stop compilation
> - Remove related files, other than `.bib` and `.tex` files.
> - Open file and try compiling again

## Citation

You can then create a `citation` by doing:

```tex
\cite{KEY_NAME:1}
```

> [!NOTE]- Potential mistake regarding citations  
> Citations have to appear in an order. For example, you _must_ use `#!tex \cite{KEY_NAME:1}` before using `#!tex \cite{KEY_NAME:2}`.

### Inside Footnotes

If you want your `citations` to appear in `footnotes` then you can use:

```tex
\usepackage[backend=bibtex, style=ieeetr]{biblatex}
\bibliography{file_name}
\begin{document}
	\autocite{KEY:VALUE}
	\printbibliography
\end{document}
```

> [!NOTE]- When using `biblatex`  
> The `#!tex \bibliography{file_name}` has to be in preamble area. Additionally, you may use `#!tex \printbibliography` to print the references.
