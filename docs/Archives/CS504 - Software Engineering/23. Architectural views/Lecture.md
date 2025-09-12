---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Architectural Views
Software architecture provides a structure about the software by putting together architectural views in an organized fashion.

According to Perry and Wolfe:  
Software architecture = {elements, forms, rationale}

These elements are further divided into 3 categories.
- Data elements
- Processing elements
- Connecting elements

![[Pasted image 20240724183612.png]]

![[Pasted image 20240724183813.png]]

| **View**             | **Components**                                                       | **Users**                                           | **Rationale**                                                                          |
| -------------------- | -------------------------------------------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Functional View**  | functions, key system abstractions, domain elements                  | domain engineers, product-line designers, end users | functionality, modifiability, product lines/reusability, tool support, work allocation |
| **Code View**        | classes, objects, procedures, functions, subsystems, layers, modules | programmers, designers, reusers                     | modifiability/maintainabi lity, portability, subsetability                             |
| **Development View** | files, directories                                                   | managers, programmers, configuration managers       | managers, programmers, configuration managers                                          |
| **Physical View**    | CPUs, sensors, storage                                               | hardware engineers, system engineers                | system delivery and installation, performance, availability, scalability, security     |
| **Concurrency View** | processes, threads                                                   | performance engineers, integrators, testers         | performance, availability                                                              |  

`views` are used as documentation vehicle for current development and future development.  
Users are `views` are both managers and customers.

## Hierarchical Views
Every view is almost hierarchical.
- `function view` can contain `sub-functions`
- `development view` contains directories which contain files.
- `code view` would have modules and systems that contain `sub-modules` and `sub-systems`
- `concurrency views` would have `processes` that contain `threads`

## Architectural Styles
Each style describes a system category that encompasses:
1. a set of components (e.g. database, computational modules) that perform a function required by a system
2. a set of connectors that enable "communication, coordination and cooperation" among components
3. constraints that define how components can be integrated to form the system and semantic modes that enable a designer to understand the overall properties of a system by analyzing the known properties of its constituent parts.
