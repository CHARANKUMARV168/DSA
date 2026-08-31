a = "abc"
b = "xyz"
c = ""
i = 0
j = 0
pick = 0
while i < len(a) and j < len(b):
    if pick == 0 :
        c = c+a[i]
        i=i+1
        pick = pick +1

    else:
        c = c+b[j]
        j= j+1  
        pick = 0 


while i < len(a):
    c = c+a[i]
    i = i+1

while j < len(b):
    c = c+b[j]
    j = j+1

print(c)


