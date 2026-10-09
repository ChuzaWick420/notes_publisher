# Quality Engineering

## Terms

- Error: Human error like syntactic or semantic
- Fault: Results of errors. It is an incorrect step or process
- Failure: Unexpected behavior caused by faults
- Bugs: Errors caught during development
- Defect: Deviation of software functionality from user requirements

## Budgeting

Total budget: $x$  
Total features: $y$  
Cost per feature: $\frac{x}{y}$

## Risk Analysis

$$\text{Risk} = \text{Likelihood}(\text{Probability}) \times \text{Consequences}(\text{Impact})$$

### Levels

> [!QUOTE] The IEEE Standard for Software Verification and Validation has published the most broadly known scale of criticality in the IT domain.

- Catastrophic
  - Continuous usage (24 hours per day)
  - Irreversible environmental damages
  - Loss of human lives
  - Disastrous economic or social impact 
- Critical
  - Continuous usage (version change interruptions) 
  - Environmental damages
  - Serious threats to human lives 
  - Permanent injury or severe illness
  - Important economic or social impact.
- Marginal
  - Continuous usage with fix interruption periods 
  - Property damages 
  - Minor injury or illness 
  - Significant economic or social impact.
- Negligible
  - Time-to-time usage 
  - Low property damages 
  - No risks on human lives
  - Negligible economic or social impact.

# Golden Triangle

- People
- Process
- Technology

> [!QUOTE] A process is a set of practices performed to achieve a given purpose more importantly practices are uniform and same across organization to perform a specific task. A process serves as an integration point which ensures synergy.

> [!QUOTE] But this should be kept in mind that there is not good or bad process; internal limitation, circumstances and resources must be evaluated before adopting any external process that seems to be optimal because what works in one situation might not work in others.

| **Immature Organization**         | **Mature Organization**                    |
| --------------------------------- | ------------------------------------------ |
| Process improvised during project | Inter-group communication and coordination |
| Approved processes being ignored  | Work accomplished according to plan        |
| Reactive, not proactive           | Practices consistent with processes        |
| Unrealistic budget and schedule   | Processes updated as necessary             |
| Quality sacrificed for schedule   | Well-defined roles/responsibilities        |
| No objective measure of quality   | Management formally commits                |

> [!QUOTE] Capability Maturity Model Integration (CMMI) is a collection or a model of best practices in systems, product and software development.

- Change should be normal and it must come slowly. Massive changes at once are doomed to failure
- Change should come in increments; in various steps.
- Change must come with future in mind, crisis prevention is better than recovering from crisis.

# Maturity Levels

## Level 1 - Initial

- Processes are imperfectly defined
- Processed are reactive in nature
- Organization is unstable and unpredictable
- No roadmap
- No defined responsibilities

### Example

1 project but 2 project managers. Each tells a different story to the client.

## Level 2 - Managed

- Policies and related frameworks are established
- Service strategy, work plans, manage work according to the plans.
- Processed are planned and managed according to policy.
- defined responsibilities
- Still not optimal
  - reactive
  - relies on Heroes and performance goes down when they are gone.

### Example

Company has few products deployed. A client requests a new module for a product. The developer is absent for few weeks so marketing team cannot reach him. Client gets angry and stops using the product / moves to someone else.

## Level 3 - Defined

- Standard process for developing and maintaining software are established and documented
- Processes include both
  - Software Engineering Processes
  - Management Processes
- Reliance is on process, not hero

### Example

Todo:
- Internal Kickoff to discuss and clarify scope related queries 
- Client Kickoff
  - Team Introduction by Project Manager 
  - Scope related queries clarified from client
  - Scope should be explicitly approved by the client
  - Meeting minutes to be shared with Client, Team lead by Project Manager

## Level 4 - Quantitatively Managed

- Management can measure different valuable metrics like software process, quality and productivity and they can also tune them as required. 
- The performance of processes is controlled using statistical and other quantitative techniques and predictions are based, in part, on a statistical analysis of fine-grained process data.
- Quantitative boundaries are decided for the processes and organizations achieve control over their products and processes by narrowing the variation in their process performance to fall within acceptable range.

### Example

| **Name**          | **No of Participants** | **Planned Time (Minutes)**             | **Total Man Time (Minutes)** |
| ----------------- | ---------------------- | -------------------------------------- | ---------------------------- |
| Internal Kick-Off | 4                      | 60                                     | 240                          |
| Client Kickoff    | 5                      | 60                                     | 300                          |
|                   |                        | Total Time Spend on Kick-Off (Minutes) | 540                          |
|                   |                        | Total Time in Hours                    | 9                            |

## Level 5 - Optimized

- Continuous process improvement in
	- Capability
	- Performance
- Such improvements occur by
	- Incremental changes in existing processes
	- Adopting new technologies and methods

### Example

#### Option 1

Reduce meeting audience

| **Name**                                                 | **No of Participants** | **Planned Time (Minutes)**             | **Total Man Time (Minutes)** |
| -------------------------------------------------------- | ---------------------- | -------------------------------------- | ---------------------------- |
| Internal Kick-Off<br><br>  <br>  <br><br>(PM, Team Lead) | 2                      | 60                                     | 120                          |
| Client Kickoff<br><br>  <br>  <br><br>(Client, PM)       | 2                      | 60                                     | 120                          |
|                                                          |                        | Total Time Spend on Kick-Off (Minutes) | 240                          |
|                                                          |                        | Total Time in Hours                    | 4                            |

#### Option 2

Merge Internal and Client Kickoff

| **Name**                         | **No of Participants** | **Planned Time(Minutes)**              | **Total Man Time(Minutes)** |
| -------------------------------- | ---------------------- | -------------------------------------- | --------------------------- |
| Kick-Off (PM, Team Lead, Client) | 3                      | 60                                     | 180                         |
|                                  |                        | Total Time Spend on Kick-Off (Minutes) | 180                         |
|                                  |                        | Total Time in Hours                    | 3                           |

## Capability Level

- The capability level reflects on how well an organization is aligned to a specific process area.
- There are six capability levels designated by the numbers 0 through 5 and each level is a next step to the continuous improvement.

## Components

3 components which derive maturity and capability

### Process Area

A cluster of related practices in an area that, when implemented collectively, satisfies a set of goals considered important for making improvement in that area.

### Generic Practices

The generic practices associated with a generic goal describe the activities that are expected to result in achievement of the generic goal and contribute to the institutionalization of the processes associated with a process area.

### Specific Practice

The specific practices describe the activities expected to result in achievement of the specific goals of a process area.

---

- There are 24 process areas.
- Each area is associated with a maturity level.
- Each area has set of standard practices which help increment maturity level.
- Process areas are views as
	- Continuous: the organization chose the processes that are critical to its business and achieve high capability levels.
	- Staged: Organization using this approach achieve the goals of the process areas associated each maturity level.

---

## Process Areas

### Requirement Management

- The major purpose behind this is to ensure alignment between the requirements, project plans and the final output.
- One part of requirement management is to document the entire requirement, any changes in requirement along with their rationale.

#### Goals

- To manage inconsistencies between products and Requirements
- To manage different versions of Requirements
- To manage correlation between different project deliverable and requirements
- Traceability Matrix to be used to manage cross referencing

#### Example

- **Understanding Requirement**: Develop an understanding with the requirements providers on the meaning of the requirements.
- **Obtain Commitment to Requirements**: Obtain commitment to requirements from project stakeholders.
- **Manage Requirements Changes**: Manage changes to requirements as they evolve during the project using Change Management Process by performing Impact Analysis.
- **Maintain Bidirectional Traceability of Requirements**: When requirements are managed well, traceability can be established from a source requirement to its lower level requirements and from those lower level requirements back to their source requirements.
- **Identify Inconsistencies**: Ensure that project plans and work products remain aligned with requirements.

### Requirement Development

- Customer requirements are further divided into Product and Project Requirements.
- Requirements are identified and refined throughout the phases of the product lifecycle.
- All the requirements should be documented, analyzed and approved by the client and the source trace should be maintained.
- Major Artifact is SRS.

#### Goals

- **Develop Customer Requirements**: Stakeholder needs, expectations, constraints, and interfaces are collected and translated into customer requirements.
- **Develop Product Requirements**: Customer requirements are refined and elaborated to develop product and product component requirements.
- **Analyze and Validate Requirements**: The requirements are analyzed and validated.

### Technical Solutions

- This process area is all about selection, design and implementation of solutions to the requirement of the product/project.
- The selected solution should produce the required output (requirement) and the solution must also tell that which requirement it is going to fulfill.

#### Goals

- **Select Product Component Solutions**: Product or product component solutions are selected from alternative solutions.
- **Develop the Design**: Product or product component designs are developed.
- **Implement the Product Design**: Product components, and associated support documentation, are implemented from their designs.

Main artifact is Technical Design Document (TDD).

### Product Integration

- Major failure occurs when the product components are either failed to integrate with each other or partially integrate which results in defects due to misaligned interfaces.
- Only few components are integrated and tested first and then more components are assembled.

#### Goals

- **Ensure Interface Compatibility**: The product component interfaces, both internal and external, are compatible.
- **Assemble Product Components and Deliver the Product**: Verified product components are assembled and the integrated, verified, and validated product is delivered.

#### Example

![[adv_e_1.svg]]

### Software Validation

#### Goals

- **Prepare for Validation**: Preparation for validation is conducted by selecting 
	- the product
	- validation environment 
	- validation criteria
- **Validate Product or Product Components**: The product or product components are validated to ensure they are suitable for use in their intended operating environment.

### Software Verification

- Verification is more concerned with building the product right way
- Software verification includes 
	- testing
	- design analysis
	- inspections 
	- code reviews

## Audits

- Through audits, organizations check 
	- Level of compliance 
	- Reason behind the nonconformance
- Reasons can be
	- People are not provided with
		- Required resources
		- Training to follow the process
	- Process is misaligned with working model

### Types

- **First Party Audits**: These (internal audits) are done by supplier company.
- **Second Party Audits**: These (external audits) are done by customer or a contracted organization on behalf of the customer.
- **Third Party Audits**: These (external audits) are done by audit organization independent of both.

