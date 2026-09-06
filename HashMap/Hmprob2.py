# print the longest sub array where the start and ending value of the sub array are the same
# hashmap <no , first occurence of index of the number >
# needs more clear explanation 
nums = [10, -1, -2,10,11, -1,7,8, 11,8, 6, 10]
hash ={}
mark1 = 0 
mark2 = 0
maxlen = 0
i = 0
for num in nums :
    if num in h.keys() and i-h[num] > maxlen :
        maxlen = i-h[num]
        mark1 = h[num]
        mark2 = i

    else:
        h[num] = i
    i =i+1

for j in range( mark1 , mark2+1):
    print(nums[j])

print()
print("max len is :",maxlen+1)