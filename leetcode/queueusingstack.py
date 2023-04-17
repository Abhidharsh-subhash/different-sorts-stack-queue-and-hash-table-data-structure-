class queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]

    def enqueue(self,value):
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
        self.s1.append(value)
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())

    def dequeue(self):
        if len(self.s1) == 0:
            return 'empty queue'
        else:
            return self.s1.pop()
        
    def display(self):
        if len(self.s1) == 0:
            return 'empty queue'
        else:
            for i in self.s1:
                print(i)

    def top(self):
        if len(self.s1) == 0:
            return 'empty queue'
        else:
            return self.s1[-1]
        
q=queue()
q.enqueue(80)
q.enqueue(70)
q.enqueue(0)
q.enqueue(67)
q.display()
print(q.top())
print('------')
q.dequeue()
q.dequeue()
print(q.top())
q.display()