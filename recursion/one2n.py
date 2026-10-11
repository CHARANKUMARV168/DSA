from collections import deque
stack = deque()

def count(i,N):
  stack.append(f"count({i},{N})")
  if i == N :
    print(f"base cond reached {i}","on func call",stack[-1])
    return 
  count(i+1,N)
  print(i)
 

count(1,5)
print(stack)