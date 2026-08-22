'''
                                   row   |  space | stars 
pattern 1 : - - - - *.              1.        4.      1
            - - - * * *.            2.        3.      3
            - - * * * * *.          3.        2       5
            - * * * * * * *.        4.        1.      7
            * * * * * * * * *.      5.        0.      9

intrusion : 
01 space : desc : {n-i} = {5-1}
''' 
n = 5
for i in range(1 , n +1 , 1):
    for j in range ( 1 ,  (n - i)+1 , 1):
        print("-",end='')
    for j in range (1, (i+(i-1))+1,1):
        print("*",end='')
    print()

'''
pattern 2 : * * * * * * * * *
            - * * * * * * *
            - - * * * * *
            - - - * * *
            - - - - *
'''
n = 5
for i in range(1 , n +1 , 1):
    for j in range( 1 ,i-1+1,1):
        print("-",end='')
    for j in range( 1 ,((n-i)+(n-i+1))+1 ,1):
        print("*",end='')
    print()

'''
pattern 3 : *
            * *
            * * *
            * * * *
            * * * * *
            * * * * 
            * * *
            * *
            * 

>> this pattern has increasing no of stars downwards till half of its length 
>> obs :
01 .total no of rows[n]   = 9
02 .increasng till row[i] = 5 : {9//2+1} : m = {n//2+1}
    >> no of stars = i 
03 .desc after m = 5
    >> no of stars = {n-i}+1
'''
n = 9 
m = n//2 +1 
for i in range( 1, n +1,1):
    for j in range (1, i+1 ,1):
        if i <= m :
            print("*",end='')
        else :
            if j < (n-i+1)+1 :
                print("*",end='')
    print()
'''
2nd approach 3rd pattern :
alternate split the pattern into halves : 
n = 5
for i in range( 1 , n+1 , 1): 
    for j in range( 1 , i+1 , 1):
            print("*",end='')
    print()

m = 4
for i in range (1 , m+1 , 1):
    for j in range(1 ,(m-i+1)+1, 1):
        print("*",end='')
    print()
'''

'''
diamond : external 
----*
---***
--*****
-*******
*********
-*******
--*****
---***
----*
'''
# approach 1 :
n = 5 
for i in range(1 , n+1 , 1):
    for j in range (1,(n-i)+1, 1):
        print("-",end='')
    for k in range (1 , (i+(i-1)+1),1):
        print("*",end='')
    print()
m = 4 
for i in range (1, m+1 ,1):
    for j in range (1, i+1, 1):
        print("-",end='')
    for k in range(1, ((m-i)+(m-i)+1)+1,1):
        print("*",end='')
    print()

# approach 2 :
n = 9
m = n // 2 + 1
print(m)
for i in range(1, n + 1):
    for j in range(1, m, 1):
        if i <= m:
            if j <= m - i:
                print("-", end='')
        else:
            if j <= i - m:
                print("-", end='')

    for k in range(1, n + 1, 1):

        if i <= m:
            if k < i + (i - 1) + 1:
                print("*", end='')
        else:
            if k < ((n-i)+(n-i)+2):
                print("*", end='')

    print()

'''
diamond : internal :

>> as there are two rows havng same no of stars it breaks the pattern and we shd go for sq cut pattern : 
* * * * *  * * * *
* * * * -  * * * *
* * * - -  - * * *
* * - - -  - - * *
* - - - -  - - - *

* * - - -  - - * * 
* * * - -  - * * *
* * * * -  * * * *
* * * * *  * * * *
'''