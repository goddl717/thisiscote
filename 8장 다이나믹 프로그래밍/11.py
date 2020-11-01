import heapq

def solution(scoville, K):
    answer = 0
    #
    
    q = []
    for i in range(len(scoville)):
        
        heapq.heappush(q,scoville[i])
    i=0    
    while q :
        a = heapq.heappop (q)
        b = heapq.heappop (q)
        heapq.heappush(q,a + 2*b) 
        print(q)
        i+=1
        if q[0] >= K :
            break
        

    answer = i
    return answer

print(solution([1, 2, 3, 9, 10, 12]	,7))