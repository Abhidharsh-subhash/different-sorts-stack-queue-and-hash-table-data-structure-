def bubble(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array

arr=[4,1,7,5,2,0,7,9,2]
print(bubble(arr))
