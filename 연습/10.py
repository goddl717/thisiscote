def dfs (start,computers,n):
    global visited
    
    
    if visited[start] == False:
        visited[start] = True
        for i in range(n) :
            if computers[start][i] == 1 and start != i and visited[i] == False:
                dfs(i,computers,n)
    else :
        return
    
def solution(n, computers):
    global visited
    answer = 0
    
    visited = [False] * n
    for i in range(n) :
        if visited[i] == False:
            answer +=1
            dfs(i,computers,n)
            
        
    return answer

print(solution(3,	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))