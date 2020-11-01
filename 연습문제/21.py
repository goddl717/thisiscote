def check(y,x,arr) :
    global R,L,N

    for i in range(4) :
        ny = y + dir[i][0]
        nx = x + dir[i][1]
        if ny >= 0 and ny < N and nx >=0 and nx < N :
            if (abs (arr[y][x]-arr[ny][nx]) <= R and abs (arr[y][x]-arr[ny][nx]) >= L ):
                sum = arr[y][x] + arr[ny][nx]
                arr[y][x] = sum//2
                arr[ny][nx] = sum//2
                return




N,L,R = map(int,input().split())
arr = []
for i in range(N) :
    arr.append(list(map(int,input().split())))

# 40 40 
# 20 40

# 35 30
# 35 40

#생각 해봐야 하는게. 매트릭스를 돌면서 값을 갱신해야하나 ?

dir = [(-1,0),(1,0),(0,1),(0,-1)]

for i in range(N) :
    for j in range(N) :
        check(i,j,arr)

