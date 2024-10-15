#sum of matrices:
A=[[12,2,32],[234,35,46],[22,34,34]]
B=[[45,64,73],[34,75,7],[33,64,6]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j]=A[i][j]+B[i][j]
print(result)
# for i in result:
#     print(i)
#     for j in i:
#         print(j)