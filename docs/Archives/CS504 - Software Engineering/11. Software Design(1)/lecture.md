---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Introduction
Once the requirements are finalized, we move towards the design.  
Here, we focus on the _how_ in solving our problem.  
Here the details are studied and a roadmap is developed which leads the development.

This includes partitioning of the system into components, defining their interfaces.  
Also defining interfaces with the real world.  
Data structures, entities, design regarding algorithms is also developed.

# Managing the Complexities of a Software System
To manage the complexities, there are principles of:
- separation of concern
- modularity
- abstraction

## Separation of Concern
This allows us to isolate different parts of the problem and focusing on each part separately, independent of each other.

## Modularity
It means you take a problem and chop it down to smaller pieces.  
This follows the #divide-and-conquer philosophy.  
You solve each part of the problem and then integrate them.

# Software Design Process
This process is not `sequencial` but rather iterative , called #agile-develop in technical terms.  
The system is looked at from different angles and different models are developed.  
The system is divided into sub-systems and modules and their interfaces are defined.  
Then these sub-systems are further divided in similar manner.

The #data-modeling is an activity performed during this design phase.  
Here you identify the entities, their attributes, their relationships and #data-structures to manage them.

# Software Design Strategies
There are 2 strategies:
1. #functional-design or #structured-design
2. #object-oriented-design

## Functional Design
The whole system is looked as a #function, (like `main` function from C) which calls other `functions` to complete the goal.  
We can decompose the whole system into `functions`.  
This approach looks very similar to #functional-programming.

## Object Oriented Design
The whole system is looked as a collection of `objects` with their own states.  
The system state is de-centralized into these `objects` which coordinate with each other through `messages` when needed.  
This approach looks very similar to #object-oriented-programming .

The #object-oriented-design has gained the popularity and is more maintainable as compared to the #functional-design.

## Software Design Qualities
The parameters to measure the software quality are following:
- Compactness
- Maintainability
- Reusability
- Efficiency  
These parameters depend on the type of project.  
Example: an #embedded-system project might prioritize _efficiency_ over _maintainability_.  
Meanwhile a business application would have its priorities flipped.

## Maintainable Design
A maintainable code base is flexible and has minimal cost involved.  
To achieve this, one should focus on `separation of concern`, `modularity` and `abstraction` such that it yields a cohesive design which is loosely coupled (meaning, changing one part of the system doesn't affects the other).
