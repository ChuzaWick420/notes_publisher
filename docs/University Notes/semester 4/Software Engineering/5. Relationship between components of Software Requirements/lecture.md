---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

![[Pasted image 20240428075743.png]]

# Business Requirements
Business requirements can conflict with each other.  
Imagine a developer company selling an embedded system to a retail store for its customers.

Now problem can arise when:
1. The developer company wants to implement a new direction for its customers.
2. The retail store wants to keep a simple solution.
3. Customers want the ease of use and features.

# Vision Statement
The vision statement should reflect a balanced view of ideologies and realities of the customer market to appeal to a diverse group of customers.

# Chemical Tracking System
"The chemical tracking system will allow scientists to request containers of chemicals to be supplied by chemical stockroom or by vendors. The location of every chemical container within the company, the quantity of the material remaining in it, and the complete history of each container’s location and usage will be known by the system at all times. The company will save 25% on chemical costs by fully exploiting chemicals already available within the company, by disposing of fewer partially used or expired containers, and by using a standard chemical purchasing process. The chemical tracking system will also generate all reports required to comply with federal and state government regulations that require the reporting of chemical usage, storage, and disposal."

# Assumptions
The management sponsor for the chemical tracking system might think that project will replace the stockroom inventory system and interface with appropriate purchasing department applications.

# Scope
The `scope` of a project defines the range of the project.  
The limitations tell us what the project won't be able to do.  
This helps in setting up the `stake holders`' expectations.  
They may request features which are:
1. Too expensive to be implemented so we have to reject them.
2. Are beneficial but we have to worry about adjusting staff, budget and schedules.  
Also, keep records of the rejected ideas along with the reasons because they may be introduced in future in different flavors. 

# Scope and Initial Release
The initial release should specify the major features of the project.  
The quality characteristics should be mentioned which ensures that product will provide the promised benefits to the customers.  
Requirements should be prioritized and a schedule should be made.

# The Context Diagram
This diagram illustrates the boundaries defined by the scope of the project.  
Everything that is outside the system which may interface with it, is called `external entity` or `terminators`.  
The diagram also specifies the flow of data between these entities.  
![[Pasted image 20240428084212.png]]

# Use Cases and Dev-Customer Relationship
For a successful project, a strong developer customer relationship has to be built for effective communication.  
This effective communication can then produce effective requirements.

A software engineer doesn't necessarily has to solve a Computer Science problem but rather he has to understand the terminology used in domains of vendor and customers and then use that terminology in a structured document.  
This improves his communication level and strengthens the relationship.  
Make sure there is no false assumptions and ambiguity.

The tool used for structing requirements is called #use-case-modeling.  
This modeling technique is used in #UML (Unified Modeling Language).  
Since it is intuitive so customer doesn't need to know the notation and the developer can communicate the system through easily.  
This way, developer has a model to work on and customer has an understanding of how system works.

## Components of Use case Model
The #use-case-model has 2 components.
 1. **Actors**: These are the entities which interact with the system. They can be humans, devices or systems.
 2. **Use cases**: These are the desired actions to be performed by `actors`.

A #use-case-model describes how the system works. Like a black box, it describes the functional requirements of the system to the `actors`.  
To the developers, it provides a blueprint on how the system behaves.  
It also provides interfaces to the testers to check if required functionality is working or not.
