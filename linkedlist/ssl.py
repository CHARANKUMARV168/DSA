class node:
    def __init__(self,val= 0):
        self.val = val
        self.next = None
    
class sll :
    
    # ll creation :
    def __init__(self):
        self.head = None
    

    def append(self,val):

        # create the new node
        new_node = node(val)
        
        # if there is no node in the list .i.e, list is empty 
        if self.head == None :
            # make the new node as head
            self.head = new_node
        
        else :
            # create a node for iteration to end of list as we need to add the node at last of the list : append func 
            curr_node = self.head 
            while curr_node.next != None :
                curr_node = curr_node.next
            
            # af iteration we reach the end of the list and we connect the new element to the last node 
            curr_node.next = new_node 
    
    # accesing each and every node of the sll 
    def traverse( self ):
        if self.head is None :
            print("empty list") 
        curr = self.head 
        while curr is not None :
            print(curr.val)
            curr = curr.next 
    
 
s1 = sll()
s1.append(10)
s1.append(20)
s1.append(30)
s1.append(40)
s1.traverse()