---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Identify Structures
## Structure
A `structure` is a manner of organization which expresses a strong semantic organization within a problem domain.

## Types
There are `2` types:
1. Generalization-Specialization (Hierarchy)
2. Whole-part (Aggregation)

# Define Attributes
When defining `attributes` of objects, remember to define them in such a way that the system needs it and there is no other way of knowing those `attributes`.

## Problems
There are some problems that need to be addressed while defining the `attributes`.
1. An attribute which varies with _time_ should be replaced by class with effective _date and time_. e.g. Price of an item.
2. An attribute which can have multiple values should be replaced by a `class` with object connection.
3. An attribute of a boolean nature should be named something like `status`.
4. If there are common attributes between the classes then they should be abstracted away into a common _generalized_ class.

# Show Collaborations
This is the 2nd step of evaluating the responsibilities of an object.  
It can be done through 8 sub-steps:
1. For an #actors, include an object connections to its #participant ( #association).
2. For a #participant, include an object connections to its #actors and its `transactions`.
3. For a `location`, include object connections to the objects it can hold ( #association), to its part objects ( #aggregation) and to the `transactions` which take place at that location. ( #association).
4. For a `transaction`, include connections to its #participant, subsequent `transactions` ( #aggregation) and its line items ( #aggregation).
5. For a `line item` , include connections to its `transactions`, its items ( #association), an `item description` object ( #association) and a subsequent `line item` ( #association).
6. For an `item`, include connections to its `line item` and `item description` object ( #association).
7. For a composite object, include connections to its parts ( #aggregation).
8. For all the objects mentioned above, include connections to objects which either receive `messages` from them or sends `messages` to them ( #association).

# Define Services
This is the 3rd and last step in defining the responsibilities of an object, that is to define what `services` it provides.  
While establishing the `services` for the objects, following fundamental questions need to be asked:
1. Why does the system need this object?
2. What useful questions can it answer?
3. What useful action can it perform?
4. What this object can do, based upon what it knows?
5. What this object can do, based upon whom it knows?
6. What calculations can it do?
7. What on going monitoring it can do?
8. What calculations across a collection could it make (letting each worker do its part)?
9. What selections across a collection could it make (letting each worker do its part)?
