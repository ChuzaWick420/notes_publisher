---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

Processes are usually used to perform different actions, such as:
- Take some data and sort it out.
- Alter an existing data by applying filters on a database.
- Taking input and doing some calculation.
- Decision making based on existing data.

# CRUD
Performing manipulation on stored data is called #CRUD operations.  
#CRUD stands for:
- Create
- Read
- Update
- Delete

## Layers of Abstractions
Within the #DFD, we hide the abstractions and complexities of each process or part of the diagram to keep it readable.  
Otherwise the diagram becomes way too big to read.  
Then each part can be explained in details in other diagrams.

### Context Level Diagram
In this level, we probe out the system and the agents it interacts with.  
At this level, the system is a black box (keeping the details hidden).  
The flow of information and which outputs are generated from which inputs are also drawn.

### Level One Diagram
This level describes the system as major `processes` and which outputs are produced by each process against the inputs provided by the external entities.

### Level Two Diagram
This level describes each `process` in detail.

> Note: The number of external agents, inputs and outputs should remain the same throughout the levels to keep consistency.

## Example
## Patient Monitoring System
### Context Level Diagram
The patient might show some vital signs which should be sent to nurse as an alter message.  
Other than that, the nurse should be able to get reports about the patient, stored as logs.  
![[Pasted image 20240510200229.png]]

### Level One Diagram
![[Pasted image 20240510200548.png]]

### Level Two Diagram
![[Pasted image 20240510200857.png]]

### Example of Mistake
![[Pasted image 20240510201338.png]]

Pay close attention, if you perform the #source-and-sink-analysis,  
you will notice that `freeze member account` process is not accepting any inputs.  
Similarly, the `create a new member account` process is not generating any output.  
The process `Generate an employee bank statement` takes 2 inputs which are irrelevant to the output generated because we need `account number` and `time of request` to generate the `bank statement`.

### Illegal Data Flows
1. an external entity cannot directly interact with another external entity, it has to be done through a `process`.
2. A #data-store cannot directly interact with another #data-store, it has to be done through a `process`.
3. An external entity cannot directly interact with a #data-store directly, it has to be done through a `process`.
