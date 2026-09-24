nums = [1,2,3,4,5]
#req = [120 , 60 , 40, 30 , 24]
pref = [] # product cal from left to right 
p = 1
for num in nums :
  p = num * p 
  pref.append(p) 
print(pref)

suff = [] # product cal from right from left 
s = 1
for num in nums[::-1] :
  s = s * num 
  suff.append(s)
suff.reverse()
print(suff)

# boundary cases :
if len(nums) == 2 :
  nums[0] = suff[1]
  nums[1] = pref[0]

nums[0] = suff[1]
nums[len(nums)-1] = pref[len(pref)-2]

for i in range(1,len(nums)-1):
  nums[i] = pref[i-1]*suff[i+1]
print(nums)