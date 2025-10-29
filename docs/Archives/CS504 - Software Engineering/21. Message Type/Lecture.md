---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Message Types

There are different types  
![[Pasted image 20240723180253.png]]

## Synchronous

These are `call events`  
![[Pasted image 20240723180544.png]]

### Guidelines

- Don't model `return` value when the value is obvious. e.g. `getTotal()`
- Only model `return` value when it is supposed to be used else where. e.g. as a parameter value for another message
- Prefer modeling `return` values as a part of method invocation. e.g. `ok = isValid()`

## Asynchronous

These are `signals`.  
They don't block the caller and are used in #multi-threading applications.  
Following are the actions they perform:
- Create a new thread
- Create a new object
- Communicate with a thread that is already running

## Create

![[Pasted image 20240723181746.png]]

## Destroy

![[Pasted image 20240723181810.png]]

An object can also destroy itself.

# Sequence Diagrams and Logical Complexity

If the diagram is small and simple then it is good.  
Otherwise if it is big and complex then it should be broken down into multiple diagrams.

# Collaborating Diagrams

![[Pasted image 20240723182133.png]]

The numbering represents the sequence of #event.

# Comparing Collaboration and Sequence Diagrams

`sequence` diagrams are good to see the flow of time.  
`collaboration` diagrams are good to see static object connections.  
what is better for understanding sequence of #event? `sequence` diagrams.  
what is better for organization and control flow? `collaboration` diagrams.

# Evaluating the Quality of an Object-oriented Design

![[Pasted image 20240723182754.png]]

The room in the diagram is not `encapsulated` as one object.  
The `heat flow regular` has to communicate to different objects, hence increasing the coupling.

![[Pasted image 20240723183403.png]]  
This diagram represents the room as a single `object` and the coupling is also reduced since the communication is done with one object.

There still exists a problem.  
The control is still centralized. We have to make queries to the `room` object and based on the responses, then we do something about the `furnace`.

This can be improved by giving the control to the `room` object itself.  
![[Pasted image 20240723183913.png]]

For example:  
a `class` with a lot of interfaces is more complex to understand.  
Instead of doing:

 ```cpp
void SetMinimumValue(int aValue);
void SetMaximimumValue(int aValue);
```

We can do

```cpp
void SetLimits(int minValue, int maxValue);
```
