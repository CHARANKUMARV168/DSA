nums = [1,2,3,4,5]

preffixprod = []
pr = 1
for num in nums:
  pr = pr*num
  preffixprod.append(pr)
print(preffixprod)
  
suffixprod = []
sf = 1
for num in nums[: :-1]:
  sf = sf * num 
  suffixprod.append(sf)
suffixprod.reverse()
print(suffixprod)

# boundary cond1
if len(nums) == 2 :
  nums[0] = suffixprod[1]
  nums[1] = preffixprod[0]
  #return nums 

# assigment of first and last end of the nums list 
nums[0] = suffixprod[1]
nums[len(nums)-1] = preffixprod[len(nums)-1-1]

# as we r done with first and last we need to just focus on the elements in b/w
for i in range(1,len(nums)-1):
  nums[i] = preffixprod[i-1]*suffixprod[i+1]
  print("the values are",preffixprod[i-1],suffixprod[i+1],nums[i])
  print(nums)