class stack:
    def __init__(self):
        self.q1=[]
        self.q2=[]

    def push(self,value):
        if not self.q1:
            self.q1.append(value)
        else:
            self.q2.append(value)

        while self.q1:
            self.q2.append(self.q1.pop(0))

        self.q1,self.q2=self.q2,self.q1

    def isEmpty(self):
        if not self.q1:
            return True
        else:
            return False
    
    def pop(self):
        if not self.q1:
            return 'empty stack'
        else:
            return self.q1.pop(0)
        
    def top(self):
        if not self.q1:
            return 'empty stack'
        else:
            return self.q1[0]
        
    def display(self):
        if not self.q1:
            print('empty stack')
        else:
            for x in self.q1:
                print (x)


s=stack()
s.push(10)
s.push(90)
s.push(70)
s.push(6)
s.display()
print('____')
s.pop()
s.display()
print(s.top())




# First, it checks whether the first queue (q1) is empty. If q1 is empty, it means there are no items in the stack yet, 
# so the new item is added to q1 directly using the append method.If q1 is not empty, it means that there are items in the stack already. 
# In this case, the new item is added to the back of the second queue (q2) using the append method.The function then moves all items from q1 to q2. 
# This is done by using a while loop that pops items from q1 using the pop method with an index of 0, which removes the first item from the list. 
# Each item is then appended to the back of q2 using the append method.After all items have been moved from q1 to q2, 
# the two queues are swapped using Python's tuple assignment. This effectively makes q2 the new empty queue and q1 the new queue containing all items
# in the stack.