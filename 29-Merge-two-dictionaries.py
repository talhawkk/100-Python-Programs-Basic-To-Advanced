# How to Merge Two Dictionaries?
#solution one
dict1={"ali" : 44, "hamza": 23}
dict2={"ahmad" : 24, "talha": 88, "hamza":93}
print(dict1 | dict2)

#solution two
print({**dict1,**dict2})

#solution three (copy update method)
dict3=dict2.copy()
dict3.update(dict1)
print(dict3)