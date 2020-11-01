from collections import deque

def cango (a,b):
    ret = 0
    for i in range(len(a)):
        if a[i] == b[i] :
            ret +=1        
    if ret == len(a) - 1:
        return True
    else :
        return False
    
def solution(begin, target, words):
    dic = {}
    for i in words :
        dic[i] = False
    
    q = deque([])
    q.append((begin,0))
    
    while q :
        temp= q.pop()
        if temp[0] == target :
            return temp[1]
        for i in words:
            if dic[i] == False and cango(temp[0],i)== True:
                dic[i] = True
                q.append((i,temp[1]+1))
                

    return 0

print(solution("hit"	,"cog"	,["hot", "dot", "dog", "lot", "log", "cog"]))