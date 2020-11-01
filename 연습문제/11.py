from collections import deque

n = int(input())
k = int(input())

arr = [[0]*(n) for i in range(n)]
dir = [(0,1),(1,0),(0,-1),(-1,0)]
dir_s = 0

#1이 사과


for i in range(k) :
    y ,x = map(int,input().split())
    arr[y-1][x-1] = 1

l = int(input())

times = []
for i in range(l) :
    temp = []
    a,b = input().split()
    a = int(a)
    times.append((a,b))

snake = deque([(0,0)])
cnt = 0 
t_in = 0

# time 처리는 어떻게 해야할까 ?

while True :
    y, x = snake[0]
    ny = y + dir[dir_s][0]
    nx = x + dir[dir_s][1]


    #벗어나면 출력
    if ny >= n or ny < 0 or nx >= n or nx < 0 :
        print (cnt+1)
        break
    #자기를 만나면 출력.

    if (ny,nx) in snake :
        print(cnt+1)
        break
    
    if arr[ny][nx] == 1:
        snake.appendleft((ny,nx))
        arr[ny][nx] = 0
    else :
        snake.appendleft((ny,nx))
        snake.pop()
    
    cnt +=1
    if t_in < len(times) and  cnt == times[t_in][0]:
        if times[t_in][1] == 'D' :
            dir_s += 1 
            dir_s = dir_s %4
        else :
            dir_s -=1 
            dir_s = dir_s %4
        t_in +=1
      
        
        

    
    
    


    



