#부모의 인덱스를 반환하는 함수.

def find_parent (vertex):
    global p
    while p[vertex] != vertex:
        vertex = p [vertex] 
    return vertex 


def union (a,b):
    global p
    a = find_parent(a)
    b = find_parent(b)
    if a > b : 
        p[a] = b
    else :
        p[b] = a

        


vertex, edge = map (int, input().split())

p = [i for i in range(vertex+1)]
print(p)
adj = [[]for _ in range(vertex+1)]
arr_edge = []

for i in range(edge):
    a,b,c = map(int,input().split())
    arr_edge.append((c,a,b))
    
    
#arr_edge.reverse()    
#union(a,b)

arr_edge.sort()
ret = 0 
for i in arr_edge :
    #1연결
    #만약 같은 집합이라면? 부모가 같다면 연결시키지말고 넘어감
    if find_parent(i[1]) == find_parent(i[2]):
        continue
    else :
        union(i[1],i[2])
        ret += int(i[0])

print(arr_edge)
print(p)
print(ret)
