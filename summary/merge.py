def merge(array):
    if len(array)<=1:
        return array
    mid=len(array) // 2
    left=array[:mid]
    right=array[mid:]

    left=merge(left)
    right=merge(right)

    return mergetwo(left,right)

def mergetwo(arr1,arr2):
    result=[]
    i=0
    j=0
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

arr=[1,9,4,7,2,3,0]
print(merge(arr))
