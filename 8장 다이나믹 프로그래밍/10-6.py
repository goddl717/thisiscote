from collections import deque



#in degree 판단.
# 0인 것들을 큐에 넣는다.
# 큐를 빼면서 연결된 간선을 지운다.
# 0인 것들을 큐에 넣는다.
vertex,edge = map(int,input().split())
indegree = [0] * (vertex+1)

#인디그리 갱신.
for i in range(edge):
    a,b = map(int,input().split())
    indegree[b] += 1

q = deque([])
for i in indegree:
    if i == 0 :
        q.append(i)
     
while q :
    for i in indegree:
        if i == 0 :
            q.append(i)

