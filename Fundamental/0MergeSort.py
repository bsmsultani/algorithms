
"""
Merge sort is a divide and conquer algorithm that works by dividing a problem into sub-problems and then solving the problem.

It consists of two methods:

- Merge : which 
"""

def Merge(arr: list, middle : int):
    
    p = 0
    q = middle + 1
    r = 0
    j = len(arr) - 1

    while p <= middle and q <= j:
        pass