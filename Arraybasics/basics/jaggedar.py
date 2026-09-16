# the nested array which in which each row has different no of elements :
ar = [
    [1,2,3,45,5],
    [6,7,8],
    [23,34,56,73]
]
for num in ar :
    for n in num :
        print(n,end=" ")
    print()

for i in range(len(ar)):
    for j in range(len(ar[i])):
        print(ar[i][j],end=" ")
    print()