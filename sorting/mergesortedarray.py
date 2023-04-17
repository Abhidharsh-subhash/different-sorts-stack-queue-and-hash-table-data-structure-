def merge(arr1,arr2):
    i=0
    j=0
    l1=len(arr1)
    l2=len(arr2)
    result=[]
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
        result.append(arr2[i])
        j+=1

    return result




array1=[1,4,9,10]
array2=[2,3,6,7,8]
print(merge(array1,array2))