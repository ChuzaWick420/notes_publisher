---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Risks of Inadequate Requirements

Without proper requirements, it can lead to production of products which is unacceptable by the end users (`stake holders`).  
We need to closely work with the users to define the requirements.  
Creeping user requirements can also lead to cost overrun.  
When changes are requested in the later stage of development, the cost is high.  
![[Pasted image 20240428062955.png]]

Ambiguous requirements lead towards time spent on doing something wrong and then re-working again.  
This can happen due to poor language and different interpretation of it by different readers

**Example**: The operator identity consists of the operator name and password; the password  
consists of six digits. It should be displayed on the security VDU and deposited in the  
login file when an operator logs into the system.

Now what does _it_ mean here? does it mean _operator, identity_ or _operator name_ or _password_?

**Gold Plating**: This is a process in which developers and users add unnecessary features to the product (which are not specified in the requirements) thinking that it will add value to the product which results in time and budget overrun.

**Minimal specifications**: This leads to a product which does what the requirement statement says but lacks the major functionalities.

# Levels of Software Requirements

We define the requirements at different levels to focus on different aspects of the project.

**Business Requirements**: These are captured to define the business objectives without going into the details. It is written in the project's vision.  
**Example statement**: "Add a spell checker to the word processor such that user can correct errors."

**User requirements**: These add further details to business requirements. These are written from user's perspective that what the users want.  
**Example statement**: "finding spelling errors in the document and decide whether to replace each misspelled word with the one chosen from a list of suggested words."

**Functional requirements**: This focuses on the fact that developers make features which the users desired (or helps them accomplish their tasks).  
**Example statement**: "the spell checker will find and highlight misspelled words. It will then display a dialog box with suggested replacements. The user will be allowed to select from the list of suggested replacements. Upon selection it will replace the misspelled word with the selected word. It will also allow the user to make global replacements."

**Non functional requirements**: These requirements include constraints and other quality and performance attributes.  
**Example statement**: "it must be integrated into the existing word-processor that runs on windows platform."

When writing the requirements, the levels should be derived from one another and be aligned (such as: the _functional_ requirements should align with _user's_ requirements which should align with _business_ requirements).

# Stake Holders

![[Pasted image 20240428071201.png]]  
_Requirement Statement_ is the _user requirements_.  
_Requirement Specification_ is the _functional requirements_.

# Characteristics of Requirement Statement

1. It should be _complete_, meaning each statement is fully defined.
2. It should be _unambiguous_, meaning every reader should get the same idea.
3. It should be _necessary_, meaning it should be something user really wants.
4. It should be _feasible_, meaning, judging from the limitations, capabilities and environment of the project, it should be possible to implement.
5. It should be _verifiable_, meaning the user can _test_ if the requirement is fulfilled or not.

# Characteristics of Requirement Specification

1. It should be _complete_, meaning no requirement is missing.
2. It should be _consistent_, meaning no requirement conflicts with one another.
3. It should be _modifiable_, meaning the changes in specifications (when necessary) should be able to be tracked.
4. It should be _traceable_, meaning, each requirement should be linked to its the source code, unit tests etc.

# Mixed Level of Abstraction

The level of abstraction should be uniform throughout the document, otherwise it can misguide workers involved in the project on the importance of tasks.  
**Example**:
1. The purpose of the system is to track the stock in a warehouse.
2. When a loading clerk types in the withdraw command he or she will communicate the order number, the identity of the item to be removed, and the quantity removed. The system will respond with a confirmation that the removal is allowable.
