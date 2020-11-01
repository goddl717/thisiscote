n = int(input())
arr = list (map (int, input().split()))
# dp 점화식을 어떻게 세울까 ??

# 점화식은 어떻게 세울까 생각을 해보자.
# dp [i] = max (dp[i-1],arr[i] + dp[i-2])
# 왜 (i-3)은 취급하지 않아도 되는가 ?
#
dp = [0] * n
dp[0] = arr[0]
dp[1] = max(arr[0],arr[1])
#두는 경우와 안두는 경우중 큰 것을 가져간다.

for i in range(2,n):
    dp[i] = max (dp[i-1], arr[i] + dp[i-2])

print(dp[n-1])

 