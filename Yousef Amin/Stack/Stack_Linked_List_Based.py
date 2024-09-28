class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
    
    def push(self,value):
        temp = Node(value)
        
        if not self.head:
            self.head = temp
        
        else:
            self.head.next = temp
    
    def pop(self):
        if not self.head:
            raise ValueError('The Stack is already Empty')
        
        if not self.head.next:
            temp = self.head
            self.head = None
            return temp
        temp = self.head.next
        self.head.next = None
        self.head = temp
        
        return self.head.data
    
    def Is_empty(self):
        if not self.head:
            return True
        return False
    
    def top(self):
        return self.head if self.head else 'Empty'

arr = Stack()
arr.push(14)
arr.push(17)
arr.pop()
arr.pop()
print(arr.top())