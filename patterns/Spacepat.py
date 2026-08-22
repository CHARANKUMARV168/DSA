# this has two patterns combined one empty spaces and the other star pattern 
# the reducing space pattern : {n-i}
# the increasing star pattern : {i +/-}

'''
pattern 01 : _ _ _ _ *
             _ _ _ * *
             _ _ * * *
             _ * * * *
             * * * * *

observation :

01 empty spaces : {n-i} = {5-1}
02 stars : i

'''
n = 5
for i in range (1 , n+1 ,1):
    for j in range( 1 , (n-i)+1 ,1):
        print(" ",end='')
    for j in range(1 , i+1 ,1):
        print("*",end='')
    print()

print()

'''
pattern 2 : * * * * *
            - * * * * 
            - - * * * 
            - - - * * 
            - - - - *
'''
n=5 
for i in range ( 1 , n+1 , 1):
    for j in range(1 , (i-1)+1, 1):
        print("-",end='')
    for j in range(1 , ((n-i)+1)+1 ,1):
        print("*",end='')
    print()
'''
pattern 3 :  * 
            * * 
           * * * 
          * * * * 
         * * * * * 

    
'''
n = 5 
for i in range (1 , n+1 ,1):
    for j in range( 1 , (n-i)+1 ,1):
        print(" ",end='')
    for j in range(1 , i+1 ,1):
        print("* ",end='')
    print()

'''
pattern 4 : * * * * *
             * * * *
              * * *
               * *
                *
'''
n = 5
for i in range ( 1 , n+1 , 1):
    for j in range(1 , i , 1):
        print(" ",end='')
    for j in range(1 , ((n-i)+1)+1 , 1):
        print(" *",end='')
    print()