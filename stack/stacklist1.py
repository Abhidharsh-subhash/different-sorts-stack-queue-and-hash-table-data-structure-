class Stack:
    def __init__(self):
        self.list=[]

    def __str__(self):
        if self.list == []:
            return 'emtpy stack'
        else:
            values=self.list.reverse()
            values=[str(x) for x in self.list]
            return '\n'.join(values)
    
    def push(self,value):
        self.list.append(value)
        return 'value inserted'
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def pop(self):
        if self.list == []:
            return 'empty stack'
        else:
            return self.list.pop()
        
    def peek(self):
        if self.list == []:
            return 'stack empty'
        else:
            return self.list[-1]
        
    def delete(self):
        if self.list == []:
            return 'stack is empty'
        else:
            self.list.clear()
            return 'stack deleted'

        
s=Stack()
s.push(10)
s.push(90)
s.push(56)
s.push(99)
s.push(76)
print('deletiion')
print(s.pop())
print(s.pop())
print('last element')
print(s.peek())
print('after deletion')
print(s.delete())
print(s)
