# Python GIL

## What is the Python GIL?

The GIL - the global interpreter lock - is precisely that, it is a mutex - or a lock - used by Python to limit Python to have only one thread
controlling Python's execution/interpreter at any given time.

This doesn't impact single threaded programming but the impacts can be seen in CPU bound or multithreaded programming.

Python uses reference counting for memory management. For example:

```
import sys

>> a = []
>> b = a
>> sys.getrefcount(a)
3
```
1. Referenced `a` upon assigning it the value of `[]`
2. Referenced `a` when set assigned to value of `b`
3. Referenced `a` when passed to `getrefcount`

The GIL prevents issues with race conditions where the reference counting variable(s) need protection. If another thread tries to access the
variable(s) and change it's value simultaneously memory leaks can happen or other unintended side effects (e.g. release the object will it
is still being referenced).

To protect reference counting locks can be placed on data structures used across threads to limit access. This introduces other problems:
- Deadlocks (when 1+ lock)
- Performance degradation each time a lock is obtained/released

Enter the GIL - this requires that any Python bytecode needing to be executed must acquire the GIL to use the Python interpreter (other
languages like Ruby use this!). 

Other solutions though aside from the GIL can include:
- Garbage collection - this has it's own limits and requires work arounds for performance like JIT compilers

GIL was selected as it emerged in a time when threaded programming did not exist, it is also easy to implement. Working in C libraries 
also require thread safe memory management.

## What is the impact of multithreaded programming?

Two types of programming:
- I/O (Input/Output) bound -- when waiting for as the name says I/O e.g. waiting for user input, waiting for files, think the web!
- CPU (Central Processing Unit) bound -- expensive operations like matrix multiplication, machine learning computation, etc!

GIL is shared across threads in I/O as while waiting the GIL doesn't have to be used. But in CPU bound programming this isn't the 
case and the GIL must be shared. 

## Are there work arounds for dealing with the GIL?

Yes! Use `multiprocessing` vs multithreading. Multiprocessing introduces multiple Python interpreters and it's own memory space, ergo 
multiple GILs. Y'all it's `pool` time!

## More reading

1. [Real Python](https://realpython.com/python-gil/)