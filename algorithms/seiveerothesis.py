a = [0 for i in range(101)]
print(a)
a[0] = 1
a[1] = 1
print(a)
for i in range(2,101,1):
  for j in range(i+i,101,i):
    a[j] = 1 
print(a)
for i in range(2,101,1):
  if a[i] == 0 :
    print(i,end=' ')