n = int(input())
edge = int(input())

arr = [[987654321 for _ in range( n+1)] for _ in range(n+1)]

#print(arr)

for i in range(edge):
    a,b,c = map(int,input().split())
    arr[a][b] = c

for i in range(1,n+1):
    arr[i][i] = 0


for i in range (1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if i != j and i != k and j != k :
                arr[j][k] = min (arr[j][k],arr[j][i] + arr[i][k])
        
print('-------------------------------')
for i in range(1,n+1):
    for j in range(1,n+1):
        print(arr[i][j],end=' ')
    print()
