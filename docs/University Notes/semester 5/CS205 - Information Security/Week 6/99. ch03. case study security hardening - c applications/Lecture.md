---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-12-04
---

<span style="color: gray;">Dated: 04-12-2024</span>

# Ch03. case Study Security Hardening - C Applications

- Carnegie Mellon Software Engineering Institute
- https://wiki.sei.cmu.edu/confluence/display/seccode/SEI+CERT+Coding+Standards
- https://wiki.sei.cmu.edu/confluence/display/c/SEI+CERT+C+Coding+Standard

- There are existing compiler implementations that allow const-qualified objects to be modified without generating a warning message.
- Avoid casting away const qualification because doing so makes it possible to modify const-qualified objects without issuing diagnostics.

```c
const int **ipp;
int *ip;
const int i = 42;

void func(void) {
	ipp = &ip; // Constraint Violation
	*ipp = &i; // Valid
	*ip = 0    // Modifies constant i (was 42)
}
```

- The first assignment is unsafe because it allows the code that follows it to attempt to change the value of the const object i.

```c
int **ipp;
int *ip;
int i = 42;

void func(void) {
	ipp = &ip; // valid 
	*ipp = &i; // valid 
	*ip = 0    // valid 
}
```

- The compliant solution depends on the intent of the programmer. If the intent is that the value of i is modifiable, then it should not be declared as a constant, as in this compliant solution:
- If the intent is that the value of i is not meant to change, then do not write noncompliant code that attempts to modify it.
- Risk Assessment
- Automated detection
- Related vulnerabilities
