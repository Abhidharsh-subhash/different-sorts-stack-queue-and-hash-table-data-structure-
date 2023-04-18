def merge(arr1,arr2):
    result=[]
    l1=len(arr1)
    l2=len(arr2)
    i=0
    j=l2-1
    while i<l1 and j>=0:
        if arr1[i]< arr2[j]:
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j-=1
    while i<l1:
        result.append(arr1[i])
        i+=1
    while j>=0:
        result.append(arr2[j])
        j-=1
    return result


array1=[5,15,25]
array2=[30,20,10]
print(merge(array1,array2))