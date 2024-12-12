import helper
import time
import numpy as np

desired_result = 2020
file_path = "inputs/day1/p1.txt"

def p1():
    _ = 0
def p2():
    _ = 0
    
if __name__ == '__main__':
    iterations = 1
    start_time = time.perf_counter()
    for i in range(0, iterations):
        # res1 = p1()
        res1 = p1()
        if (i % (iterations/10) == 0): print(f"{i} of {iterations}",end='\r')
    end_time = time.perf_counter()
    print(f"Elapsed time of {iterations} iterations: {(end_time-start_time) * 1000} ms\n\tAverage time per run is {(end_time-start_time)*1000/iterations} ms")
    
    start_time = time.perf_counter()
    for i in range(0, iterations):
        if (i % (iterations/10) == 0): print(f"{i} of {iterations}",end='\r')
        res2 = p2()
    end_time = time.perf_counter()
    print(f"Elapsed time of {iterations} iterations: {(end_time-start_time) * 1000} ms\n\tAverage time per run is {(end_time-start_time)*1000/iterations} ms")
    
    print(f"{res1} {res2}")
    