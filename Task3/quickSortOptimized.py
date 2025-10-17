def quicksort_optimized(arr):
    if len(arr) <= 1:
        return arr

    if len(arr) <= 10:
        return insertion_sort(arr)

    first, middle, last = arr[0], arr[len(arr) // 2], arr[-1]
    pivot = sorted([first, middle, last])[1]

    left = [x for x in arr if x < pivot]
    middle_arr = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort_optimized(left) + middle_arr + quicksort_optimized(right)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
