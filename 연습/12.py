from collections import deque
    
def solution(N, number):
    
    
    
    
    q= deque([])
    q.append((N,0))
    dic = {}
    while q :
        temp = q.popleft()
        if temp[1] >= 8 :
            return -1
        if temp[0] == number :
            return temp[1]
        #없으면 큐에 넣는다.
        if temp[0]*N not in dic :
            dic[temp[0]*N] = temp[1]
            q.append((temp[0] *N,temp[1]+1))
        #있으면 그냥 지나간다.      
        if temp[0]-N not in dic :
            dic[temp[0]-N] = temp[1]
            q.append((temp[0] -N,temp[1]+1))
        if temp[0]//N not in dic :
            dic[temp[0]//N] = temp[1]
            q.append((temp[0]//N,temp[1]+1))        
        if temp[0]+N not in dic :
            dic[temp[0]+N] = temp[1]
            q.append((temp[0]+N,temp[1]+1))        
                   
    answer = 0
    return -1
print(solution(5,12))