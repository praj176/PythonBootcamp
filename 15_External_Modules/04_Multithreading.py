'''
Multi-threading allows your program to perform multiple tasks concurrently, which improves the performance

> Threads and processes are like the building blocks of multitasking
A process is an independent program in execution. It has it's own memory space, it's own resources (like file handles, variables, etc.)
---> At least one thread running inside it

> A thread is a smaller unit of execution within a process. Multiple threads in the same process:
Share the same memory and resources. Can run tasks in parallel (like multitasking within the same app)

Eg : Process can be considered as restaurant and threads can be considered as chefs.
'''
import threading
import time
'''
Used the threading module to run multiple tasks simultaneously, improving efficiency during wait times like file downloads or API responses
eg : like downloading and working at the same time without waiting.
'''
