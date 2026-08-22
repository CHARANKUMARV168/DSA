'''
the first pattern is : *****
                       *****
                       *****
                       *****
                       *****

each row has five stars and each column has also 5 stars the simplest first pattern 
n : no of rows = 5 
m : no of columns = 5 
'''
n = 5 
for i in range (1, n + 1 ,1) :         # changing row is the resposibility of i
    for j in range (1, n + 1 ,1) :     # printing stars is the responsiblity of j
        print("*",end = '')
    print(" ")
'''
pattern 2 : 1 1 1 1 1
            2 2 2 2 2 
            3 3 3 3 3 
            4 4 4 4 4
            5 5 5 5 5
'''
for i in range (1, n + 1 ,1) :         # changing row is the resposibility of i
    for j in range (1, n + 1 ,1) :     # printing stars is the responsiblity of j
        print(f"{i}",end = '')
    print(" ")

'''
pattern 3 : 1 2 3 4 5
            1 2 3 4 5 
            1 2 3 4 5 
            1 2 3 4 5 
            1 2 3 4 5 

'''
for i in range(1 ,6 ,1):
    for j in range(1 ,6 ,1):
        print(j ,end='')
    print(" ")
