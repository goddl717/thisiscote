from collections import deque
dir = [(1,0),(-1,0),(0,1),(0,-1)]
n,k = map(int,input().split())
arr = []
for i in  range (n) :
    arr.append(list(map(int,input().split())))

s,y,x = map(int,input().split()) 
visited = [[0]*n for i in range(n)]

q = []
for i in range(n) :
    for j in range(n) :
        if arr[i][j] != 0 :
            q.append((arr[i][j],0,i,j))
            visited[i][j] = 1

q.sort()

q = deque(q)


while q :
    now = q[0]
    if now[1] == s :
        break

    q.popleft()
    for i in range(4) :
        nx = now[3] + dir[i][1]
        ny = now[2] + dir[i][0]
        if nx >=0 and nx < n and ny >= 0 and ny < n and visited[ny][nx] == 0 :
            q.append((now[0],now[1]+1,ny,nx))
            arr[ny][nx] = now[0]
            visited[ny][nx]=1

print(arr[y-1][x-1])       







