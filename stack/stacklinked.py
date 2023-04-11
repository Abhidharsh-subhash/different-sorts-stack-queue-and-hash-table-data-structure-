class Node:
    def __init__(self,data=None):
        self.data=data
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
    # This method creates a stack linked list
    def __init__(self):
        self.linkedlist=linkedlist()

    def __str__(self):
        values=[str(x.data) for x in self.linkedlist]
        return '\n'.join(values)

    def isEmpty(self):
        if self.linkedlist.head is None:
            return True
        else:
            return False
        
    def push(self,value):
        node=Node(value)
        node.next=self.linkedlist.head
        self.linkedlist.head=node

    def pop(self):
        if self.linkedlist.head is None:
            return 'empty stack'
        else:
            self.linkedlist.head=self.linkedlist.head.next
            return 'deleted last inserted element'

    def delete(self):
        if self.linkedlist.head is None:
            return 'empty stack'
        else:
            self.linkedlist.head = None
            return 'deleted successfully'

    def peek(self):
        if self.linkedlist.head is None:
            return 'empty stack'
        else:
            return self.linkedlist.head.data

        
s=stack()
s.push(11)
s.push(8)
s.push(0)
s.push(5)
# print(s.isEmpty())
s.pop()
s.pop()
print(s)
print('top')
print(s.peek())
print(s.delete())