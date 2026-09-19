'''
kadane : the more effecient way of finding the max sub array which i.e, finds which sub array has the maximum sum for the given array .
* used to find the max sum of a continuos sub array in 0(n) time and 0(1) space complexity 
* it has two important elements :
01 current_sum : this variable decides whether we shd extend the sub array ( current_sum + num ) or just consider the num {select the max by comparing both the values}
02 max_sum : on each iteration the current sum is compared to the max_sum and then store the max value among both of them into the max_sum 
>> the first element of the array is considered as the max_sum coz :
* sub array cannot be empty 
* we consider the first value to be the best value 
'''
# this gives the max sub array 
nums = [1,23,34,-43,65,63]
curr = 0
most = a[0]
for num in nums :
    curr = max(num , curr+num)
    most = max(curr , most)
return most

# min sub array 
curr = 0
least = a[0]
for num in nums :
    curr = min(num , curr+num)
    least = min(curr , least)
return least