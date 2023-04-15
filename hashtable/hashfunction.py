def hash(key):
    s=0
    for i in key:
        s+=ord(i)
    return s%100  #100 is the size of the list

print(hash('march 6'))

print(ord('A'))#it will get the ASCII value of A
