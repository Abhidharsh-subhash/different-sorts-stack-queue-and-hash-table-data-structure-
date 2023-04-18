class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        n=self.head
        while n is not None:
            yield n
            n=n.ref

class stack:
    def __init__(self):
        self.linkedlist=linkedlist()

    def isEmpty(self):
        if self.linkedlist.head is None:
            return True
        else:
            return False
        
    def __str__(self):
        if self.isEmpty():
            return 'empty stack'
        else:
            values=[str(x.data) for x in self.linkedlist]
            return '\n'.join(values)
    
    def push(self,value):
        node=Node(value)
        if self.isEmpty():
            self.linkedlist.head = node
            self.linkedlist.tail = node
        else:
            self.linkedlist.tail.ref = node
            self.linkedlist.tail = node

    def pop(self):
        if self.linkedlist.tail == self.linkedlist.head:
            self.linkedlist.tail = None
            self.linkedlist.head = None
        else:



s=stack()
s.push(90)
s.push(78)
s.push(0)
s.push(56)
print(s) 


#it is not possible to insert the value at the end of the linkeed list to implement stack as it takes more complexity to add at the end 
# of the linkedl list because it takes a traversal to add at the end of the linkeslist but it is possible to reduce the complexity by 
# adding at the beginning of the linked list

