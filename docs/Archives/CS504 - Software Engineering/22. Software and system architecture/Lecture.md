---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Introduction

The design process for identifying the sub-systems which make up the system and a framework to control their communication, is called `architectural design`.  
The output of this design process is called `software architecture`.

A `program family` is a set of programs(not all of which necessarily have been or will even be constructed) for which it is profitable and useful to consider as a group.

# What is Software Architecture?

There is no single definition but it focuses on the structural aspects of a system.

## Definitions

### Uml 1.3

Architecture is the organizational structure of a system.
- It can be recursively decomposed into components which interact with each other through `interfaces`
- the relationships which connect these parts.
- Constraints for connecting the parts together.

### Garlan and Perry, Guest Editorial to the Ieee Transactions on Software Engineering, April 1995

Software architecture is the combination of components of a program or system, their relationships and the rules governing their design and evolution over time.

### Ieee Glossary

It is a process of defining a collection of hardware and software components to develop a computer system

### Shaw and Garlan

The architecture of a software defines it as a collection of components and their interactions.  
Components are such things as filters, data bases, clients, servers and layers in a hierarchical system.

# Why is Architecture Important?

If the project has not achieved a system architecture, it should not proceed to full-scale software development.  
Having it as a deliverable enables its use throughout the development and maintenance process.

## Reasons to Invest in Architecture

### Mutual Communication

It represents common high-level abstraction of the system that most stakeholders can use to have a mutual understanding of the system and it also enables them to communicate.

### Early Design Decision

Since it is the earliest design documents of a system, it has a lot of weight since it captures an over all view of the system.  
So any change in the design should be made early before development by looking at the architecture

The different parts of the system can be assigned to different groups for construction.  
This is called work breakdown structure of a system.

### Reusable Abstraction of a System

It can be used as a substitute for designs of other systems which have similar needs.

## Architectural Attributes

A software architecture should cover functional and non-functional requirements of the software system. This includes:
- Performance
- Security
- Safety
- Availability
- Maintainability

Following are the guidelines that can help in addressing these challenges:
1. **Performance:** Performance can be improved by minimizing system communication. This can be done by localizing the operations and try to make as self contained modules as possible
2. **Security:** Security can be improved by using a layered architecture with critical assets put in inner layers.
3. **Safety:** Safety critical components should be isolated.
4. **Availability:** Availability can be ensured by building redundancy in the system and having redundant components in the architecture.
5. **Maintainability:** Maintainability can be insured by using self contained modules.

## Architectural Design Process

It is a creative and iterative process.  
This is done by:

### System Structuring

This is decomposition process in which a system is decomposed into multiple sub-systems and their communication is identified.  
A `sub-system` is a system on its own, the operations are independent of the services provided by other sub-systems.  
A `module` is a system component that provides services to other components but would not normally be considered as a separate system.

### Control Modelling

Control modelling establishes a model of the control relationships between the different parts of the system.

### Modular Decomposition

The system is decomposed into multiple modules
