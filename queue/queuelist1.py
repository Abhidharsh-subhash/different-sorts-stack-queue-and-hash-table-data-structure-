class Queue:
    def __init__(self):
        self.list=[]

    def __str__(self):
        values=[str(x) for x in self.list]
        return ' '.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def enque(self,value):
        self.list.append(value)
        return 'inserted'
    
    def deque(self):    
        if self.isEmpty():
            return 'queue is empty'
        else:
            self.list.pop(0)
            return 'deleted'

    def peek(self):
        if self.isEmpty():
            return 'queue is empty'
        else:
            return self.list[0]
        
    def delete(self):
        if self.isEmpty():
            return 'queue is emtpy'
        else:
            self.list.clear()
            return 'queue deleted'
    
q=Queue()
# print(q.isEmpty())
q.enque(10)
q.enque(90)
q.enque(34)
# q.deque()
# q.deque()
# print(q.peek())
print(q.delete())
print(q)
