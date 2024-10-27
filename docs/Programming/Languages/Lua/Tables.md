# Tables

## Defining

You can have a `table` with normal `keys` as follows

```lua
dict = {
	key1 = "Hi",
	key2 = false,
	key3 = 69,
	key4 = function()
		print("Hello World from function")
	end,
}
```

You can also have other `non nil` values as `keys`

```lua
dict = {
	["str_key"] = "string key",
	[420] = "numeric key",
}
```

## Accessing

You can access `keys` using the `dot` notation like `object oriented programming`.  
But this works for `keys` which are defined as `identifiers`.

```lua
str = dict.key1
```

You can also access it like `javascript`.  

```lua
str = dict["key1"]
```

## Modifying

You can change values of existing `keys`.

```lua
dict.key2 = false
```

## Adding

And you can register new `keys` as well

```lua
dict.newKey = 420
```

## Iteration

```lua
for key, val in pairs(table) do
	print(key, val)
end
```

## Special Table

There is a special `table` which tracks your `global` objects, including the `global` objects you create.

```lua
_G
```

```lua
x = 69

function greet()
	print("Hello World")
end

for key, value in pairs(_G) do
	print(key, value)
end
```
