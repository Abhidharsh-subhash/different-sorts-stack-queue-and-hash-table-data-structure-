def bubble(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] < array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array

arr=[1,6,2,4,0,5,8,3]
print(bubble(arr))