class Node:
    def __init__(self,value):
        self.value=value
        self.ref=None

    def __str__(self):
        return str(self.value)
    
class linkedlist:
    def __init__(self):
        self.head=None
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
        values=[str(x.value) for x in self.linkedlist]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.linkedlist.head is None:
            return True
        else:
            return False
    
    def enqueue(self,value):
        node=Node(value)
        if self.isEmpty():
            self.linkedlist.head=node
            self.linkedlist.tail=node
        else:
            self.linkedlist.tail.ref=node
            self.linkedlist.tail=node

    def dequeue(self):
        if self.isEmpty():
            return 'empty stack'
        else:
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head=self.linkedlist.head.ref

    def peek(self):
        if self.isEmpty():
            return 'empty stack'
        else:
            return self.linkedlist.head.value
        

q=queue()
q.enqueue(89)
q.enqueue(90)
q.enqueue(78)
q.enqueue(0)
q.enqueue(67)
q.dequeue()
print(q)
print(q.peek())
