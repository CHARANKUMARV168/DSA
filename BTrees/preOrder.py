# node first and next left and nxt right 

class Node :
    def __init__(self,value):
        self.value = value 
        self.left = None 
        self.right = None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)

n1.left = n2
n1.right = n3

n2.left = n4
n2.right = n5

n3.left = n6
n3.right = n7

n4.left = n8
n4.right = n9
    
res = []
def preorder(Node):
    if Node == None :
        return
    res.append(Node.value)
    preorder(Node.right)
    preorder(Node.left)

preorder(n1)
print(res)