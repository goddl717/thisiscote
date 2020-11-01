n = int(input())
arr = list(map(int,input().split()))
yoen = list(map(int,input().split()))

#이거 하긴 했는데..
min1 = 987654321
max1 = -987654321


def dfs(cnt,yoen,value,arr) :
    global min1
    global max1
    if cnt == n-1 :
        min1 = min(min1,value)
        max1 = max(max1,value)     
        return 
    else :
        #여기서 수를 정하는데,
        if yoen[0] > 0 :
            yoen[0] -=1
            dfs(cnt+1,yoen,value+arr[cnt+1],arr)
            yoen[0] +=1

        if yoen[1] > 0 :
            yoen[1] -=1
            dfs(cnt+1,yoen,value-arr[cnt+1],arr)
            yoen[1] +=1

        if yoen[2] > 0 :
            yoen[2] -=1
            dfs(cnt+1,yoen,value*arr[cnt+1],arr)
            yoen[2] +=1

        if yoen[3] > 0 :
            yoen[3] -=1
            if value < 0 :
                value *= -1
                value = value // arr[cnt+1]
                value *= -1
                dfs(cnt+1,yoen,value,arr)
            else :
                dfs(cnt+1,yoen,value//arr[cnt+1],arr)
            
            yoen[3] +=1
    return

dfs(0,yoen,arr[0],arr)
print(max1)
print(min1)


