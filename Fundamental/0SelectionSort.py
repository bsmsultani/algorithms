
"""
Has a time complexity of O(n^2) and is Unstable.

"""

def SelectionSort(arr: list) -> list:

    for i in range(len(arr) - 2):
        min = i
        j = i + 1
        for j in range(len(arr) - 1):
            if arr[j] < arr[min]:
                min = j
            
        arr[i] = arr[min]

    return arr


sorted = SelectionSort([3, 1, 5, 8])

print(sorted)
