# factors of a no : a is a fcator of b if it divides the no completely with remainder 0 
n = 10 
# ffoctor of n are in range 1  - 10 
fact = []
for i in range(1, n+1 , 1):
    if n%i == 0 :
        fact.append(i)
print(fact)