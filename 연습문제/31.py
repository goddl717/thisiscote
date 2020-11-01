def function(arr) :
    rows = len(arr)
    cols = len(arr[0])
    dp = [[0]*cols for i in range(rows)]
    for i in range(rows):
        dp[i][0] = arr[i][0]
    for j in range(cols-1):
        for i in range(rows):

            dp[i][j+1] = max(dp[i][j+1],dp[i][j] + arr[i][j+1])
            if i-1 >=0 :
                dp[i][j+1] = max(dp[i-1][j+1],dp[i][j] + arr[i-1][j+1])
            if i+1 < rows:
                dp[i][j+1] = max(dp[i+1][j+1],dp[i][j] + arr[i+1][j+1])
    return dp



n = int(input())

for i in range(n) :
    a,b = map(int,input().split())
    temp = list(map(int,input().split()))
    arr = [[0]*b for i in range(a)]

    for i in range(a):

        for j in range(b):
            arr[i][j] = temp[i*b+j]
    ret = function(arr)
    #print(ret)
    print(ret[a-1][b-1])

    
