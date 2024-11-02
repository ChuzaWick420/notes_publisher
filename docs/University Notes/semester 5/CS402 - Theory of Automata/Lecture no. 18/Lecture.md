---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-02
---

<span style="color: gray;">Dated: 02-11-2024</span>

# Lecture No. 18

## Example

### $FA_1$

```mermaid
stateDiagram-v2
state1: p-
state2: q
state3: +

state1-->state1 : b
state1-->state2 : a
state2-->state1 : b
state2-->state3: a
state3 --> state3 : a, b
```

### $FA_2$

```mermaid
stateDiagram-v2
s1 : 1-
s2 : 2
s3 : 3
s4 : 4
s5 : 5
s6 : 6+

s1 --> s2 : a
s2 --> s4 : a
s4 --> s6 : a
s6 --> s6 : a, b
s1 --> s3 : b
s3 --> s5 : b
s5 --> s6 : b
s4 --> s3 : b
s5 --> s2 : a
s2 --> s3 : b
s3 --> s2 : a
```

#### `Non Deterministic Finite Automaton`[^1] For $FA_1 \cup FA_2$

```mermaid
stateDiagram-v2
s1 : -
p : p
q : q
+ : +
1 : 1
2 : 2
3 : 3
4 : 4
5 : 5
6+ : 6+

s1 --> p : b
s1 --> q : a
s1 --> 2 : a
s1 --> 3 : b
p --> p : b
p --> q : a
q --> p : b
q --> + : a
+ --> + : a, b

1 --> 2 : a
1 --> 3 : b
2 --> 3 : b
2 --> 4 : a
3 --> 5 : b
3 --> 2 : a
4 --> 6+ : a
4 --> 3 : b
5 --> 2 : a
5 --> 6+ : b

6+ --> 6+ : a, b
```

## `Non Deterministic Finite Automaton`[^1] For $FA_1 FA_2$

### Method

From the first `finite automaton`,[^2] introduce new `states` which connect the `final states` to 2nd `finite automaton`'s[^2] `states` which are connect to its own(the 2nd `finite automaton`[^2]) `initial states`.

There are some possible routes we can take depending on if the `finite automata`[^2] accept a `null string`[^3] or not

#### $FA_1$ And $FA_2$ Does not Accept $\Lambda$

##### $FA_1$

```mermaid
stateDiagram-v2
state1: p-
state2: q
state3: r+

state1-->state1 : b
state1-->state2 : a
state2-->state1 : b
state2-->state3: a
state3 --> state3 : a, b
```

##### $FA_2$

```mermaid
stateDiagram-v2
s1 : 1-
s2 : 2
s3 : 3
s4 : 4
s5 : 5
s6 : 6+

s1 --> s2 : a
s2 --> s4 : a
s4 --> s6 : a
s6 --> s6 : a, b
s1 --> s3 : b
s3 --> s5 : b
s5 --> s6 : b
s4 --> s3 : b
s5 --> s2 : a
s2 --> s3 : b
s3 --> s2 : a
```

##### `Non Deterministic Finite Automaton`[^1] For $FA_1 FA_2$

```mermaid
stateDiagram-v2
p : p-
q : q
r : r
1 : 1
2 : 2
3 : 3
4 : 4
5 : 5
6+ : 6+

p --> p : b
p --> q : a
q --> r : a
q --> p : b
r --> r : a, b
r --> 2 : a
r --> 3 : b
1 --> 2 : a
1 --> 3 : b
2 --> 3 : b
2 --> 4 : a
3 --> 2 : a
3 --> 5 : b
4 --> 3 : b
4 --> 6+ : a
5 --> 4 : a
5 --> 6+ : b
6+ --> 6+ : a, b
```

#### $FA_2$ Accepts $\Lambda$ but $FA_1$ Does not

##### $FA_1$

```mermaid
stateDiagram-v2
state1: p-
state2: q
state3: r+

state1-->state1 : b
state1-->state2 : a
state2-->state1 : b
state2-->state3: a
state3 --> state3 : a, b
```

##### $FA_2$

```mermaid
stateDiagram-v2
x : $x\pm$
y : y

x --> y : a, b
y --> x : a, b
```

##### `Non Deterministic Finite Automaton`[^1] For $FA_1 FA_2$

```mermaid
stateDiagram-v2
p : p-
r : r+
x : x+



p --> q : a
p --> p : b

q --> p : b
q --> r : a

r --> r : a, b
r --> y : a, b

y --> x : a, b
x --> y : a, b
```

#### Both $FA_1$ and $FA_2$ Accept $\Lambda$

##### $FA_1$

```mermaid
stateDiagram-v2
x : $x\pm$
y : y

x --> y : a, b
y --> x : a, b
```

##### $FA_2$

```mermaid
stateDiagram-v2
1 : $1\pm$



1 --> 2 : a
1 --> 3 : b

2 --> 1 : a
2 --> 4 : b

3 --> 1 : b
3 --> 4 : a

4 --> 2 : b
4 --> 3 : a
```

##### `Non Deterministic Finite Automaton`[^1] For $FA_1 FA_2$

```mermaid
stateDiagram-v2
1 : $1\pm$
s : $\pm$


s --> y : a, b
s --> 3 : b
s --> 2 : a

y --> s : a, b

1 --> 2 : a
1 --> 3 : b

2 --> 1 : a
2 --> 4 : b

3 --> 1 : b
3 --> 4 : a

4 --> 2 : b
4 --> 3 : a
```

## `Non Deterministic Finite Automaton`[^1] For $FA^*$

### Method

The method is rather confusing to be stated in one paragraph so I will define it step by step with an example visualization.

#### Example

Consider the following `finite automaton`[^2]  
![[cs402_18_d_1.svg]]  
Because the $FA^*$ can accept a $\Lambda$, therefore we will introduce a `state` which is both, `initial` and `final`.  
![[cs402_18_d_2.svg]]  
Then we will connect it to the `states` which are connected to old `initial state` through the same transitions.  
![[cs402_18_d_3.svg]]  
In similar fashion, we will connect the old `final state` as well and remove the $-$ sign for old `initial state`.  
![[cs402_18_d_4.svg]]

## References

[^1]: Read more about [[semester 5/CS402 - Theory of Automata/Lecture no. 15/Lecture|non deterministic finite automaton]].
[^2]: Read more about [[notes_publisher/docs/University Notes/semester 5/CS402 - Theory of Automata/Lecture no. 4/Lecture|finite automaton]].
[^3]: Read more about [[notes_publisher/docs/University Notes/semester 5/CS402 - Theory of Automata/Lecture no. 1/Lecture|strings]].