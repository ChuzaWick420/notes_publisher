# Lists

`Lists` are not a unique `data type` but rather, they are just `tables` with numbers as `keys`.

```lua
list = {
	"Hi",
	"Bye",
	69,
	true,
	function()
		print("yo")
	end,
}

list_items_count = #list  -- # operator returns the number of items in the list

for i = 1, list_items_count do
	print(list[i])        -- indices start from 1
end
```