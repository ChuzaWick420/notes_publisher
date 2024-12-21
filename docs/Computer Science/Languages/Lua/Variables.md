# Variables

```lua
variable = "value"
```

There are no `data types` in `lua`.  
The `variables` are dynamic.

## Scoping

By default, `variables` are `global`.  
To localize them inside a `block`, you will need a `local` keyword.

```lua
g_var = "hi" -- this is a global variable and is accessible inside and outside the functions

function fun ()
	local l_var = "bye"
	print(g_var) -- accessible here
	print(l_var) -- accessible here
end


print(g_var) -- accessible here
print(l_var) -- not accessible here, it is `nil` here

```