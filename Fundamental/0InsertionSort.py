

def InsertionSort(arr: list) -> list:

    for i in range(len(arr)):
        v = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > v:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = v

    return arr



sorted = InsertionSort([223,12,3,23,1,23,4,23,5,43,5,34,6])

print(sorted)