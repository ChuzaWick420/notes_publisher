---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-12-04
---

<span style="color: gray;">Dated: 04-12-2024</span>

# Ch03. case Study Security Hardening - c++ Applications

- Carnegie Mellon Software Engineering Institute
- https://wiki.sei.cmu.edu/confluence/pages/viewpage.action?pageId=88046682

- Rule 01. Declarations and Initialization (DCL)
- Rule 02. Expressions (EXP)
- Rule 03. Integers (INT)
- Rule 04. Containers (CTR)
- Rule 05. Characters and Strings (STR)  
- Rule 06. Memory Management (MEM)
- Rule 07. Input Output (FIO)
- Rule 08. Exceptions and Error Handling (ERR)Page:
- Rule 09. Object Oriented Programming (OOP)
- Rule 10. Concurrency (CON)
- Rule 10. Concurrency (CON)
- CON50-CPP. Do not destroy a mutex while it is locked
- Mutex objects are used to protect shared data from being concurrently accessed. If a mutex object is destroyed while a thread is blocked waiting for the lock, critical sections and shared data are no longer protected.
- The C++ Standard, `thread.mutex.class`, paragraph 5 `ISO/IEC 14882-2014`, states the following:
- The behavior of a program is undefined if it destroys a mutex object owned by any thread or a thread terminates while owning a mutex object.

```cpp
#include <mutex>
#include <thread>

const size_t maxThreads = 10;
void do_work(size_t i, std::mutex *pm) {
	std::lock_guard<std::mutex> lk(*pm);

	// Access data protected by lock
}

void start_threads() {
	std::thread theads[maxThreads];
	std::mutex = m;

	for (size_t i = 0; i < maxThreads; ++i) {
		threads[i] = std::thread(do_work, i, &m);
	}
}
```

- Non-Compliant Code Example:
- This noncompliant code example creates several threads that each invoke the do_work() function, passing a unique number as an ID.
- Unfortunately, this code contains a race condition, allowing the mutex to be destroyed while it is still owned, because start_threads() may invoke the mutex's destructor before all of the threads have exited.

```cpp
#include <mutex>
#include <thread>

const size_t maxThreads = 10;
void do_work(size_t i, std::mutex *pm) {
	std::lock_guard<std::mutex> lk(*pm);

	// Access data protected by lock
}

std::mutex = m;
	
void start_threads() {
	std::thread theads[maxThreads];

	for (size_t i = 0; i < maxThreads; ++i) {
		threads[i] = std::thread(do_work, i, &m);
	}
}
```

- Compliant Code Example:
- This compliant solution eliminates the race condition by extending the lifetime of the mutex.
