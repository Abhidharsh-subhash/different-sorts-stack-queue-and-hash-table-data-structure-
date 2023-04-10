def selection(array):
    for i in range(len(array)):
        min=i
        for j in range(i+1,len(array)):
            if array[min] > array[j]:
                min=j
        array[i],array[min]=array[min],array[i]
    return array

arr=[11,54,2,65,78,34,99,0]
print(selection(arr))