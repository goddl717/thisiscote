def find_parent (vertex) :
    global p

    while vertex != p[vertex] :
        vertex = p[vertex]
    return vertex



def union(a,b):
    global p
    a = find_parent(a)
    b = find_parent(b)

    if a < b :
        p[b] = a
    else :
        p[a] = b

# 최상위 부모를 찾는 함수.
#         

n,m = map(int,input().split())
p = [i for i in range(n+1)]

for i in range(m):
    a,b,c = map (int,input().split())
    if a == 0 :
        union(b,c)
    elif a == 1:
        if p[b] == p[c]:
            print("yes")
        else :
            print("no")

print(p)
for i in range(len(p)):
    print ( find_parent(p[i]),end = ' ')


    