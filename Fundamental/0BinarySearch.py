"""
If the collection of items are sorted in ascending to some recognised order, we can use decrease-and-conquer algorithm.


"""

def BinarySearch(arr: list, val):

    l = 0
    r = len(arr) - 1

    while l <= r:
        m = int((l+r)/2)
        if val == arr[m]: return m
        elif val < arr[m]: r = m - 1
        else: l = m + 1

    return None


idx = BinarySearch([1, 2, 3, 4, 9], 9)

print(idx)