# the straight frwd non optimised slow approach twds solving a problem 
# this method will try and follow each and every single method to solve a prob

#method 1 : prints all values incl duplicates i and j are same 
a=[1,2,3,4,5]
for i in range(len(a)) :
    for j in range(len(a)):
        print(f'{a[i],a[j]}',end='')
    print()

print()

# method 2 : w/o duplication : i<j
for i in range(len(a)):
    for j in range(i+1,len(a)):
        print(f'{a[i],a[j]}',end='')
    print()

# Q1 . write all pairs of a sum where i < j 
b = [10 ,20 ,30 ,40 ,50]
for i in range(len(b)):
    for j in range(i+1,len(b)):
        print(b[i],"+",b[j],"=",b[i]+b[j])
    print()

# 02 trget sum = 60 
b = [10 ,20 ,30 ,40 ,50]
for i in range(len(b)):
    for j in range(i+1,len(b)):
        if b[i]+b[j] == 60 :
            print(b[i],"+",b[j],"=",b[i]+b[j])
    print()

# triplet sum 
b = [10 ,20 ,30 ,40 ,50,60,70,80,90]
for i in range(len(b)):
    for j in range(i+1,len(b)):
        for k in range(j+1,len(b)):
            if b[i]+b[j]+b[k] == 80 :
                print(b[i],"+",b[j],"+",b[k],"=",b[i]+b[j]+b[k])

# a[j]-a[i] == diff and i < j 
b = [10 ,20 ,30 ,40 ,50,60,70,80,90]
for i in range(len(b)):
    for j in range(i+1,len(b)):
            if b[j]-b[i] == 60 :
                print(b[j],"-",b[i],"=",b[j]-b[i])