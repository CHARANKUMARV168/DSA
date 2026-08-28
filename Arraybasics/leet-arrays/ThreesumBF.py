class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        psum =[]
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if (nums[i]+nums[j]+nums[k] == 0):
                        a = [nums[i],nums[j],nums[k]]
                        a.sort()
                        if a not in psum :
                            psum.append(a)
        return psum

nums = [-1,0,1,2,-1,-4]
Solution(nums)