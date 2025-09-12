---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Creating a Use case Model
The #use-case-model is created firstly by identifying the `actors`.  
Then their `use cases` are defined which define the system.  
After that, the relationship between these `use cases` are defined.

All these steps are not sequential but parallel. 

# Components of Use case
1. **Priority**: Some use cases have higher priority so the ones with lower priority should be delayed to next phases.
2. **Actor**: Defining which use cases will be used by an `actor`.
3. **Summary**: To provide _context_ to the reader how this use case is going to be used.
4. **Pre-condition**: This determines which conditions have to be fulfilled before using the use case.
5. **Post-condition**: This is the expected state of the system after the use case has been used.
6. **Extends**: It can extend other use cases.
7. **Details**:
	1. **Normal Course of Events**: An expected sequence of behavior of the system when use case is being used.
	2. **Alternative Paths**: Sequence of actions deviating from the normal course.
	3. **Exceptions**: When an error occurs in the system, what can be done.
8. **Assumptions**: All the assumptions that have be taken for this use case.

**Example:**  
![[Pasted image 20240428195956.png]]

**Summary**: The data to be deleted should not be used in the system. (meaning you can only delete the unused data).  
**Pre-condition**: The information to be deleted was stored on the system.  
**Post-condition**: The information is gone.  
**Uses**: Record transactions, cancel actions.  
**Extends**: none.  
**Details**:
1. **Normal course of Events**: The use case states when the user wants to delete the information. A dialogue box appears asking the user if he wants to delete the information. User confirms and the information is deleted permanently.
	1. Use Cases: Transaction Record
2. **Alternative Path**: The user chooses _abort_ and the action is cancelled.
	1. Use Cases: Cancel Action
3. **Exceptions**: The user is not allowed to delete the information that is being used inside the system.  
**Assumptions**: An information which is not being used in the system, can be deleted permanently from the system and cannot be retrieved.

# Other Ways to Express Use Case
Another way is to create a table with 2 columns, namely `User Action` and `System Reaction`.

# Activity Diagram
It provides a visual for how the use case is being performed.  
![[Pasted image 20240429151743.png]]

# Use case Limitations
The _non-functional_ requirements are not documented.  
These requirements can be something like:  
**Usability**: It should be usable to colorblind people.  
**Reliability**: It should be useable all the time.  
**Performance**: The authorization process should take about 30 seconds.  
**Access**: It should be accessible over the internet.  
**Portability**: It should be able to run on multiple OSs.
