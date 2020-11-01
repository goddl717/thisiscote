n = int(input())
arr = []
flag = 0
#n이 6이다 
#전체 모든 경우에 대해서 만들어 봐라는 뜻 ?
#만약에 걸리면 False 를 반환
#안걸리면 True
def monitor(arr,teacher) :
    # S면 통과 X면 못감
    # .
    global n
    dir = [(-1,0),(1,0),(0,1),(0,-1)]
    for i in range(4):
        sx = teacher[1] + dir[i][1]
        sy = teacher[0] + dir[i][0]
        #언제 통과하지 ?
        #S이면 
        while (sx>=0 and sx < n and sy >= 0 and sy < n and arr[sy][sx] != 'O'):
            if arr[sy][sx] == 'S' :
                return False
            sx = sx + dir[i][1]
            sy = sy + dir[i][0]
    return True

        


def check(arr) :
    # 선생의 시야에서 s가 나오면 실패고, 모든 경우에 대해서 통과하면 True
    teachers= []
    global n
    for i in range(n) :
        for j in range(n) :
            if arr[i][j] == 'T':
                teachers.append((i,j))
    for i in range(len(teachers)) :
        if monitor(arr,teachers[i]) == True:
            continue
        else :
            return False 
    return True



def make_obstacle (cnt,arr) :
    global flag
    global n
    if cnt == 3 :
        if flag == 1:
            return 
        #성공을 한번이라도 하면 통과자나.

        if check(arr) == True :
            flag = 1
        return 


    for i in range(n) :
        for j in range(n) :
            if arr[i][j] == 'X' :
                arr[i][j] = 'O'
                make_obstacle(cnt+1,arr)
                arr[i][j] = 'X'
            
for i in range(n) :
    arr.append(input().split())


make_obstacle(0,arr)

if flag == 0:
    print("NO")
else :
    print("YES")



