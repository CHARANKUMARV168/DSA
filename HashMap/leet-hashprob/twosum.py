nums = [2,7,11,15]
target = 9
h ={}
res= []
i=0
for num in nums :
    if target - num in h:
        res.append(h[target-num])
        res.append(i)
    else :
        h[num]=i
        i=i+1
print(res)


