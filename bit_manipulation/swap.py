a = 5 
b = 10 

a = a ^ b #(a = 5 ^ 10)
print(a)
b = a ^ b #(a ^ b ^ b) => b ^ b = 0 : a
print(b)
a = a ^ b  # a ^ b 
print(a)   #(a^b)^(a)