# the program which displays the dupliactes using hash set :
# the key part of the hashset actually uses the set for implementation which allows no dupliactes so using the set allows only usage of unique values making find the dupliactes in a easy manner 
nums = [1,2,3,4,2,5,3,1,5]
seen = set()
for num in nums :
    if num in seen :
        print(num)
    seen.add(num)