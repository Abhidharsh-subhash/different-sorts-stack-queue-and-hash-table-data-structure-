def insertion(array):
    for i in range(1,len(array)):
        x=array[i]
        j=i-1
        while j>=0 and x < array[j]:
            array[j+1]=array[j]
            j-=1
        array[j+1]=x
    return array

a=[34,2,6,45,3,88,34,3,6]
print(insertion(a))
