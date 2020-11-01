import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr = [[100001]*(n+1) for i in range(n+1)]




for i in range(m) :
    a,b,weight = map(int,sys.stdin.readline().split())
    if arr[a][b] > weight :
        arr[a][b] = weight

for i in range(1,n+1) :
    for j in range(1,n+1) :
        if i == j :
            arr[i][j] = 0

'''
for i in range(1,n+1) :
    for j in range(1,n+1) :
        print(arr[i][j],end = ' ')
    print()
'''
for c in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1) :
            arr[a][b] = min (arr[a][c] + arr[c][b] , arr[a][b])

for i in range(1,n+1) :
    for j in range(1,n+1) :
        print(arr[i][j],end = ' ')
    print()
    