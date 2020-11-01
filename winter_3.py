import copy
def dfs(y,x):
    # dfs는 간단해서 ..... 안적으셔도 아시겠죠 ?ㅎㅎ
    global visited
    global n
    global arr
    global cnt1
    global cnt2
    global cnt3
    dir = [(-1,0),(1,0),(0,1),(0,-1)]
    
    visited[y][x] = 1

    for i in range(4):
        ny = y + dir[i][0]
        nx = x + dir[i][1]
        if ny < n and ny >= 0 and nx  < n and nx >= 0 and visited[ny][nx] == 0 and arr[ny][nx] == arr[y][x]: 
            dfs(ny,nx)
    return

              
                
def solution(v):
    global cnt1
    global cnt2
    global cnt3
    global n
    global visited
    global arr

    n = len(v)
    # 혹시 몰라서 딥카피 써봣습니다.
    arr = copy.deepcopy(v)
    # visited 0 으로 다 갱신
    visited = [[0]*n for i in range(n)]
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    
    for i in range(n) :
        for j in range(n):
            # 들어갈수 있으면 dfs를 돌리고 
            # dfs 에서 visited를 갱신한 1로
            # 처음에 들어가면서 cnt1,2,3의 값을 추가시킴.
            if visited[i][j] == 0 :
                
                dfs(i,j)
                if arr[i][j] == 0 :
                    cnt1 +=1
                elif arr[i][j] == 1:
                    cnt2 +=1
                else :
                    cnt3 +=1
                    
    # 다 돌고 나서 
    print(cnt1,cnt2,cnt3)
    answer = []
    answer.append(cnt1)
    answer.append(cnt2)
    answer.append(cnt3)

    
    
   
    return answer


print(solution ([[0,0,1,1],[1,1,1,1],[2,2,2,1],[0,0,0,2]]))

