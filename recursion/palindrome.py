s = "malayalam"

def pal(s,l,r):
  if l > r:
    return True

  if s[l] != s[r] :
    return False
    
  return pal(s,l+1,r-1)

x = pal(s,0,len(s)-1)
print(x)