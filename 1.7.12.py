a = [[7,8,9],
     [4 ,2,6],
     [6 ,8,4]]
b = [[3,6,1],
     [2,2,3],
     [5,5,6]]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range(len(a)):
    for j in range(len(a[i])):
                   result[i][j]=a[i][j]+b[i][j]

for k in result:
                   print(k)
            
                   

