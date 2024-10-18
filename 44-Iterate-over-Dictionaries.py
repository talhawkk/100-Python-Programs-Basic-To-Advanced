#iterate over dictionaries
dict={"talha":"ab","hamza":"h","ali":"Ahmad","jaaz":"ab"}
for key,index in dict.items():
    print(key,index)
print("\n")
#another methode:
for key in dict:
    print(key,dict[key])