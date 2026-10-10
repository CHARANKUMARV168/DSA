# decimal to binary convertion 
# method 1 :
num = 10 
res = []
while num != 0 :
    res.append(num%2)
    num = num // 2
res.reverse()
print(res)

# 2 method : bin(num)
x = 10
print(bin(10))

# 3rd method : 
y = 10 
b = formar(y,'b')
print(b)