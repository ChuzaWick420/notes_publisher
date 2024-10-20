---
Provider: Microsoft
Platform: Microsoft Learn
---

# Introduction to Scripting
## Intro
When you are using `PowerShell`, you might find yourself repeating some commands again and again.  
Therefore, it is better to store these commands or statements into a `text file` which ends with `.ps1` extension.  
The script involves calls to `cmdlets`, `functions`, `variables` and more.

## Variables
You can use `variables` to store values and use them as inputs to to other commands.

## Functions
`Functions` are a _named_ set of statements which produce and output, which further can be used as input to other commands.

## Flow Control
These are execution paths a program can take.  
Statements like `If`, `ElseIf` and `Else` are helpful for this.

## Loops
These are constructs which let you perform certain operations for a number of times.

## Error Handling
There are `terminating` and there are `non-terminating` errors.

## Expressions
These are representatives of `values`.

## .NET And .NET Core Integration
`PowerShell` can integrate with `.NET` and `.NET Core`.

## Run a Script
`Scripts` can be dangerous.  
If you don't understand them, don't run them.

### Relative Paths
The `scripts` require either an `absolute` path or `relative` path to be executed.  
This ensures that you exactly know what you are running in case the `script` name overlaps with name of some other `cmdlet`.

### Execution Policy
These are safety features which have different levels.
1. Local Computer
2. Current User
3. Current Session

## Execution Policy

```PowerShell
Get-ExecutionPolicy
```

This returns the `execution policy`  
Possible values:
1. `Restricted`: The computer cannot run the scripts.
2. `RemoteSigned`: The computer can run the scripts. The `scripts` downloaded from internet, needs to be _signed_ by a _digital signature_ by a _trusted publisher_.

## Variables
These are not just for `scripts`.  
You can also define them on console.

```PowerShell
$PI = 3.14
```

### Working with Variables: Quotation Marks and Interpolation
You can use `Write-Host` or `Write-Output` to print stuff on the console.

Using `double quotations`, we can interpret values of the `variables`.  
Code:

```PowerShell
Write-Host "Value of PI is $PI"
```

Output:

```
Value of PI is 3.14
```

Using `single quotations`, there is no interpretation done.

Code:

```PowerShell
Write-Host 'Value of PI is $PI'
```

Output:

```
Value of PI is $PI
```

We can also use `$()` for `expressions`.  
Example:

```PowerShell
Write-Host "Value of PI is $($PI + 1)"
```

## Scope
These define where the `variables` and other things like `functions` etc are accessible.

### Types of Scope
There are 3 types.

#### Global Scope
Things which are defined in this `scope` are accessible even after the `session` ends.  
This exists as the `PowerShell` starts.

#### Script Scope
This is limited to the `script` file itself and everything defined inside it, is wiped away after the file is done running.  
If you want to define `variables` at _global scope_ then you prepend the `global` keyword during definition.

```PowerShell
global $PI = 3.14
```

#### Local Scope
It is the _current scope_ which can be _global_ or any other scope.

### Scope Rules
#### Scopes Can Nest
A `scope` can have a _parent scope_.  
Conversely, a _parent scope_ can have a _child scope_

#### Items Are Visible in the Current and Child Scopes
Items which are defined in a `scope` are available in that particular `scope` and any of its _child scope_.  
This behavior can be changed by making the items private to the `scope` they were created in.

#### Items Can Be Changed only in the Created Scope
Items can only be changed in the `scope` they were created in.  
This can be changed by specifying a different `scope`.

## Profiles
These are `scripts` which run as soon as a new `PowerShell` session starts.

### Profile Types

| Description                | Path                                                            |
| -------------------------- | --------------------------------------------------------------- |
| All users, All Hosts       | $PSHOME\Profile.ps1                                             |
| All users, current host    | $PSHOME\Microsoft.PowerShell_profile.ps1                        |
| Current user, all hosts    | $Home[My ]Documents\PowerShell\Profile.ps1                      |
| Current user, current host | $Home[My ]Documents\PowerShell\Microsoft.PowerShell_profile.ps1 |

The `$PSHOME` is the `PowerShell` installation directory  
The `$HOME` is the `Current User` home directory

### Create a Profile
You can do the following to print all profiles and the associated paths to them

```PowerShell
$Profile | Select-Object *
```

Here the `$Profile` is the variable which holds path to the _profiles_.

To make your customizations:
1. Make a `text file` using the command

```PowerShell
New-Item -Path $Profile.CurrentUserCurrentHost
```

1. Add your customizations to the text file.
2. Restart `PowerShell`
