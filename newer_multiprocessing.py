import time
import concurrent.futures

start = time.perf_counter()

def doSomething(seconds):
    print("Hello")
    time.sleep(seconds)
    return "Bye"

with concurrent.futures.ProcessPoolExecutor() as executor:
    results = []
    for _ in range(10):
        f = executor.submit(doSomething, 1)
        results.append(f)
    for x in concurrent.futures.as_completed(results):
        print(x.result())

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')