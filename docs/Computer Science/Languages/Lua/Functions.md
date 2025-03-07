# Functions

## Normal

```lua
function name (arg)
	-- function body
	return 1 + 2 -- returining values is optional
end
```

```lua
name = function (param) print (param) end
```

`Functions` can return multiple values.

```lua
function name (arg)
	return 1, 2, 3, 4
end
```

The following are the same `functions`.

```lua
function log(x)
	print(x)
end

log = function(x) print(x) end
```

## Higher order Functions

### Taking Function as Argument

```lua
function name (para)
	para("hi")
end

name(print)
```

### Returning Functions

```lua
function name () 
	return function (value) print (value) end
end

name()("hi")
```

## Working with Tables

```lua
function name (table)
	print(table.key)
end

name({key = 69}) -- valid
name{key = 69}   -- valid
```