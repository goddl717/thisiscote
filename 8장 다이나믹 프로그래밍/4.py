n , m =map(int,input().split()) 
arr = []
for i in range(n):
    arr.append(int(input()))
dp= [987654321]*(m+1)
#동전의 종류를 받아서 합이 m이 되는 최소의 동전의 갯수를 구하여라 .
#동전의 종류는 n개

dp[0] = 0
# dp [i] = min (dp[i-1] .....) + 1
for i in range(m+1):
    for j in range(n):
        if i - arr[j] >= 0 and dp[i-arr[j]] != 987654321 :
            dp[i] = min(dp[i],dp[i-arr[j]]) +1

print(dp[m])
# dp[i] = min (dp[i],dp[i-arr[i]])
