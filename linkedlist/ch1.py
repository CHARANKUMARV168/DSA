class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Create nodes
head = ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)
node4 = ListNode(40)

# Connect nodes
head.next = node2
node2.next = node3
node3.next = node4

print(head)