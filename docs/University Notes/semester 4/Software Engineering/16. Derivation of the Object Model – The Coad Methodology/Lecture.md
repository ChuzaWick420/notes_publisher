---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# The Coad Methodology
This methodology provides `5` steps to derive the static structure of the #object-model.

## Select Objects
This is divided into`6` further steps:

### Select Actors
#actors are entities that take part in the system.  
**Examples:** People, organizations etc.

### Select Participants
A #participant is a role which an #actors plays in the system.  
**Examples:** customer, cleric, buyer, cashier etc.

> NOTE: an #actors can play as multiple #participant in the system at different times.

### Select Places
Places can be objects which contain other objects.  
**Example:** Hospital, School etc.

### Select Transactions
These are "events" that have to be tracked.  
**Examples:** Agreement, assignment, authorization, delivery, subscription etc.

### Select Container Objects
Similar to places.  
Every place can be a container but every container cannot be a box.  
**Examples:** box, cabinet, safe, shelf etc.

### Select Tangible Things
These are the remaining nouns left in the system.

## Things to Consider
While selecting objects, following things have to be considered:
1. Every object needs to have some responsibility or a role in the system. For this reason, it is important to know the attributes of the object. If it is not possible to know about the object then it is better to remove it from the system.
2. Avoid using #controller-objects (someone who likes to do everything by himself, does not trust anyone). Use delegation instead where responsibility is passed onto another object.
3. There might be multiple objects with similar responsibilities. Try to look for them and assign a common name.
4. Use meaningful names. Try using the names from the problem domain itself.
