# set theory :
a = {1,2,3,4,5,6,7,8,9,10}
b = {10,20,30,4,5,6,70,80,9,100}
common = a.intersection(b)
print(common)
uniquea = a - common
print(uniquea)
uniqueb = b - common 
print(uniqueb)

h1 = {}
h2 = {}
h3 = {}
# unique id assigment for elements 
for num in a :
  h1[num] = 1
for num in b :
  if num in a :
    h1[num] = 3 
  else :
    h1[num] = 2
print("h1",h1)
print("h2",h2)
print("h3",h3)


print(a-b)
print(b-a)