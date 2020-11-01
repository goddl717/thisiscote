import sys
import heapq


vertex,edge = map(int,sys.stdin.readline().rstrip().split())
start = int(sys.stdin.readline().rstrip())


dp = [987654321] * (vertex+1)

adj = [[] for _ in range(vertex+1)]


for i in range(edge):
    a,b,weight = map(int,sys.stdin.readline().rstrip().split())
    adj[a].append((weight,b))

print(adj)

q = []
heapq.heappush(q,(0,start))
dp[start] = 0
while q :
    dist,now = heapq.heappop(q)
    #만약에 이전에 값을 갱신해서 값보다 크다면 넘어간다.

    if dist > dp[now] :
        continue
    # 뽑고
    # 
    else :
        for j in adj[now]:
            cost = dp[now] + j[0]
            if cost < dp[j[1]]:
                dp[j[1]] = cost
                heapq.heappush(q,(cost,j[1]))
        
print(dp)


#visited[start] = True
#최소값을 찾는다. (갱신되지 않은 노드중에서)
#최소값과 연결된 간선을 초기화 한다.
#다시 최소값을 찾는다.
#visited 갱신은 모든 갱신이 이루어지고 나서 행한다.
#  
# 탈출 조건은 모든 간선이 True가 되면 ?


