a = [[6,9],
     [5 ,10],
     [15 ,7]]

transpose=[[0,0,0],
           [0,0,0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        transpose[j][i]=a[i][j]

for k in transpose:
    print(k)
