#문제는 내림차순이 되게하는데 최대의 병사들이 남게 만든다.
#sys는 적용 완료.

import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
dp = [1] * n

#내림 차순이 적용 되게 설계를 한다..

# a ... b ... c a > b > c 이게 깨지면 빼면 되는거 아닌가 ?
sum =0
print(arr)

for i in range(n):
    for j in range(0,i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(dp)
print(n - dp[n-1])





