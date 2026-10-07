class stackusingq :

    def __init__(self):
        self.list = deque()
    
    def add(self,val):
        self.list.append(val)
        for i in range(len(self.list)-1):
            self.list.apped(self.list.popleft())
    
    def pop(self):
        if len(self.list) == 0 :
            return "empty"
        
        return self.list.popleft()
    
    def top(self):
        return self.list[0]
    
    def is_empty(self):
        return len(self.list) == 0 
    
    def size(self):
        return len(self.list)
    


