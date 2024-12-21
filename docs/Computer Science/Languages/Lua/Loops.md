# Loops

## For

```lua
for i = 0, 20, 2 do
	print(i)
end
```

Notice how there are `3` values.

1. Starting value
2. Ending value
3. Add to `i` by

The last number which determines the amount of addition is _optional_.

## While

```lua
while num < 50 do
	print("hi")
	num = num + 1
end
```

`block scopes` usually end with `end` keyword.

## Another Variant

```lua
n = 50
repeat
	print("hi")
	n = n - 1
until n < 20
```

Very similar to `do while` from `C` but only difference here is that the condition needs to be `false`.  
If the condition is `true`, it will run once and exit.