---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Object Oriented Analysis
The intent of object oriented analysis is to define all `classes`, their `relationships` and their `behaviors`.

The tasks involved are:
1. Static Model
	1. Identify classes (`attributes` and `methods` are defined)
	2. Specify class hierarchy
	3. Identify object-to-object relationships
	4. Model the object behavior
2. Dynamic Model
	1. Scenario diagrams

# Object Oriented Design
OOD transforms the analysis model into design model which serves as a blueprint for our software.  
There are `4` layers of OOD pyramid:
1. **The subsystem layer:** Representation of each of the subsystems which enable our software to fulfil customer requirements and act as a blueprint for technical infrastructure for those requirements.
2. **The class and object layer:** This layer contains the class hierarchies including `generalizations` and `specializations` along with the design representation of each object.
3. **The message layer:** This layer specified the internal and external `interfaces` the objects will have in order to communicate with each other.
4. **The responsibility layer:** This layer contains the #data-structures and #algorithms to handle the `attributes` and `methods` of the `objects`.

# Abbot’s Textual Analysis
This technique of identifying objects is one of the oldest.  
Parts of speech are identified and then are modeled.  
![[Pasted image 20240525183110.png]]

## Example
### Problem Statement
A simple cash register has a display, an electronic wire with a plug, and a numeric keypad, which has keys for subtotal, tax, and total. This cash storage device has a total key, which triggers the release on the drawer. The numeric buttons simply place a number on the display screen, the subtotal displays the current total, the tax key computes the tax, and the total key adds the subtotal to the tax.

### Tasks
1. Identify all the classes in this problem statement.
2. Eliminate the unnecessary classes.

#### Nouns(initial)
- Register 
- Display 
- Wire
- Plug
- Keypad 
- Keys
- Devices 
- Release 
- Drawer
- Buttons 
- Screen
- Number
- Total
- Tax

#### Nouns(general knowledge)
- 0-9 keys 
- Money
- Tax Key 
- Total Key
- Subtotal Key

#### Eliminating Irrelevant / Redundant Nouns
- Register
- Display
	- <span style="color:red;">Wire</span>, Irrelevant
	- <span style="color:red;">Plug</span>, Irrelevant
- Keypad
- Keys
	- <span style="color:red;">Devices</span>, vague 
	- <span style="color:red;">Release</span>, Irrelevant
- Drawer
	- <span style="color:red;">Buttons</span>, redundant
	- <span style="color:red;">Screens</span>, redundant 
	- <span style="color:red;">Number</span>, attribute 
	- <span style="color:red;">Total</span>, attribute 
	- <span style="color:red;">Total</span>, attribute 
- 0-9 Key
	- <span style="color:red;">Value</span>, attribute 
- Money
- Subtotal Key
- Tax Key
- Total Key
