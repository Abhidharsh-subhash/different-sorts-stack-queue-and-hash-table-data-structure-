def mergesort(array):
    if len(array) <= 1:
        return array
    
    mid=len(array) // 2
    left=array[:mid]
    right=array[mid:]

    left=mergesort(left)
    right=mergesort(right)

    return mergetwo(left,right)

def mergetwo(arr1,arr2):
    j=0
    i=0
    result=[]
    l1=len(arr1)
    l2=len(arr2)
    while (i<l1 and j<l2):
        if arr1[i]<arr2[j]:
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1
    while i<l1:
        result.append(arr1[i])
        i+=1
    while j<l2:
        result.append(arr2[j])
        j+=1
    return result

arra=[1,4,2,7,5,3,7,8]

print(mergesort(arra))
