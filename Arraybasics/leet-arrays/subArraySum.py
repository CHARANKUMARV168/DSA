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

        
# optimization using hash map and preffix sum array 
def subarraysumhashprefix(nums , k):
    sum = 0 
    hashmap = {}
    hashmap[0] = 0
    i = 0 
    for num in nums :
        sum = sum + num
        if  (sum - k) in hashmap.values():
            count = count +1 
        
        hashmap[i] = sum 
        i= i+1 
    return count



nums = [1,1,1]
k = 2
x = subarraySum(nums,k)
print(x)