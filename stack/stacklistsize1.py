class stack:
    def __init__(self,size):
        self.size=size
        self.list=[]

    def __str__(self):
        if self.isEmpty():
            return 'stack is empty'
        else:
            values=self.list.reverse()
            values=[str(x) for x in self.list]
            return '\n'.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False 
        
    def isFull(self):
        if self.size == len(self.list):
            return True
        else:
            return False

    def push(self,value):
        if self.isFull():
            return 'stack is full'
        else:
            self.list.append(value)
            return 'value inserted'
        
    def pop(self):
        if self.list == []:
            return 'empty stack'
        else:
            return self.list.pop()
        
    def peek(self):
        if self.list == []:
            return 'empty stack'
        else:
            return self.list[0]
        
    def delete(self):
        if self.list == []:
            return 'empty stack'
        else:
            self.list.clear()
            return 'stack deleted'
            
n=int(input('enter the size of the stack'))
s=stack(n)
s.push(10)
s.push(33)
s.push(34)
s.push(78)
s.push(88)
s.push(111)
print(s)
print('topmost')
print(s.peek())
print(s.delete())
print(s)


