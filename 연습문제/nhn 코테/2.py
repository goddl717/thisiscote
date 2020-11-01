#nhn 코테 리뷰.

import sys
H,W = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))



sum1 = 0

for i in range(1,W-1):
    #i번째 이전까지의 배열
    left = arr[:i]
    #i+1번째 부터의 배열
    right = arr[i+1:]
    if min (max(left),max(right)) - arr[i] >=0 :

        sum1 += min (max(left),max(right)) - arr[i]

print(sum1)


