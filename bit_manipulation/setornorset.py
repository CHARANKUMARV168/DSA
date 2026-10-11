a = 13
i = 0
no = 1

# using left shift operator 
if ( a & (no << i)) != 0 :
    print("set")
else :
    print("not set")

# using right shift operator :
if ( (a>>i) & no) != 0:
    print("set")
else :
    print("not set")