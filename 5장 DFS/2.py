from  collections import deque


n,m = map ( int, input().split())


arr = []
dir = [(-1,0),(1,0),(0,1),(0,-1)]
#괴물이 있는 부분은 1이고 없는 부분은 0이다.
visited = [[0]*m for _ in range(n)]

for i in range(n):
    arr.append(list(map(int,input())))


print(arr)

print(visited)

visited[0][0] = 1
q = deque()
q.append([0,0])
while q :
    y,x = q.popleft()

    for i in range(4) :
        ny = y + dir[i][0]
        nx = x + dir[i][1]
        if ny >=0 and ny < n and nx >=0 and nx < m and visited[ny][nx] == 0 and arr[ny][nx] == 1:
            visited[ny][nx] = visited[y][x]+1
            q.append([ny,nx])

#print(visited)
#print()
print(visited[n-1][m-1])

         
    







