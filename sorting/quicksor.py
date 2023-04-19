def partition(arr):
    pivort_index=0
    pivort=arr[pivort_index]

    start=pivort_index + 1
    end=len(arr) - 1

    while start<=end:
        while arr[start] <= pivort:
            start+=1
        while arr[end] > pivort:
            end-=1
        if start < end:
            arr[start],arr[end]=arr[end],arr[start]
    arr[pivort_index],arr[end]=arr[end],arr[pivort_index]

def quicksort(array):
    if len(array) <= 1:
        return array

    pivot_index = partition(array)
    left_partition = quicksort(array[:pivot_index])
    right_partition = quicksort(array[pivot_index + 1:])
    
    return left_partition + [array[pivot_index]] + right_partition

arr1=[11,9,29,7,2,15,28]
quicksort(arr1)
print(arr1)

