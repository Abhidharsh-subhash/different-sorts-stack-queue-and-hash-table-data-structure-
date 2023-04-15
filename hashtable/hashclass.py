class hashtable:
    def __init__(self):
        self.max=100
        self.arr=[None for i in range(self.max)]
    
    def get_hash(self,key):
        s=0
        for i in key:
            s+=ord(i)
        return s%self.max
    
    def add(self,key,value):
        h=self.get_hash(key)
        self.arr[h]=value

    def get(self,key):
        h=self.get_hash(key)
        return self.arr[h]
    
h=hashtable()
# print(h.get_hash('march 6'))
h.add('march 6',312)
h.add('march 7',320)
h.add('march 8',410)
print(h.arr)
print(h.get('march 7'))