from collections import deque

n,m,k,x = map (int,input().split())
adj = [[]for i in range(n+1)]
visited = [0]*(n+1)

for i in range(m):
    a,b = map(int,input().split())
    adj[a].append(b)

visited[x] = 0
q = deque([])
q.append(x)

while q :
    now = q[0]
    q.popleft()
    for i in range(len(adj[now])):
        if visited[adj[now][i]] == 0:
            visited[adj[now][i]] = visited[now] +1
            q.append(adj[now][i])

print(visited)
ret = []

for i in range(len(visited)) :
    if  visited[i] == k :
        ret.append(i)

if ret == [] :
    print("-1")
else :
    for i in range(len(ret)):
        print(ret[i])
        

