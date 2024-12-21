# About this project
## Primary Goals

Following are the primary goals for this project.
1. Act as knowledge vault for myself.
2. Allow others to benefit from my knowledge.

### Working time
[![wakatime](https://wakatime.com/badge/user/47e86f1b-ec2f-4c40-9f16-c1e58403c114/project/681a6bfe-d0ed-4350-bc28-5e4580f6c968.svg)](https://wakatime.com/badge/user/47e86f1b-ec2f-4c40-9f16-c1e58403c114/project/681a6bfe-d0ed-4350-bc28-5e4580f6c968)

## How it works
I write  
- my notes with [obsidian](https://obsidian.md/) or [NeoVim](https://neovim.io/).  
- 2D diagrams with [LaTeX](https://www.latex-project.org/) or `Excalidraw`.  
- 3D diagrams with `python`.  
After writing my notes, I use `git` to commit and push to this repository.  
After changes have been pushed, `Github Actions` spins up a `linux` machine to run instructions listed in `./github/workflows/ci.yml`.  
The `ci.yml` file tells the machine to:
- Use `mkdocs` to generate a website based on my notes.
- Use `pygments` to syntax highlight the code blocks.
- Run a `bash script` which runs my `python` scripts, responsible for generating the `HTML` pages for the 3D diagrams which later get linked to my notes using `iframes`.
- Host the website on `Github Pages`.

## References
- https://github.com/jobindjohn/obsidian-publish-mkdocs
