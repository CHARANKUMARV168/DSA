'''
* using Using collections.deque
* deque class from the collections module provides fast insertion and deletion operations
* It supports stack behavior using append() and pop() methods. deque is usually faster than lists for large data operations

| Stack operation | `deque` method    | What it does                       |
| --------------- | ----------------- | ---------------------------------- |
|   Push.         | `append(x)`       | Adds element to the top            |
|   Pop.          | `pop()`           | Removes and returns top element    |
|   Peek / Top    | `stack[-1]`       | Views top element without removing |
|   isEmpty       | `len(stack) == 0` | Checks whether stack is empty      |
|   Size          | `len(stack)`      | Returns number of elements         |


'''

from collections import deque

st = deque()
st.append("a")
st.append("b")
st.append("c")

print(st)
print(st.pop())
print(st.pop())