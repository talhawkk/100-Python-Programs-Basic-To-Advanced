#Python itrators with Function:
l=[23,35,34,23]
iterate=iter(l)
print(iterate.__next__())
print(iterate.__next__())
print(iterate.__next__())
print(iterate.__next__())



# class Fantastic_five:
#     def __init__(self):
#         self.num=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.num<=5:
#             value=self.num
#             self.num+=1
#             return value
#         else:
#             raise StopIteration

# FF=Fantastic_five()
# for i in FF:
#     print(i)