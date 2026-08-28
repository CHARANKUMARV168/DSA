# problem : diagonal difference of the 3*3 cross matrix 
# remember the array indexing starts from 0 and in iteration dont strt from 1 
a = [ 
     [1,2,3,4],
     [4,5,6,7],
     [9,8,9,10],
     [11,12,23,1]

]
norm = 0 
cross = 0

for i in range(0 , len(a),1):
    for j in range( 0,len(a[i]),1):
        if i ==j :
            norm = norm +a[i][j]
            
        if i+j==len(a)-1 :
            cross = cross +a[i][j]
            
    
print(norm)
print(cross)
print(abs(norm-cross))


'''
method 2 :
n_sum = 0 
c_sum = 0
n = len(a)
for i in range(len(a)):
    n_sum = n_sum + a[i][i]
    c_sum = c_sum + a[i][n-i-1]
    print()
print(n_sum)
print(c_sum)
'''
