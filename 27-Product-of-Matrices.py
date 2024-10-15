
#product of matrixes:
A=[
    [23,34,23],
    [2,5,55],
    [5,34,23]
]
B=[
    [24,54,3],
    [45,63,34],
    [35,64,2]
]
R=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            R[i][j]+=A[i][k]*B[k][j]


# print(R)
for i in R:
    for j in i:
        print(j, end=" ")
    print("\n")