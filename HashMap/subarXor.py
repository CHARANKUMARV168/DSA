# if the sub array xor is equal to zero then return true else false 
nums = [ 2 , 1 , 1 , 1 , 2 , 2 , 1 , 1]
xor = 0
hash = {}
break1 = 0 
for num in nums :
    xor = xor^num
    if xor in hash.keys():
        print(True)
        break1 = 1
        return 
    else :
        hash[xor] = 1
        
if break1 == 0 :
    print(False)