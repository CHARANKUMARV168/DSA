# ⚠️when patterns are increasing : {i} +/- smtg
# ⚠️when patterns are decreasing : {n-i} +/- smtg
# descresaing odd no pattern : {{n-i}+{n-i}+1}
# descreasing even no pattern : {n-i}+{n-i}+2


'''
pattern 1 : *
            * * 
            * * *
            * * * *
            * * * * *
        
if the no of stars are increasing from top to down :

n = 5
for i in range (1 ,n+1,1):
    for j in range (1 ,i+1,1):
            print("*" ,end ='')
    print()


'''
n = 5
for i in range (1 ,n+1,1):
    for j in range (1 ,n+1,1):
        if j <= i :
            print("*" ,end ='')
    print()

print("\n")
'''
pattern 2 : * *                 1st row = 2   no of stars = i + 1
            * * *               2nd row = 3
            * * * *.            3rd row = 4
            * * * * *           4th row = 5
            * * * * * *.        5th row = 6

for i in range (1, n +1 ,1):
    for j in range( 1 , n+2 ,1):
        if j <= i+1 :
            print("*",end='')
    print()
     
'''
for i in range(1 , n +1 ,1):
    for j in range( 1 ,  i+1+1 ,1):
        print("*",end='')
    print()



'''
pattern 3 : *                  [i=1] 1st row = 1   no.of.stars = row + row.no - 1   
            * * *              [i=2] 2nd row = 3   stars = i + {i - 1}
            * * * * *          [i=3] 3rd row = 5
            * * * * * * *      [i=4] 4th row = 7
            * * * * * * * * *  [i=5] 5th row = 9

for ( int i = 1 ; i <= n ; i++){
    for (int j = 1 ; j <= i+(i-1) ; j++){
        System.out.print("*");
    }
    System.out.println();
}

'''

for i in range( 1 , n+1 , 1):
    for j in range( 1 ,i+(i-1)+1, 1):
        print("* ",end = '')
    print()

'''
pattern 4 : * *                [i=1] 1st row = 2   no.of.stars = row * 2   
            * * * *            [i=2] 2nd row = 4   stars = i * 2
            * * * * * *        [i=3] 3rd row = 6.  {or}
            * * * * * * * *    [i=4] 4th row = 8   no.of.stars = row+row
            * * * * * * * * * *[i=5] 5th row = 10. 

for ( int i = 1 ; i <= n ; i++){
    for (int j = 1 ; j <= i*2 ; j++){
        System.out.print("*");
    }
    System.out.println();
}

'''

for i in range ( 1 , n +1 , 1):
    for j in range ( 1 , i*2 + 1 , 1):
        print("*",end='')
    print()



'''
pattern 5 : * * * * *  1st row = 5.  intrusion : {n-i}+1
            * * * *    2nd row = 4
            * * *      3rd row = 3
            * *        4th row = 2
            *          5th row = 1

for (int i = 1 ; i <= n ; i++){
    for ( int j = 1 ; j < (n-i)+1 ; j++){
        sop("*");
    }
    sop("\n")
}
'''
for i in range(1 , n+1 ,1):
    for j in range( 1 ,(n-i)+1+1, 1):
        print("*",end='')
    print()


'''
pattern 6 : * * * * * * * * *  1st row = 9.  intrusion : {n-i}+{n-i}+1
            * * * * * * *      2nd row = 7
            * * * * *          3rd row = 5
            * * *              4th row = 3
            *                  5th row = 1

for (int i = 1 ; i <= n ; i++){
    for ( int j = 1 ; j < (n-i)+(n-i)+2 ; j++){
        sop("*");
    }
    sop("\n")
}
'''
for i in range(1 , n+1 ,1):
    for j in range( 1 ,(n-i)+(n-i)+1+1, 1):
        print("*",end='')
    print()

'''
pattern 6 : * * * * * * * * * * 1st row = 10  intrusion : {n-i}+{n-i}+2
            * * * * * * * *     2nd row = 8
            * * * * * *         3rd row = 6
            * * * *             4th row = 4
            * *                 5th row = 2

for (int i = 1 ; i <= n ; i++){
    for ( int j = 1 ; j < (n-i)+(n-i)+2 ; j++){
        sop("*");
    }
    sop("\n")
}
'''
for i in range(1 , n+1 ,1):
    for j in range(1, ((n-i)+(n-i)+2)+1 , 1):
        print("*",end='')
    print()