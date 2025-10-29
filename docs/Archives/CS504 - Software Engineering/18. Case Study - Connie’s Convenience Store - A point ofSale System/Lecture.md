---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# The System

## Identifying the Purpose of the System

1. develop an overall purpose statement of 25 words or less. Why this system?
2. Keep the overall goal, critical success factor, always in front of you.
3. "To support, to help, to facilitate".

### Connie's Wish List

1. scan items and automatically price them
2. know whether an item is on sale
3. automatically total the sale and calculate tax
4. handle purchases and returns
5. handle payments with cash, check, or charge
6. authorize checks and cards
7. calculate change when working with cash or checks
8. record all of the information about a customer transaction
9. balance the cash in the drawer with the amount recorded by the point-of-sale system.

### Why?

1. speed up checkout time
2. reduce the number of pricing errors
3. reduce the labor required to ticket the item with a price, originally and when
4. prices change.

### Summary

to help each cashier work more effectively during checkout, to keep good records of each sale, and to store more efficient store operations.

## Identify System Features

### Logging Important Information

1. to maintain prices based upon UPC
2. to maintain tax categories (categories, rates, and effective dates)
3. to maintain the authorized cashiers
4. to maintain what items we sell in a store
5. to log the results of each sale in a store

### Conducting Business

1. to price each item, based upon its UPC
2. to subtotal, calculate tax, and total
3. to accept payment by cash, check, or charge

### Analyzing Business Results

1. to count how many of each item sold
2. to count how much we received in cash, check, or credit card sales
3. to assess how each cashier is performing
4. to assess how each store is performing

### Working with Interacting Systems

to obtain authorization from one or more credit (or check) authorization system.

# Selecting Objects

## Select Actors

1. Person

## Select Participants

1. cashier
2. head cashier
3. customer

If there is no difference between `cashier` and `head cashier` then they should be put into 1 common class.

## Select Places

1. Store
2. Shelf

The system doesn't keep track of the `shelf`.

## Select Transactions

1. sale
2. every sale is a collection of sale line items
3. return
4. payment
5. session

## Select Container Classes

1. cashiers
2. registers
3. items

## Select Tangible Things

1. item
2. register
3. cash drawer
4. Tax Category (Descriptive things)
