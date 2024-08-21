# Thread vs Process

## What is a thread?

Threads share a process and are therefore dependent on one another; they share the same memory space. Unlike
a process though threads take less time to terminate.

The states of a thread include:
- Running
- Ready
- Blocked

## What is a process?

Processes are scheduled in the CPU from their ready state. Memory is not shared with other processes.
Failures in one process do not impact one another. 

The states of a process include:
- New
- Ready
- Running
- Waiting
- Suspended
- Terminated

## Resources

1. [Geeks for Geeks](https://www.geeksforgeeks.org/difference-between-process-and-thread/)