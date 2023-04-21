def partition(mylist,pivot,end):
    start=pivot
    for i in range(pivot+1,end+1):
        if mylist[i] < mylist[pivot]:
            start+=1
            mylist[i],mylist[start]=mylist[start],mylist[i]
    mylist[pivot],mylist[start]=mylist[start],mylist[pivot]
    return start

def quicksort_helper(mylist,left,right):
    if left < right:
        pivot=partition(mylist,left,right)
        quicksort_helper(mylist,left,pivot-1)
        quicksort_helper(mylist,pivot+1,right)
    return mylist

def quicksort(array):
    return quicksort_helper(array,0,len(array)-1)


arr=[3,6,9,2,0]
print(quicksort(arr))

