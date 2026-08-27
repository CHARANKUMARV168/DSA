# the prefix sum array : A array data structure in which each current element is # the sum of its previous elements 

a = [10,20,30,40,50,60,70]

# let psum be a prefix sum array of an array a initialised with 0
psum = [ 0 for i in range(len(a)) ]
print(psum)

sum = 0 
for i in range(len(a)):
    sum = sum + a[i]
    psum[i] = sum

print(psum)
a=psum
print(a)

'''
hackerrank : 
01 simple array sum 
02 a very big sum 

leetcode :
1480. Running Sum of 1d Array
'''