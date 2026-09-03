'''  
        0 1 3
a = 0 [[1,2,3],
    1 [5,6,7],
    2 [8,9,10]]

'''

# accesing : element by element
a = [[1,2,3],
    [5,6,7],
    [8,9,10]]
for i in a :
    print(i)
    for j in i :
        print(j)

# accesing : through index value 
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
    print()
