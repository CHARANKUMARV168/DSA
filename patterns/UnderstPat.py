
'''
for i in range(1 , n+1 ,1):
    y = 5
    for j in range(1 , i+1 , 1):
        print(y,end='')
        y = y-1
    print()

print()
'''
y = 1
n = 5 
for i in range( 1 ,n+1,1):
    x = 5
    for j in range(1 ,i+1,1):
        print(x,end='')
        x= x-1
    print()

'''
pattern 2 :    

    1
   121
  12321
 1234321
123454321

'''
n = 5
for i in range(1 ,n+1 ,1):
    
    for j in range( 1, (n-i)+1,1):
        print(" " ,end='')
    x=1
    for k in range(1 , i+1,1):
        print(x,end='')
        x= x+1
    a=i-1
    for l in range(1 ,(i-1)+1,1):
        print(a,end='')
        a =a-1
    print()

'''

pattern 3 : 

    1
   212
  32123
 4321234
543212345
'''
n = 5
for i in range(1 ,n+1,1):
    for j in range(1,(n-i)+1,1):
        print(" ",end='')
    
    a = i 
    for k in range( 1, i+1,1):
        print(a,end='')
        a= a-1

    b = 2
    for l in range(1, (i-1)+1,1):
        print(b,end='')
        b=b+1
    
    print()

'''
>> when we try printing the var which is defined outside the loop and incr/dec inside the loop we get continous values in a pattern 
>> when the var is decalreed inside the loop and decremented/ incremented inside only the same value is printed in a row and decremnented/increased row wise

pattern :

111111111
122222221
123333321
123444321
123454321
123444321
123333321
122222221
111111111

'''
for i in range (1 , n+1,1):
    a=1
    for j in range(1 ,(i-1)+1,1):
        print(a,end='')
        a+1
    b = i
    for k in range(1 ,((n-i)+(n-i)+1)+1,1):
        print(i,end='')
    c = i-1
    for l in range(1 ,(i-1)+1 ,1):
        print(c,end='')
    print()


n = 4
for i in range(1 ,n+1 ,1):
    x = 1
    for j in range( 1, (n-i)+1,1):
        print(x ,end='')
        x= x+1
    
    for k in range( 1 ,(i+i+1)+1,1):
        y = n-i+1
        print(y,end='')
        y=y-1
   
    z = n-i
    for l in range( 1, (n-i)+1, 1):
        print(z,end='')
        z=z-1
    
    print()