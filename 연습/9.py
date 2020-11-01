#상위 루트를 찾는 것.
def find_parent(a):
    global parent
    while (parent[a] != a):
        a = parent[a]
    
    return parent[a]

#합치는 것
def union (a,b):
    global parent
    a = find_parent(a)
    b = find_parent(b)
    if a >= b :
        parent[b]= a
    else :
        parent[a]= b
    

def solution(n, costs):
    #정렬
    global parent
    parent = [0]*n
    for i in range(n):
        parent[i] = i
        
    edge = sorted(costs,key = lambda x : x[2])
    answer = 0
    
    for i in edge :
        if find_parent(i[0]) != find_parent(i[1]) :
            union(i[0],i[1])
            answer += i[2]
            
    return answer

print(solution(	4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))