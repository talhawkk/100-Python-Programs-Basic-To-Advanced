#sort a dictionary by value:
dict={"talha":233,"hamza":2323,"ali":232}
#to sort w.r.t keys put 1 to keys, and if sort w.r.t values use 0 in function
sv=sorted(dict.items(), key=lambda x:x[1])
print(sv)
svalues=sorted(dict.values())
print(svalues)