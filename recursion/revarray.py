nums = [1,2,3,4,5,6,7,8]

def rev(nums,l,r):
  print()
  if l > r :
    return
  nums[l],nums[r] = nums[r],nums[l]
  rev(nums,l+1,r-1)

rev(nums,0,len(nums)-1)
print(nums)