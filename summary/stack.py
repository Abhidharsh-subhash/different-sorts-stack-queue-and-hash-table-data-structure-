class Node:
    def __init__(self,value):
        self.value=value
        self.next=next

class linkedlist:
    def __init__(self):
        self.head=None

    def __iter__(self):
        n=self.head
        while n is not None:
            yield n
            n=n.next

class stack:
    def __init__(self):
        self.linkelist=linkedlist()

    def __str__(self):
        if self.isEmpty():
            return 'empty stack'
        else:
            values=[str(x.value) for x in self.linkelist]
            return '\n'.join(values)  

    def isEmpty(self):
        if self.linkelist.head is None:
            return True
        else:
            return False

    def push(self,value):
        node=Node(value)
        node.next=self.linkelist.head
        self.linkelist.head=node

    def pop(self):
        if self.isEmpty():
            return 'empty stack'
        else:
            self.linkelist.head=self.linkelist.head.next

    def peek(self):
        if self.isEmpty():
            return 'empty stack'
        else:
            return self.linkelist.head.value
        


s=stack()
s.push(10)
s.push(78)
s.push(34)
s.push(90)
s.push(55)
s.pop()
print(s)
print(s.peek())