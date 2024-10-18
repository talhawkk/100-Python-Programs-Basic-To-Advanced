#Concatenate Two List 
l1=[23,25,24,224]
l2=[35,74,74,432]
print(l1+l2)
#or
l1.extend(l2)
print(l1)
#or
l3=list(set(l1+l2))
print(l3)