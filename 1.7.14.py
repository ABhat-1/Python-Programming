a= [[2,3,7],
    [8,9,4],
    [5,6,3]]

b = [[8,10,11],
     [12,14,18],
     [10,15,17]]

mul_res = [[0,0,0],
           [0,0,0],
           [0,0,0]]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            mul_res[i][j]+=a[i][k]*b[k][j]

for k in mul_res:
    print(k)
 
