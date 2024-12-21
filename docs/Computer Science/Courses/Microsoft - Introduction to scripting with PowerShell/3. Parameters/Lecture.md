---
Provider: Microsoft
Platform: Microsoft Learn
---

# Parameters
The following can accept `parameters`:
1. `Cmdlets`
2. `functions`
3. `scripts`  
These make the `scripts` more flexible

## Declare and Use a Parameter
To use `parameters` we use `Param()` keyword.

imagine we have a file named `script.ps1`

```PowerShell
Param(
	$Path
)
New-Item $Path
Write-Host "File has been created"
```

The `parameters` been to be comma separated.

## Use The Parameter
Then inside the `PowerShell` we can use it as follows.

```PowerShell
./script.ps1 -Path "./newfile"
```

## Improve Your Parameters
You should keep the following questions in mind:
1. Is this `parameter` _optional_ or _mandatory_?
2. What are the legal and illegal values?
3. Does it accept _multiple types_ of values or _single type_
4. Can it rely on _default values_?
5. Can you provide details to the user?

## Select an Approach
You can do the following things

### If / Else

```PowerShell
Param(
   $Path
)

If (-Not $Path -eq '') {
   New-Item $Path
   Write-Host "File created at path $Path"
}

Else {
   Write-Error "Path cannot be empty"
}
```

### Making Parameters Mandatory
You can make a `parameter` _mandatory_ by using a _decorator_.

```PowerShell
Param(
	[Parameter(Mandatory)]
	$Path
)
```

If you run the `script` without providing the value of the `parameter`, `PowerShell` would ask you to enter the value for it.

```
cmdlet script.ps1 at command pipeline position 1 Supply values for the following parameters:
Path:
```

You can further improve the _decorator_ by providing a `HelpMessage`.

```PowerShell
[Parameter(Mandatory, HelpMessage = "Please provide a valid path")]
```

Then if you type `!?`, the `HelpMessage` will pop up.

```
cmdlet script.ps1 at command pipeline position 1 Supply values for the following parameters:
(Type !? for Help.) 
Path: !?
Please provide a valid path
```

### Assigning a Type

```PowerShell
Param(
	[string]$Path
)
```

### Default Values

```PowerShell
Param(
	[string]$Path = "defaut value"
)
```
