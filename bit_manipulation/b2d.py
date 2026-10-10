# convertion of binary to decimal 

no = 1001 
s = str(no)
l = list(s)
print(l)
lim = len(l)
sum = 0
for i in range(lim-1,-1,-1):
  sum = sum + (int(l[i])*(2**i))
print(sum)