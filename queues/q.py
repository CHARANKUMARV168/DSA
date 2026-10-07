"""
| Queue operation  | `deque` method   | What it does                              |
|------------------|------------------|-------------------------------------------|
|   Enqueue.       |    `append(x)`   | Adds element to the rear/back.            |
|   Dequeue.       |    `popleft()`   | Removes and returns the { front } element |
|   Peek / Front.  |     `queue[0]`   | Views front element without removing      |
|   isEmpty        | `len(queue) == 0`| Checks whether queue is empty             |
|   Size.          |   `len(queue)`   | Returns number of elements                |
|.  insertleft.    | appendleft(val). | adds the val to left side of list.        |
|.  removeright.   | pop.             |removes the val from the left side of list.|
"""


class Queue:
    def __init__(self):
        self.items = []

    def is_empty (self):
        return len(self.items) == 0
          
    def enqueue (self, val):
        self.items.append(val)

    def dequeue (self):
        if len(self.items) == 0:
            print("the q is empty")
            return
        x = self.items.pop(0)
        return x

    def front (self):
        if len (self.items) == 0:
            return print ("Cannot peek, queue is empty") 
        return self.items[0]

    def rear(self):
        if len (self.items) == 0:
            print ("Cannot read, queue is empty")
        return self.items[-1]
        
    def size(self):
        return len(self.items)