---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-12-04
---

<span style="color: gray;">Dated: 04-12-2024</span>

# Ch03. case Study Security Hardening - Java Applications

- Carnegie Mellon Software Engineering Institute
- https://wiki.sei.cmu.edu/confluence/display/java/SEI+CERT+Oracle+Coding+Standard+for+Java  
![[Pasted image 20241204071257.png]]  
![[Pasted image 20241204071315.png]]  
![[Pasted image 20241204071331.png]]
- Rule 7
- ERR02-J. Prevent exceptions while logging data
- Exceptions that are thrown while logging is in progress can prevent successful logging unless special care is taken. Failure to account for exceptions during the logging process can cause security vulnerabilities, such as allowing an attacker to conceal critical security exceptions by preventing them from being logged. Hence, programs must ensure that data logging continues to operate correctly even when exceptions are thrown

```java
try {
	// ...
}

catch (SecurityException se) {
	System.err.println(se);
	// Recover from exception
}
```

- Non-compliant Code Example:
- This noncompliant code example writes a critical security exception to the standard error stream:
- Writing such exceptions to the standard error stream is inadequate for logging purposes. First, the standard error stream may be exhausted or closed, preventing recording of subsequent exceptions. Second, the trust level of the standard error stream may be insufficient for recording certain security-critical exceptions or errors without leaking sensitive information. If an I/O error were to occur while writing the security exception, the catch block would throw an IOException and the critical security exception would be lost. Finally, an attacker may disguise the exception so that it occurs with several other innocuous exceptions.

```java
try {
	// ...
}

catch (SecurityException se) {
	logger.log(Level.SEVER, se);
	// Recover from exception
}
```

- Compliant Solution:
    - This compliant solution uses java.util.logging.Logger, the default logging API provided by JDK 1.4 and later. Use of other compliant logging mechanisms, such as log4j, is also permitted.
- Typically, only one logger is required for the entire program.
