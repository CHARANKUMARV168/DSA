a = [ 10 ,20 , 30 ,40 ,50 ,60 ,70]
i = 0 
j = 0 
k = 3 
k = k - 1
while j <= k :
  print(f"a[j] at pos {j} :",a[j])
  j = j +1 
  
print("after loop value of a[j]",a[j])
# j = j - 1 
while j <= len(a)-1 :
  i = i + 1
  # j = j + 1
  print("a[i] and a[j] :",a[i], a[j])
  j = j + 1