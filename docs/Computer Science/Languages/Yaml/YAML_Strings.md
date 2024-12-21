# Strings

## Single Quote

```yaml
key: 'I am value'
```

## Double Quotes

```yaml
key: "I am value"
```

### Blocks

### Literal Block

Returns `\n` inside the `string` with newlines.

```yaml
key: |
This is begining of the block
	Continues but indentation for this line is stripped
		This line keeps its left over identation after being stripped
	This line is not included since it is de-indented.
```

### Folded Block

Replaces `\n` by `space` characters (` `).

```yaml
key: >
This is beginning of block

The blank line above this results into newline character
	And indented line like this also gets to keep newlines 
	characters.
```

### Strip

Stripes the trailing blank lines.

```yaml
key: |-
value
```

```yaml
key: >-
value
```

### Keep

Keeps the trailing blank lines.

```yaml
key: |+
value
```

```yaml
key: >+
value
```