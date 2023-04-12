class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
    
class linkedlist:
    def __init__(self):
        self.head=None

    def __iter__(self):
        n=self.head
        while n is not None:
            yield n
            n=n.ref

class Stack:
    def __init__(self):
        self.linkedlist=linkedlist()

    def __str__(self):
        if self.isEmpty():
            return 'empty stack'
        else:
            values=[str(x.data) for x in self.linkedlist]
            return '\n'.join(values)

    def isEmpty(self):
        if self.linkedlist.head is None:
            return True
        else:
            return False

    def push(self,value):
        node=Node(value)
        node.ref=self.linkedlist.head
        self.linkedlist.head=node

    def pop(self):
        if self.linkedlist.head is None:
            return 'empty linked list'
        else:
            self.linkedlist.head = self.linkedlist.head.ref
            return 'deleted'
        
    def peek(self):
        if self.linkedlist.head is None:
            return 'emtpy linked list'
        else:
            return self.linkedlist.head.data
        
    def delete(self):
        if self.linkedlist.head is None:
            return 'emtpy linked list'
        else:
            self.linkedlist.head = None
            return 'deleted'

s=Stack()
print(s.isEmpty())
s.push(29)
s.push(23)
s.push(78)
s.push(23)
s.pop()
s.pop()
print(s)
print('-------')
print(s.peek())
print(s.delete())
