import numpy as np
from collections import Counter
from itertools import pairwise

def read_into_nparray(filename: str, dtype: np.dtype=np.int32):
    return np.loadtxt(filename, dtype=dtype)

def read_into_array_split_by_delim(filename: str, delimeter: str):
    with open(filename, 'r') as f:
        lines = f.read().split('\n')
        return [line.split(delimeter) for line in lines]
    
def read_into_string(filename: str):
    with open(filename, 'r') as f:
        return f.read()
    
def count_occurences(data: list):
    return Counter(data)

def is_sorted(data: list):
    return all(a <= b for a,b in pairwise(data))

def is_reverse_sorted(data: list):
    return all(a >= b for a, b in pairwise(data))

def strict_is_sorted(data: list):
    return all(a < b for a,b in pairwise(data))

def strict_is_reverse_sorted(data: list):
    return all(a > b for a,b in pairwise(data))