# About this project
## Primary Goals
Following are the primary goals for this project.
1. Act as knowledge vault for myself.
2. Allow others to benefit from my knowledge.

## How it works
I write my notes with [obsidian](https://obsidian.md/).  
I write the 2D diagrams with [LaTeX](https://www.latex-project.org/).  
I write the 3D diagrams with `python`.  
After writing my notes, I use `git` to commit and push to this repository.  
After changes have been pushed, `Github Actions` spins up a `linux` machine to run my `./github/workflows/ci.yml` file.  
The `ci.yml` file tells the machine to:
- Use `mkdocs` to generate a website based on my notes.
- Use `pygments` to syntax highlight the code blocks.
- Run a `bash script` which runs my `python` scripts, responsible for generating the `HTML` pages for the 3D diagrams which later get linked to my notes using `iframes`.
