n,m,k = map(int,input().split())
print(n,m,k)
#바로 list 로 변경.
arr = list(map(int,input().split()))
print(arr)
arr.sort()

rotate = k * arr[len(arr)-1] + arr[len(arr)-2]

ret = 0 
# 딱 끊어서 더하는 경우.
ret += rotate * (m//(k+1))
# 마지막에 남는 부분을 더하는 경우.
ret += arr[len(arr)-1] * (m%(k+1))

print(ret)




