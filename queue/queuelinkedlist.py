class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

    def __str__(self):
        return str(self.data)
    
class linkedlist:
    def __init__(self):
        self.head=None
        #here we are assinging tail value as it is more efficient to insert the value at the end of the linked list
        self.tail=None

    def __iter__(self):
        n=self.head
        while n is not None:
            yield n
            n=n.ref

class queue:
    def __init__(self):
        self.linkedlist=linkedlist()

    def __str__(self):
        values=[str(x) for x in self.linkedlist]
        return ' '.join(values)
    
    def enque(self,value):
        node=Node(value)
        if self.linkedlist.head is None:
            self.linkedlist.head = node
            self.linkedlist.tail = node
        else:
            self.linkedlist.tail.ref=node
            self.linkedlist.tail=node
        
    def isEmpty(self):
        if self.linkedlist.head is None:
            return True
        else:
            return False

    def deque(self):
        if self.isEmpty():
            return 'empty queue'
        else:
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.ref
            return 'deleted'
        
    def peek(self):
        if self.isEmpty():
            return 'empty queue'
        else:
            return self.linkedlist.head.data

s=queue()
s.enque(90)
s.enque(67)
s.enque(0)
print(s.peek())
print(s)