---
Provider: Microsoft
Platform: Microsoft Learn
---

# Manage Input and Execution Flow Using `IF`, `ElseIf` and `Else`
The `expressions` in `If` construct evaluate to either `True` or `False`.

```PowerShell
If(<expressio>) {
	# Statements to run
}
```

## Operators
`PowerShell` has built-in parameters like `$True` and `$False`

There are different operators such as:  
1. `-le` for _less than or equal to_
2. `-eq` for equal

### Example

```PowerShell
$Value = 3

If ($Value -le 0) {
  Write-Host "Is negative"
}
```

## `Else`
This block runs if the `If` condition fails.

## `ElseIf`
This blocks run if the condition for previous `If` or `ElseIf` fails.
