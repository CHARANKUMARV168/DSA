nums = [10,20,30,40,50,60,70]

h ={}

# default value addition which say that sum is zero until the index 0 
h[0] = 0
print(h)

# for the element insertion we will use a pointer i staring from 1 , which says sum of 1 element is 
i = 1

# the sum var which is part of the psum array
sum = 0
for num in nums :
    sum = sum + num
    h[i] = sum
    i = i+1 

print(h)
