# Tables

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

You can access `keys` using the `dot` notation like `object oriented programming`.

```lua
str = dict.key1
```

You can change values of existing `keys`.

```lua
dict.key2 = false
```

And you can register new `keys` as well

```lua
dict.newKey = 420
```