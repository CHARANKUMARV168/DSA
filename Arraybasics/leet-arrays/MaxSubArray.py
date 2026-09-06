
def maxSubArray(nums):
    curr_sum = 0
    max_sum = nums[0]
    for num in nums :
        curr_sum = max(curr_sum+num,num )
        max_sum = max(max_sum,curr_sum)
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))