---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

The information moves from one place to another.  
When it is moved, certain actions are performed over it.  
This movement is controlled by a set of rules.  
These are documented easily through the state transition diagram.

# Trouble Ticket System

![[Pasted image 20240429185411.png]]

# Tabular Form

![[Pasted image 20240429185709.png]]

## External Inputs

These are elementary processes come from outside the system to process or control information and may alter the system. It's primary intent is to maintain ILFs (Internal Logic Files).

## External Outputs

These are the elementary processes which send information outside of the application boundary.  
Their primary intend is to present the information to the user.  
The processing logic must contain at least one mathematical structure or should create derived data.  
They can also maintain ILFs.

## External Inquiry

It also sends data outside the application boundary and presents data to the user derived from the ILFs.  
It doesn't contain any mathematical formulas. 

![[Pasted image 20240429202744.png]]

# Data Flow Model

## Dfd Notation

**Process**: Rectangle  
**External Entity**: Rectangle  
**Data store**:  
![[Pasted image 20240429203522.png]]  
**Data Flow:** Arrow

## Flow Charts

These are sequential.  
Usually would be used to represent algorithms.

**Example:**  
![[Pasted image 20240429203923.png]]
