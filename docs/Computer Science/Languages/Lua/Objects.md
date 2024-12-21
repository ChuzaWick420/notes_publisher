# Objects

`Objects` are just `tables`.

All following 3 examples achieve the same effect.

```lua
Dog = {
	new = function (self, args)
		-- does something
	end
}
```

```lua
Dog = {}
function Dog.new(self, args)
	-- does something
end
```

```lua
Dog = {}
function Dog:new(args)
	-- does something
end
```

Now we will define how `new()` should work

```lua
function Dog:new()                         
	newObj = {sound = 'woof'}                
	self.__index = self
	return setmetatable(newObj, self)
end
```

The `new()` should return an `instance` which is a `table` (an `object`).  
This `table` is returned by `setmetatable()`

```lua
return setmetatable(newObj, self)
```

which sets `self` as `meta table` for `NewObj` (the data for the `instance` or `instance` in itself but only from the definition perspective).  

```lua
newObj = {sound = 'woof'}                
```

This allows us to overload the `.` `operator` which we do by 

```lua
self.__index = self
```
