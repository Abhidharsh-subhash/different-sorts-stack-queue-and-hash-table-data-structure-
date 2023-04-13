def merge(array,start,middle,end):
    n1=middle-start+1
    n2=end-middle

    L=[0] * n1
    R=[0] * n2

    for i in range(n1):
        L[i] = array[start+i]

    for j in range(n2):
        R[j] = array[middle+1+j]

    i=0 #initial index of first sub list
    j=0 #initial index of second sub list
    k=start #initial index of merged sub list