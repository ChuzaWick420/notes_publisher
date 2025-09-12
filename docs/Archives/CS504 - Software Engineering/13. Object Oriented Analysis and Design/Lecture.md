---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Object Oriented Design, Why?
An Object Oriented system software is usually hierarchical, highly cohesive and loosely coupled.  
The key advantages of this approach are following:
1. It is more closer to human cognition
2. Reusable code is generated through provision of generalization and inheritance.
3. Reduced effort for maintenance and enhancements resulting from low coupling, higher cohesion and inheritance.

# The Object and the Class
An `object` is an individual unit which exists in the system.  
It has:
1. Identity
2. State
3. Behavior

## State
The `state` is a collection of `properties` the object possesses along with their values.  
These are encapsulated within the object.

## Behavior
These are the actions performed by the `object` in response to a stimuli from the clients through the `methods` the `object` possesses.

## Structure
A `class` is a template for `objects` of similar type.  
It has a public view (from outside) called its `interface`.  
It also has a private view (from inside) called its `implementation`.

# Classification
This stage is the most critical one.  
When we look at the problem from different angles, we can classify it into different categories.  
![[Pasted image 20240525151249.png]]

# The Object Model
The elements of #object-oriented-design are collectively called #object-model.  
It consists of principles of:
1. Abstraction
2. Encapsulation
3. Hierarchy of Inheritance

## Abstraction
This focuses on the external `interface` the `class` provides and it is separated from how it is internally implemented.

## Encapsulation
This focuses on the fact that external entities cannot look into the implementation of the `class`.

# Relationship among Objects
There are patterns of interaction between objects.  
These relationships are:
1. Inheritance
2. Association
3. Aggregation

## Inheritance
#inheritance defines a “kind of” hierarchy among `classes`.  
There are `2` `classes` involved.
1. `super class`: From which the general properties are derived
2. `sub class`: The derived class which can either _extend_ the functionality of _restriction_ the functionality (`specialization`).

## Association
#association defines a relationship in which object `A` “uses” object `B`.

## Aggregation
#aggregation defines a relationship in which object `A` is “contained by” object `B`.

# Aggregation and Association
## Basic Differences
The objects in #aggregation exist in a tighter coupling.  
They exist in a way that they cannot exist independently.  
However, if they are usually independent, then they are in #association relationship.

## Object Creation and Life Time
In terms of #aggregation, the objects have to be created at same time and have to be destroyed at same time as well.  
Whereas, in case of #association, objects have to be alive _only_ when a `message` needs to be communicated between them.

## Coupling and Linkages
#aggregation has strong `coupling` as compared to #association.  
The links between the objects in #aggregation are permanent meanwhile for #association, they only exist as long as the services are required from different objects.  
After the services have been done, the links can be discontinued.

## Ownership and Visibility
For #aggregation, since it is a container - contained relationship, the container has encapsulated its parts which cannot be accessed outside of it.  
For #association, the objects can be directly accessed by other objects.

## Database Persistence
For #aggregation, the parts have to be stored as well but for #association, only reference to the objects will be enough.
