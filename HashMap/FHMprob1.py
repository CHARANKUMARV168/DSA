# write a program to print one or all the occureneces in a array

a = [10,20,30,10,20,20,10,10,30,20,10,20,30]
h = {}

for key in a:
    if key not in h.keys() :
        h[key] = 1
    else :
        value = h[key]
        value = value +1 
        h[key] = value

print(h)
