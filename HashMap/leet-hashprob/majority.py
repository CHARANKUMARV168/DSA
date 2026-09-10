class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        thresh = math.floor(len(nums)/2)
        hash = {}
        if len(nums) == 1:
            return nums[0]
        for num in nums:
            if num in hash :
                hash[num] = hash[num]+1
                if hash[num] > thresh:
                    return num
            else :
                hash[num] = 1