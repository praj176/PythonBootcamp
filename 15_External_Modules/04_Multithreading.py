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
import threading  # To create threads
import time       # To add delay using sleep()

# This is the function that each thread will run
def worker(num):
    print(f"Thread {num}: Starting")  # Print when a thread starts
    time.sleep(2)                     # Simulate some work by waiting 2 seconds
    print(f"Thread {num}: Finishing") # Print when a thread finishes

threads = []  # Create an empty list to keep track of all thread objects

# Start 3 threads
for i in range(3):
    # Create a Thread object that will run the 'worker' function with argument 'i'
    thread = threading.Thread(target=worker, args=(i,))
    
    threads.append(thread)  # Add the thread to our list
    
    thread.start()  # Start running the thread (calls the worker() function in parallel)

# Wait for all threads to finish before moving on
for thread in threads:
    thread.join()   # This makes sure the main program waits until this thread is done

# After all threads are finished, print this
print("All threads completed")

