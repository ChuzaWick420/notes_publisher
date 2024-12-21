# Meta Tables

```lua
tab_1 = {
	key_1 = 5,
	key_2 = 7,
}

meta_tab = {
	__add = function(tb1, val)
		local dumb = {
			key_1 = tb1.key_1 + val,
			key_2 = tb1.key_2 + val,
		}
		return dumb
	end,
}

setmetatable(tab_1, meta_tab)

sum = tab_1 + 2

for key, val in pairs(sum) do
	print(key, val)
end
```

In the example above, we have a `table` called `tab_1` and another `table` called `meta_tab`.  
This `meta_table` has a method called `__add()` which takes a `table` as its first argument  
and another second argument.  
After that, we set it as `meta table` for `tab_1`.  
Doing so, allows `tab_1` to execute `__add()` when it encounters a `+` operator.  
As a result, the section

```lua
tab_1 + 2
```

evaluates to the `table` returned by `__add()` which is `dumb`.

Here is another example which adds 3 `tables`.

```lua
tab_1 = {
	key_1 = 5,
	key_2 = 7,
}

tab_2 = {
	key_1 = 2,
	key_2 = 1,
}

tab_3 = {
	key_1 = 3,
	key_2 = 2,
}

meta_tab = {
	__add = function(tb1, tb2)
		local tab = {}
		tab.key_1 = tb1.key_1 + tb2.key_1
		tab.key_2 = tb1.key_2 + tb2.key_2
		return tab
	end,
}

setmetatable(tab_1, meta_tab)
setmetatable(tab_2, meta_tab)
setmetatable(tab_3, meta_tab)

sum = tab_1 + tab_2 + tab_3

for key, val in pairs(sum) do
	print(key, val)
end
```

This is similar to `operator overloading`.

| **Metamethod**    | **operator**      |
|-------------------|-------------------|
| `__add(a, b)`     | `a + b`           |
| `__sub(a, b)`     | `a - b`           |
| `__mul(a, b)`     | `a * b`           |
| `__div(a, b)`     | `a / b`           |
| `__mod(a, b)`     | `a % b`           |
| `__pow(a, b)`     | `a ^ b`           |
| `__unm(a)`        | `-a`              |
| `__concat(a, b)`  | `a .. b`          |
| `__len(a)`        | `#a`              |
| `__eq(a, b)`      | `a == b`          |
| `__lt(a, b)`      | `a < b`           |
| `__le(a, b)`      | `a <= b`          |
| `__index(a, b)`   | `a.b`             |
| `__newindex(a,b,c)` | `a.b = c`     |
| `__call(a, …)`  | `a(…)`          |
