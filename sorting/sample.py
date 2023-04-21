def partition(arr):
    pivot_index = 0
    pivot = arr[pivot_index]

    start = pivot_index + 1
    end = len(arr) - 1

    while start <= end:
        while arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    return end

def quicksort(array):
    if len(array) <= 1:
        return array

    pivot_index = partition(array)
    left_partition = quicksort(array[:pivot_index])
    right_partition = quicksort(array[pivot_index + 1:])
    
    return left_partition + [array[pivot_index]] + right_partition

arr1 = [11, 9, 29, 7, 2, 15, 28]
print(quicksort(arr1)) # Output: [2, 7, 9, 11, 15, 28, 29]

