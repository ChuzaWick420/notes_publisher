# Operators

## Composite Operators

`lua` does not have operators which composite with =, such as:
1. `+=`
2. `-=`
3. `*=`
4. `/=`  
Instead, we need to rely on things like

```lua
var = var + 1
```

## Not Operator

`!=` is not present in `lua`.  
instead, we have `~=`.

## Logical Operators

`lua` does not have `!` or `&&` or `||`, instead it has `not` and `and` and `or` keywords.
