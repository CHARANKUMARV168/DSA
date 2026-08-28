# comparing triplets 
a = [ 5, 6 ,7]
b = [ 3 ,6 ,10]
a_score = 0
b_score = 0
if len(a) == len(b) :
    for i in range(len(a)):
        if a[i] > b[i]:
            a_score = a_score +1 
        if b[i] > a[i]:
            b_score = b_score +1 
print(a_score,b_score)