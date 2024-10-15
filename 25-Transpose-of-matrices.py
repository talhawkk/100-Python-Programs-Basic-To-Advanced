#Transpose of a matrix:
A=[
    [12,34,45],
    [56,74,86],
    [23,35,75]
]
T=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
"""a00,a01,a02
   a10,a11,a12
   a20,a21,a22
   

   a00 a10 a20
   a01 a11 a21
   a02 a12 a22
   """
# for i in range(len(A)):
#     for j in range(len(A[0])):
#         print(A[j][i])
for i in range(len(A)):
    for j in range(len(A[0])):
        T[j][i]=A[i][j]
print(T)
