# implementing stack using list 
class stack :

    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0 
    
    def push(self,val):
        self.items.append(val)
    
    def pop(self):
        if len(self.items) == 0 :
            return "stack empty"
        x = self.items.pop()
        return x
    
    def top(self):
        if len(self.items) == 0 :
            return "no elements on top"
        return self.items[-1]
    
    def size(self):
        return len(self.items)

s1 = stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.pop()
print(f"the stack s1",s1.items)
print(s1.top())