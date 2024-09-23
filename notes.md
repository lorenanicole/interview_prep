# What Are Python Threads

A thread refers to a thread of execution by a computer program.

Every Python program is a process with one thread called the main thread used to execute your program instructions. Each process is in fact one instance of the Python interpreter that executes Python instructions (Python byte-code), which is a slightly lower level than the code you type into your Python program.

Sometimes, we may need to create additional threads within our Python process to execute tasks concurrently.

Python provides real naive (system-level) threads via the threading.Thread class.

# Multithreading vs multiprocessing?

A process is what we call a program that has been loaded into memory along with all the resources it needs to operate. It has its own memory space.

A thread is the unit of execution within a process. A process can have multiple threads running as a part of it, where each thread uses the process’s memory space and shares it with other threads.

Multithreading is a technique where multiple threads are spawned by a process to do different tasks, at about the same time, just one after the other. This gives you the illusion that the threads are running in parallel, but they are actually run in a concurrent manner. In Python, the Global Interpreter Lock (GIL) prevents the threads from running simultaneously.

Multiprocessing is a technique where parallelism in its truest form is achieved. Multiple processes are run across multiple CPU cores, which do not share the resources among them. Each process can have many threads running in its own memory space. In Python, each process has its own instance of Python interpreter doing the job of executing the instructions.

# Python's GIL

CPython implementation detail: In CPython, due to the Global Interpreter Lock, only one [thread](https://docs.python.org/3/library/threading.html) can execute Python code at once (even though certain performance-oriented libraries might overcome this limitation). If you want your application to make better use of the computational resources of multi-core machines, you are advised to use multiprocessing or concurrent.futures.ProcessPoolExecutor. However, threading is still an appropriate model if you want to run multiple I/O-bound tasks simultaneously.

# What's a race condition?



- GIL - global interpreter lock, a mutex, only allows the Python intepreter to have 1 lock for the interpreter, so at any one given moment of time only one thread can be in a state of execution 
- Has to do with the way Python was implemented before true threading programming existed, Python uses ref count for memory management, "memory management technique in which the objects are deallocated when there is no reference to them in a program"
- But without a lock in threaded type programming can have memory leak

```
>>> import sys
>>> s = "hello, world"
>>> sys.getrefcount(s)
2
>>> s2 = s
>>> sys.getrefcount(s)
3
```
- Since Python uses reference counting Python needed protection from race conditions where two threads increase or decrease ref count variables values simultaneously
- The GIL is simple to implement and was easily added to Python. It provides a performance increase to single-threaded programs as only one lock needs to be managed.

# What is a race condition?

- Example - Python's use of reference counting!
- Happens when two+ computer program processes, or threads, attempt to access the data and change it simultaneously
- The result in the change to data let's to a race of which thread will mutate the shared data

```

import threading 
  
# global variable x 
x = 0
  
def increment(): 
    """ 
    function to increment global variable x 
    """
    global x 
    x += 1
  
def thread_task(): 
    """ 
    task for thread 
    calls increment function 100000 times. 
    """
    for _ in range(100000): 
        increment() 
  
def main_task(): 
    global x 
    # setting global variable x as 0 
    x = 0
  
    # creating threads 
    t1 = threading.Thread(target=thread_task) 
    t2 = threading.Thread(target=thread_task) 
  
    # start threads 
    t1.start() 
    t2.start() 
  
    # wait until threads finish their job 
    t1.join() 
    t2.join() 
  
if __name__ == "__main__": 
    for i in range(10): 
        main_task() 
        print("Iteration {0}: x = {1}".format(i,x)) 
```