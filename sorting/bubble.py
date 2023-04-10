def bubble(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array

arr=[10,57,24,99,89,56,23]
print(bubble(arr))