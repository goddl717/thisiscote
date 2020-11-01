import sys

vertex,edge = map(int,sys.stdin.readline().rstrip().split())
start = int(sys.stdin.readline().rstrip())


dp = [987654321] * (vertex+1)
visited = [False]* (vertex+1)

adj = [[] for _ in range(vertex+1)]


for i in range(edge):
    a,b,weight = map(int,sys.stdin.readline().rstrip().split())
    adj[a].append((b,weight))

print(adj)

dp[start] = 0
#visited[start] = True
#최소값을 찾는다. (갱신되지 않은 노드중에서)
#최소값과 연결된 간선을 초기화 한다.
#다시 최소값을 찾는다.
#visited 갱신은 모든 갱신이 이루어지고 나서 행한다.
#  
# 탈출 조건은 모든 간선이 True가 되면 ?

while(True):
    #가장 가장은 노드 번호 찾기.
    
    min1 = 987654321
    index = -1
    for i in range(1,vertex+1):
        if visited[i] == False and min1 > dp[i] :
            index = i
    if index == -1 :
        break
    else :
        for i in range(len(adj[index])):
            if dp[adj[index][i][0]] > dp[index] + adj[index][i][1] :
                dp[adj[index][i][0]] = dp[index] + adj[index][i][1]
        # for j in adj[index]:
            #if dp[j[0]] > dp[index] + j[1]
        visited[index] = True 
print(dp)

