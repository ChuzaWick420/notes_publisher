# Normal

```lua
function name (arg)
	-- function body
	return 1 + 2 -- returining values is optional
end
```

```lua
name = function (param) print (param) end
```

# Higher Order Functions

## Taking Function as Argument

```lua
function name (para)
	para("hi")
end

name(print)
```

## Returning Functions

```lua
function name () 
	return function (value) print (value) end
end

name()("hi")
```
