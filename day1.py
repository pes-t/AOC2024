import helper
import time
import numpy as np

desired_result = 2020
file_path = "inputs/day1/p1.txt"

def p1():
    _ = 0
    data = helper.read_into_array_split_by_delim(file_path, '   ')
    left_data = sorted([int(x[0]) for x in data])
    right_data = sorted([int(x[1]) for x in data])
    total_diff = 0
    
    # print(data)
    # print(left_data)
    # print(right_data)
    
    for ind, _ in enumerate(left_data):
        total_diff += abs(left_data[ind] - right_data[ind])
    

    return total_diff

def p2():
    data = helper.read_into_array_split_by_delim(file_path, '   ')
    left_data = sorted([int(x[0]) for x in data])
    right_data = sorted([int(x[1]) for x in data])
    right_count_list = dict([x, right_data.count(x)] for x in set(right_data))
    total_score = 0
    
    for _, elem in enumerate(left_data):
        total_score += elem * right_count_list.get(elem, 0)    
    
    # print(left_count_list)
    # print(right_count_list)
    
    return total_score
    
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
    