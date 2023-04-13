class Queue:
    def __init__(self,limit):
        self.limit=limit
        self.queue=limit * [None]
        self.start=-1
        self.end=-1

    def __str__(self):
        values=[str(x) for x in self.queue]
        return ' '.join(values)
    
    def isFull(self):
        if self.end+1 == self.start:
            return True
        elif self.start == 0 and self.end == len(self.queue)-1:
            return True
        else:
            return False

    def isEmpty(self):
        if self.end == -1 and self.start == -1:
            return True
        else:
            return False
        
    def enque(self,value):
        if self.isFull():
            return 'queue is full'
        else:
            if self.end+1 == self.limit:
                self.end=0
            else:
                self.end +=1
                if self.start == -1:
                    self.start=0
                self.queue[self.end]=value
                return 'element inserted'
            
    def deque(self):
        if self.isEmpty():
            return 'empty queue'
        else:
            element=self.queue[self.start]
            start=self.start
            if self.start == self.end:
                self.start=-1
                self.end=-1
            elif self.start +1 == self.limit:
                self.start=0
            else:
                self.start+=1
            self.queue[start]=None
            return element
        
    def peek(self):
        if self.isEmpty():
            return 'empty stack'
        else:
            return self.queue[self.start]
        
    def delete(self):
        if self.isEmpty():
            return 'empty stack'
        else:
            self.queue = self.limit * []
            self.start =-1
            self.end = -1
            return 'queue deleted successfully'

n=int(input('enter the queue size'))
q=Queue(n)
print(q.enque(0))
print(q.enque(89))
print(q.enque(78))
print(q.enque(45))
print(q.enque(56))
print(q.deque())
print(q.deque())
print(q)
print('------')
print(q.peek())
print(q.delete())
