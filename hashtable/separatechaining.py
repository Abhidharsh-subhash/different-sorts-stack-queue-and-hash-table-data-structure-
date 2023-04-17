class hashtable:
    def __init__(self):
        self.max=10
        self.arr=[[] for i in range(self.max)]
    
    def get_hash(self,key):
        s=0
        for i in key:
            s+=ord(i)
        return s%10
    
    def __setitem__(self,key,value):
        s=self.get_hash(key)
        found=False
        #here we are using tuple so it is immutable
        for index,element in enumerate(self.arr[s]):
            if element[0] == key and len(element) ==2:
                self.arr[s][index] = (key,value)
                found=True
                break
        if not found:
            self.arr[s].append((key,value))

    def __getitem__(self,key):
        s=self.get_hash(key)
        for element in self.arr[s]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self,key):
        s=self.get_hash(key)
        for index,element in enumerate(self.arr[s]):
            if element[0] == key:
                del self.arr[s][index]


h=hashtable()
h['march 6']=290
h['march 6']=78
h['march 8']=67
h['march 9']=4
h['march 17']=459
del h['march 17']
print(h.arr)


