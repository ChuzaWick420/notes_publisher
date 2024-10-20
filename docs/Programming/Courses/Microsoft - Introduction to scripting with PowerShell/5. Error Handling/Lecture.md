---
Provider: Microsoft
Platform: Microsoft Learn
---

# Error Handling
There can be levels of severity to the `errors` which determine if `script` should be stopped etc and totally depends your approach.

## Errors
You can get different types of `errors`.  
For example, if you are trying to write to a file, you might get `errors` like.
1. File does not exist
2. You are not allowed to write to the file

In `PowerShell`, there are `2` types of errors.

### Terminating Errors
This `error` can be handled by using `Try` / `Catch` blocks and if these are not handled, the `script` will terminate at the statement which caused the `error`.

### Non Terminating Errors
These `errors` don't terminate the `script`.

## Managing Errors by Using `Try`/`Catch`/`Finally`
### `Try`
You can encapsulate the potential `error` prone statements into a `try` block

```PowerShell
Try {
   # Statement. For example, call a command.
   # Another statement. For example, assign a variable.
}
```

### `Catch`
The `try` block may raise an `error`.  
In this case, while trying to _write_ to a file, we can get a `System.IO.IOException`.  
The `Catch` block catches this and tries to recover.  
The `Catch` block in the end _catches_ all `exceptions` other than `System.IO.IOException`.

```PowerShell
Try {
   # Do something with a file.
} Catch [System.IO.IOException] {
   Write-Host "Something went wrong"
}  Catch {
   # Catch all. It's not an IOException but something else.
}
```

### `Finally`
This is used in the end for clean up purposes.

```PowerShell
Try {
   # Do something with a file.
} Catch [System.IO.IOException] {
   Write-Host "Something went wrong"
}  Catch {
   # Catch all. It's not an IOException but something else.
} Finally {
   # Clean up resources.
}
```

## Inspecting Errors
There is a built-in `variable` (or `object`) that is `$_`

```PowerShell
Try {
     # Do something with a file.
   } Catch [System.IO.IOException] {
     Write-Host "Something IO went wrong: $($_.exception.message)"
   }  Catch {
     Write-Host "Something else went wrong: $($_.exception.message)"
   }
```

## Raising Errors

```PowerShell
Try {
   Get-Content './file.txt' -ErrorAction Stop
} Catch {
   Write-Error "File can't be found"
}
```

 We used `ErrorAction` with value `Stop` so that the `try` / `catch` block can deal with the error.

```PowerShell
Try {
   If ($Path -eq './forbidden') 
   {
     Throw "Path not allowed"
   }
   # Carry on.

} Catch {
   Write-Error "$($_.exception.message)" # Path not allowed.
}
```

We can also used a `Throw` block to raise an `error`.
