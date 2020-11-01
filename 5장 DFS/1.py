def dfs (y,x) :
    global visited
    if visited[y][x] == 1:
        return
    visited[y][x] = 1

    for i in range(4):
        nx = x + dir[i][0]
        ny = y + dir[i][1]
        if nx >=0 and nx <m and ny >=0 and ny < n and visited[ny][nx] == 0:
            dfs(ny,nx)
    return



dir = [(-1,0),(1,0),(0,1),(0,-1)]

n,m = map(int,input().split())

arr = []
for i in range(n):
    arr.append(list(map (int,input())))
visited = arr
cnt =0

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 :
            dfs(i,j)
            cnt+=1


print(cnt)





