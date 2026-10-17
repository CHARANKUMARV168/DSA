# implementing a binary tree :
class Node :
    def __init__(self,value):
        self.value = value 
        self.left = None 
        self.right = None

drinks = Node("drinks")
hot = Node("hot")
cold = Node("cold")
coffee = Node("coffee")
tea = Node("tea")
cola = Node("cola")
fanta = Node("fanta")

drinks.right = hot
drinks.left = cold
hot.left = tea
hot.right = coffee
cold.left = cola
cold.right = fanta


# when we try printing a object we get its address we dont get its val 
print(drinks)
# we shd access it attributes to get the value 
print(drinks.value)

# how to say we have connected all the nodes of a tree 
print("address of all the nodes of a tree")
print(drinks.right)
print(hot)
