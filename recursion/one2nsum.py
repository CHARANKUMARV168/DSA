from collections import deque
stack = deque()

def count(sum,i,N):
  stack.append(f"count({i},{N},{sum})")
  if i > N :
    print("sum",sum)
    print(f"base cond reached {i}","on func call",stack[-1])
    return 
  sum=sum+i
  print(f"{i}sum",sum)
  count(sum,i+1,N)

  

count(sum=0,i=1,N=5)

print(stack)