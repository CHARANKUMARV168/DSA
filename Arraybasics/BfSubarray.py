'''
brute force sub array : 
sub array : a small continuos part of the main array 
'''
# prints all the sub arrays 
a = [10,20,30,40,50,60,70]
for i in range(len(a)):
    for j in range(i,len(a),1):
        for k in range(j,len(a),1):
            print(f'{a[k]}'+" ",end='')
        print()
        
a=[1,2,3,4,5]
for i in range(len(a)) :
    for j in range(i,len(a)):
        for k in range(i,j+1,1):
            print(f'{a[k]}'+" ",end='')
        print()

a=[1,2,3,4,5]
for i in range(len(a)) :
    for j in range(i,len(a)):
        for k in range(i,j+1,1):
            print(f'{a[k]}'+" ",end='')
        print()

a=[10,20,30,40,50]
for i in range(len(a)) :
    for j in range(i,len(a)):
        print(f'{i}',f'{j}')
        for k in range(i,j+1,1):
            print(a[k])
        print()
    print()
# i gives the left bound 
# j gives the right bound

'''
to generate all the combination of sub arrays :
lock i from 0 to n-1 :
    lock j from i to n-1 :
        print(i,j) # this is where we generate all combinations 
        use k b/w i and j :
           ⚠️always use j+1 as we use python range function
           print(arr[k])
        print()
    print()
'''