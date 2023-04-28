
def sequential_search(arr: list, key):

    i = 0
    n = len(arr)

    while i < n and arr[i] != key:
        i += 1
    
    if i < n:
        return i 
    else:
        return None
    

idx = sequential_search([1, 2, 3, 5, 9], 9)

print(idx)