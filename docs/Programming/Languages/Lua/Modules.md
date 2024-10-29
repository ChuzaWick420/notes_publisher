# Modules

## Example

### Plugin.lua File

```lua
local M = {}

local function iAmSecret()
	print("I am a caveman")
end

function M.greet()
	print("Hello World")
	iAmSecret()
end

return M
```

## Some other File

```lua
local plugin = require("Plugin")
 -- translates to
local plugin = (
	function()
		-- contents of `Plugin.lua` are loaded here
)() -- invokes the function
```

The `iAmSecret()` `function` is only visible inside the `Plugin.lua` file itself, not outside of it.

## Caching

```lua
local a = require("Plugin") -- included and ran
local b = require("Plugin") -- not ran, cached

-- a = b

local x = dofile("Plugin.lua") -- ran
local y = dofile("Plugin.lua") -- ran

local f = loadfile("Plugin.lua") -- load but don't run
```