import time
import multiprocessing

start = time.perf_counter()

def doSomething(seconds):
    print("Hello")
    time.sleep(seconds)
    print("Bye")

"""
#This is running these programs synchronously.  
doSomething()
doSomething()
"""

"""
#An old way to do multiprocessing.  A way to run the same function twice, but at the same time.  
process1 = multiprocessing.Process(target = doSomething)
process2 = multiprocessing.Process(target = doSomething)

#Starts the process.
process1.start()
process2.start()

#Process will finish before moving on in the script.  
process1.join()
process2.join()
"""

#Rather than spelling out each process, we can loop through to do the same thing.
#We have to append each process to a list so we can join them all in a later loop.  
#If we had the join statement in this loop, it would be the same as executing synchronously.  
#Arguments need to be passed as lists. 
processes = []  
for _ in range(10):
    process = multiprocessing.Process(target = doSomething, args = [1.5])
    process.start()
    processes.append(process)

for process in processes:
    process.join()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')