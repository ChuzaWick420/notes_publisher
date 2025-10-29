---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Interaction Diagram

A series of diagrams can be used to describe the _dynamic behavior_ of an object-oriented system.  
This is done in terms of #message .

## Purpose

- Model interaction between objects
- Assist in understanding how a system actually works.
- Verify that the use case description can be supported by the existing classes
- Identify responsibilities/operations and assign them to classes.

#UML provides 2 mechanisms:
1. **Sequence Diagrams:** They provide time based view
2. **Collaboration Diagrams:** They provide an organization-based view

### Sequence Diagrams

The sequence of object interactions is illustrated by #message arranged in a time sequence.  
These can be used to easily model:
1. Sequential flows
2. Branching
3. Iteration
4. Recursion
5. Concurrency

![[Pasted image 20240723175601.png]]

In the above diagram,
- the `X-axis` represents the `objects` as boxes.
- `Y-axis` represents time
- `dotted line` represents the `life line` of the object
- boxes at top of the `life line` are called `activation boxes`, they represent for how long a #message will be activated.

#### Syntax

In the objects, \[instance name]\[: class name]
