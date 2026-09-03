#  01 Frequency hashmap : the first hashmap 


# hash map is a combination of key and value 
# and each key is unique 
# keyword to create a hashmap in python : dict = {} i.e, var_name = { key , value }

# syntax for creation
h = {}

# insertion : based on index value 
# hash_var[index_val] = "value"
# where index_val is the key 
h[1] = "charan"
h[2] = "adi"
h[3] = "advith"
h[4] = "adam"
h[5] = "arya"
# retrival process happens only through key value 
print(h[1])
print(type(h))

# updation is done through the same index method 
# if we use the same key with diff value the key value is updated with most recenetly updated value and the older one is removed 

h[1] = "t-rex"
print(h[1])

# to display all the key value of the dict i.e, hashmap
# syntax : h_var.keys()
print(h.keys())

# to display all the values of the dict i.e, hashmap 
# syntax : h_var.values()
print(h.values())

# to check if key is present in hashmap :
# key_var in h.keys()
# use in operator to check if the key is present or not 
print(1 in h.keys()) 

# to check if the value is present in the hashmap 
# val in h.values()
print("charan" in h.values())
print("t-rex" in h.values())

print("iterating using for loop over hashmap keys")
for i in h.keys():
    print(h[i])

# i acess the keys 
# h[i] to access the values