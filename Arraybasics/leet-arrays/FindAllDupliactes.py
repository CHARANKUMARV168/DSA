'''
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

'''
# this is using hash map 
nums = [4,3,2,7,8,2,3,1]
count = 1
h = {}
arr =[]
h[0] = 0
for num in nums :
    if num in h.keys():
        count = count +1
        h[num] = count
        if count >= 2 :
            arr.append(num)
    h[num] = 1
print(arr)

# hashset : more optmised approach 
hashset = set()
arr = []
for num in nums:
    if num in hashset():
        arr.append(num)
    hashset.add(num)
print(arr)