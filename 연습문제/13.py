from collections import deque
from itertools import combinations

#하나의 값에서 치킨집으로 가는 최소값.

def bfs(visited,arr,y,x) :
    dir = [(-1,0),(1,0),(0,1),(0,-1)]
    q = deque([])
    q.append((y,x))
    visited[y][x] = 1
    while q :
        cy = q[0][0]
        cx = q[0][1]

        q.popleft()
        for i in range(4):
            ny = cy + dir[i][0]
            nx = cx + dir[i][1]
            if (nx >=0 and nx < N and ny >=0 and ny < N and visited[ny][nx] == 0) :
                q.append((ny,nx))
                visited[ny][nx] = visited[cy][cx]+1
                if arr[ny][nx] == 2 :
                    return visited[ny][nx]-1

        




N, M = map(int,input().split())

arr = []
for i in range(N) :
    arr.append(list(map(int,input().split())))
min2 = 987654321

chicken = []
home = []
arr2 = [[0]*N for i in range(N)]
visited = [[0]*N for i in range(N)]


for i in range(N) :
    for j in range(N) :
        if arr[i][j] == 2:
            chicken.append((i,j))
            arr[i][j] = 0
        if arr[i][j] == 1:
            home.append((i,j))

temp = (list(combinations(chicken,M)))

for i in home :
    arr2[i[0]][i[1]] = 1

for i in temp :
    sum1 = 0
    for j in range(len(i)):
        arr2[i[j][0]][i[j][1]] = 2
    
    for k in range(len(home)):
        sum1 += bfs(visited,arr2,home[k][0],home[k][1])
        visited = [[0]*N for i in range(N)]

    for j in range(len(i)):
        arr2[i[j][0]][i[j][1]] = 0

    min2 = min (min2,sum1)




#1. arr2를 만든다. 1은 초기화.
# -> 값을 반복적으로 구한다.

#2. arr2에 2를 초기화 시킨다.
#3. bfs를 돌려서 값을 구한다.
#4. arr2를 다시 0으로 바꾼다.




print(min2)


print("asdf")


