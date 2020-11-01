# 0:북쪽, 1 : 동쪽 , 2 : 남쪽, 3: 서쪽
# 0 : 육지, 1: 바다

n,m = map (int, input().split())
arr= []

#순서대로 방향.
#시계방향이면 %연산자를 쓰면 될거같음.

dir =[[-1,0],[0,1],[1,0],[0,-1]]
sy,sx, d = map(int,input().split())
for i in range(n) :
     arr.append(list(map(int,input().split())))

cy,cx = sy,sx 
cnt = 1 
arr[cy][cx] = 1
while(True):
    # 현재 방향을 기준으로 돌아야 한다.
    for i in range(d+1, d+6):
        flag = 0
        ny = cy + dir[i % 4][0]
        nx = cx + dir[i % 4][1]
        #갈 수 있으면
        if ny >=0 and ny < m and nx >= 0 and nx < n and arr[ny][nx] == 0:
            cy = ny
            cx = nx
            arr[ny][nx] = 1
            d = i%4
            flag = 1
            cnt +=1

            break
    
    if flag == 0:
        ny = cy + dir[(d+2)%4][0]
        nx = cx + dir[(d+2)%4][1]
        if (arr[ny][nx] == 0):
            cy = ny
            cx = nx
            cnt +=1
            d = (d+2)%4
        if (arr[ny][nx] ==1):
            print(cnt)
            break


 
    
    




    