# given list of stock prices of the index valued days 
nums= [7,1,5,3,6,4]

nums1 = [0]

# we find the min no from l -> r
# so that we know which was the best day to buy the stock i.e, the day which the stck price was really low through the list 
# the first day is the intial val as we dont know the prices before that 
m = [nums[0]]

for i in range(1,len(nums)):   
    # compare the current day price with the prev min val known 
    # m[i-1] will contain the least min val which has occured before the current val
    # the x will contain the lowest value among currnt val and last known least val 
    x = min(nums[i],m[i-1])

    # to cal to profit we sub the current val with the prev knwon least val 
    # store the difference(profits) of each current and previously knwon value
    nums1.append(nums[i]-m[i-1])


    # this will keep track of least values knwon till the curr val 
    m.append(x)
print(nums)
print(m)
print(nums1)


"""
fully optimised code which gives the same val 

maxprofit = 0 
minprice = nums[i]
for curp in prices :
    minprice = min(minprice , curp)
    maxprofit = max(maxprofit , curp-minprice)
return maxprofit 

"""