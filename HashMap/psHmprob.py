# print true if the sub array sum is equal to k (target)

nums = [1,2,3,4,5]
target = 4
hash = {}
hash[0]=0 # the default which helps if the num == sum 
sum = 0
i = 1
for num in nums :
    sum = sum + num
    if (sum - target) in hash.values():
        print(True)
        break
    hash[i] = sum 
    i= i+1 