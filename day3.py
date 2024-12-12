import helper
import time
import numpy as np
import re

desired_result = 2020
file_path = "inputs/day3/p1.txt"

def p1():
    data = helper.read_into_string(file_path)
    
    matches = re.findall("mul\\(\\d*,\\d*\\)", data)
    total = 0
        
    for match in matches:
        delim = match.find(',')
        n1 = int(match[4: delim]) # mul is always length 3
        n2 = int(match[delim + 1:-1]) # all but final char
        total += n1 * n2

    return total
def p2():
    data = helper.read_into_string(file_path)
    dont_as_last_cmd = False
    curr_ind = 0
    
    dont_inds = [m.start() for m in re.finditer("don't", data)]
    do_inds = [m.start() for m in re.finditer("do[^n]", data)]
    # print(f"pre  processing: {data}")
    
    for dont_ind in dont_inds:
        while (do_ind := do_inds[curr_ind]) < dont_ind:
            curr_ind += 1
            if curr_ind >= len(do_inds):
                dont_as_last_cmd = True
                break
        if not dont_as_last_cmd:
            data = data.replace(data[dont_ind:do_ind], ' '*(do_ind - dont_ind))
        else:
            data = data.replace(data[dont_ind:], ' ')
    
    # print(f"post processing: {data}")
    
    matches = re.findall("mul\\(\\d*,\\d*\\)", data)
    total = 0
        
    for match in matches:
        delim = match.find(',')
        n1 = int(match[4: delim]) # mul is always length 3
        n2 = int(match[delim + 1:-1]) # all but final char
        total += n1 * n2

    return total
    
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
    