class hashtable:
    def __init__(self):
        self.max=100
        self.arr=[None for i in range(self.max)]

    def get_hash(self,key):
        s=0
        for i in key:
            s+=ord(i)
        return s%100
    
    #default names given in the documentation
    def __setitem__(self,key,value):
        s=self.get_hash(key)
        self.arr[s]=value

    def __getitem__(self,key):
        s=self.get_hash(key)
        return self.arr[s]
    
    def __delitem__(self,key):
        s=self.get_hash(key)
        self.arr[s]=None
    
h=hashtable()
h['march 6']=220
h['march 9']=200
h['march 3']=320
del h['march 9']
print(h.arr)
print(h['march 6'])