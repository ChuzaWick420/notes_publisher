---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

<span style="color: gray;">Dated: 25-10-2024</span>

# Lecture No. 1

## What Does Automata Means?

It is the plural of `automaton`, and it means "something that works automatically".

## Introduction to Languages

There are 2 types of languages

1. Formal (Syntactic languages).
2. Informal (Semantic languages).

## Alphabets

A finite non empty `set`[^1] of `symbols` (called `letters`) is called an `alphabet` and is represented by the Greek letter $\Sigma$.  
It includes `letters`, `digits` and variety of `operators` such as `GOTO` and `IF`.

### Example

Certain versions of `ALGOL` has 113 `letters`.  
The `binary language` has the `alphabet`  

$$\Sigma = \{1, 0\}$$

## Strings

Concatenation of finite number of `letters` from the `alphabet` is called a `string`.

### Example

If $\Sigma = \{a, b\}$ is the [alphabet](#alphabets) then $ab$ and $abaaab$ are both `strings`.

## Null String

A `string` consisting of no `letters` at all, is called `null string` or `empty string`.  
It is denoted by Greek letters $\lambda$ or $\Lambda$.

## Words

`Words` are [strings](#strings) belonging to some `language`.

### Example

If $\Sigma = \{x\}$ then `language` $L$ can be defined as:  

$$L = \{x^n : n = 1, 2, 3, \ldots\}$$

or  

$$L = \{x, xx, xxx, \dots\}$$

The $x$, $xx$ and $xxx$ are the `words` of `language` $L$.

> NOTE: All [words](#words) are [strings](#strings) but not all [strings](#strings) are [words](#words).

## Valid and Invalid Alphabets

While defining an [alphabet](#alphabets), an [alphabet](#alphabets) may consist of a group of `symbols`.  

$$\Sigma = \{B, aB, bab, d\}$$

Now consider the following [alphabet](#alphabets).  

$$\Sigma = \{B, Ba, bab, d\}$$

and then consider a [string](#strings) $BababB$.  
It can be `tokenized` into following ways:

1. $Ba$, $bab$ and $B$
2. $B$, $abab$ and $B$

The _2nd_ way is problematic, here's why.  
When the `compiler` (`Lexical Analyzer`) scans the [string](#strings), the _1st_ `symbol` $B$ is recognized to be part of the [alphabet](#alphabets) but the _2nd_ `symbol` $abab$ is not recognized.

> NOTE: While defining an [alphabet](#alphabets), any 2 or more `symbols` should NOT start with same `letter`.

## Length of a String

If $s$ is a [string](#strings) then $|s|$ is called the `length of string`.

### Example

$$\Sigma = \{a, b\}$$

$$s = ababa$$

$$\text{Tokenization} = a, b, a, b, a$$

$$|s| = 5$$

### Example

$$\Sigma = \{B, aB, bab, d\}$$

$$s = BaBbabBd$$

$$\text{Tokenization} = B, aB, bab, B, d$$

$$|s| = 5$$

## Reverse of a String

The reverse of a [string](#strings) is denoted as $Rev(s)$ or $s^r$ and consists of `letters` of $s$ but in reverse order.

### Example

$$\Sigma = \{a, b, c\}$$

$$s = abc$$

$$\text{Tokenization} = a, b, c$$

$$Rev(s) = s^r = cba$$

### Example

$$\Sigma = \{B, aB, bab, d\}$$

$$s = BaBbabBd$$

$$\text{Tokenization} = B, aB, bab, B, d$$

$$Rev(s) = s^r = dBbabaBB$$

## Defining Languages

`Languages` can be defined in different ways:

- Descriptive definition
- Recursive definition
- Regular Expressions
- Finite Automaton

### Descriptive Definition

The `language` is defined, describing the conditions imposed on its words.

#### Example

`Language` $L$ of [strings](#strings) of `odd lengths` defined over $\Sigma = \{a\}$ can be written as  

$$L = \{a^{2n + 1}: n = 0, 1, 2, \ldots\}$$

$$L = \{a, aaa, aaaaa, \ldots\}$$

## Palindrome

It is a `language` defined over $\Sigma$ consisting of $\Lambda$ and $s$ such that  

$$Rev(s) = s$$

> `Palindromes` can exist as [strings](#strings) of both lengths $2n - 1$ and $2n$.

## References

[^1]: Read more about [[Mathematics/Set/Content|sets]].