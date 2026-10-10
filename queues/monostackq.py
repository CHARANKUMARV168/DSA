from collections import deque
nums = [1,2,3,4,3]
stack = deque()
lim = len(nums)
# only change the the res value when the loop enters the og array 
res = [-1]*lim
print("og array  :",nums)
# img will update the stack with the largest element in the array 
print("ur_img_ar :",nums,nums)
for i in range(2*lim-1,-1,-1) :
  while len(stack) != 0 and stack[-1] <= nums[i%lim]:
    print("before poping :",stack)
    stack.pop()
    print("after poping :",stack)
  if i < lim and len(stack) != 0 :
       print("res before adding val",res)
       res[i] = stack[-1]
       print("res after adding val",res)
  stack.append(nums[i%lim])
  print("values added to stack",stack)
print()
print(res)
  