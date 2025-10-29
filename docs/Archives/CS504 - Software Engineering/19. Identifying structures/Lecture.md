---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Identifying Spec-gen Structures

## Kind of Stores

A store of a kind of sales outlet.  
Connie might expand to other sales outlets so for now, leave the store as it is.

## Kind of Sales

- Sales, return
- Only difference is that these might be positive or negative.

## Prices

- Regular price 
- Promotional sales price

## Payment

- Cash
- Check
- Charge  
![[Pasted image 20240723134742.png]]

# Identifying Whole-part Structures

- A store as a whole is made up of cashiers, registers and items
- A register contains a cash drawer
- A sale is constituted of sale line items  
![[Pasted image 20240723135218.png]]

# Establishing Responsibilities

## Who I Know - Rules of Thumb

- an #actors knows about its #participant.
	- person knows about cashier
- a `transaction` knows about its #participant.
	- a `session` knows about its `register` and `cashier`
- a `transaction` contains its `transaction line items`
	- `sale` contains its `sale line items`
- a `transaction` knows about its `sub transactions`
	- `session` knows about its `sales`
	- `sale` knows about its `payments`
- a `place` knows about its `transactions`
	- `store` knows about its `sessions`
- a `place` knows about its `descriptive objects`
	- `store` knows about its `tax categories`
- a `container` knows about its `contents`
	- `store` knows about its `cashiers`, `items`, `registers`

# Define Attributes, Services and Links - what I Know, what I Do, Who I Know

## Actors

`person`

### Attributes

- name
- address
- phone

### Services

## Participants

`cashier`

### Attributes

- number
- password
- authorization level
- current session

### Services

- isAuthorized
- assess
- Performance

## Places

`store`

### Attributes

- name

### Services

- get item for UPC
- get cashier for number

## Tangible Things

- `item`

### Attributes

- number
- description
- UPCs
- prices
- taxable
- attributes with repeating names - create new objects
	- UPC
	- Price (specialization - promotional price)

### Services

- get price for a date
- how much for quantity

### Who I Know?

- UPC  
- Price  
- Tax Category
- Sale line item

- `register`

### Attributes

- number

### Services

- How much over interval
- How many over interval

### Who I Know?

- Store
- Session
- Cash drawer (part of register)

- `cash drawer`

### Attributes

- balance
- position (open, close)
- Operational state

### Services

- open

### Who I Know?

- register

- `Tax Category`

### Attributes

- category
- rate
- effective date

### Services

- get
- add
- set

### Who I Know?

- items

## Transactions

- `sale`

### Attributes

- date and time

### Services

- calculate subtotal
- calculate total
- calculate discount
- calculate tax
- commit

### Who I Know

- session
- payment
- SLIs

- `sale line item`

### Attributes

- date and time?
- quantity
- tax status (regular, resale, tax-exempt)

### Services

- calculate sub total

### Who I Know

- item
- sale

- `return`

### Attributes

- return price
- reason code
- sale date
- sale price

### Services

### Who I Know

- `payment`

### Attributes

- `payment`
	- amount paid
	- cash tendered
- `check object`
	- bank
	- account number
	- amount tendered
	- authorization code
- `credit object`
	- card type
	- card number
	- expiration date
	- authorization code

### Services

### Who I Know

- sale

![[Pasted image 20240723150152.png]]

- `session`

### Attributes

- start date
- end date
- start time
- end time

### Services

- how much money collected over interval
- how many sales

### Who I Know

- register
- cashier
- store
- sales
