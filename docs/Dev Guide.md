# Dev Guide

## Terminologies

### Figures (scripted)

`Matplotlib` generated 3d diagrams using `python`.

### Diagrams (Excalidrawings)

`Excalidraw` drawings.

### Imgs

Raw images

# Other Constraints

- Use enumeration for notes with uniform digits, such as starting from `01. name` if course ends within `99` lectures.
- Use headings to name files within the site, instead of file names.
	- Headings for display
	- file names for usage within project
		- Capitalized course codes in name
- Just like file names, use names for visual aids as well.
- Use `![[img_path]]{id="img_id"}` to refer to a figure in current document
	- Follow `Figure: x.y` where `x` is lecture or chapter number and `y` is the number of figure
	- Excalidrawings will use `coursecode_e_x_y` format
	- Imgs will use `coursecode_i_x_y` format
	- Scripted will use `coursecode_f_x_y` format
	- Use svgs generated from excalidraw within notes