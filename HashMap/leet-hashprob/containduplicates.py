# if there is a duplicate return true else false 
nums = [10,20,30,40,50]
seen = set()
for num in nums :
    if num in seen :
        return True 
        break
    else:
        seen.add(num)
return False

# {OR}

if len(nums) == len(set(nums)):
    return True 
return False 