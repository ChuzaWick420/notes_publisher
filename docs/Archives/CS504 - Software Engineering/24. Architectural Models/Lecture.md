---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Architectural Models

A `static model` shows the major system components while a `dynamic process model` shows the process structure of the system.

## Architectural Styles

There are different styles with their characteristics and attributes which can be beneficial according to the requirement at hand.  
Among many styles, the most commonly practice are the following:
- Data-centered Architectures
- Client Server Architecture and its variation
- Layered Architectures
- Reference Architecture

## Data-centered or the Repository Model

Any system and sub-system needs to exchange data. There are 2 ways:
1. Shared data is held in a central database or repository and may be assessed by all sub-systems
2. Each sub-system maintains its own database and passes data explicitly to other sub-systems

## Repository Models

![[Pasted image 20240724204109.png]]  
This model is mostly used in mainframe applications

### Advantages

It is efficient way to sharing large amounts of data.  
In this case, sub-systems need not to be concerned with how data is produced centralized management.
- backup
- security

### Disadvantages

Data evolution is difficult and expensive.

## Client Server Model