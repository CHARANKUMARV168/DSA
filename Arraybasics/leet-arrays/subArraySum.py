# 560. Subarray Sum Equals K
# solved using brute force
def subarraySum( nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                sum = 0
                for z in range(i,j+1,1):
                    sum = sum+nums[z]
                if sum == k:
                    count = count+1
        return count

        

nums = [1,1,1]
k = 2
x = subarraySum(nums,k)
print(x)