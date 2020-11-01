#동전을 사용하는 경우와 사용하지 않는 경우가 있을 수 있다.
#그러면 전체 경우의 수는 2^1000 쓴다 안쓴다. 이런 식으로는 풀면 안된다.

# 만들수 있는지 없는지를 판별해보자.


a,b = map (int,input().split())
arr = list(map(int,input().split()))

arr.sort()
ret = 0

for i in range(len(arr)) :
    for j in range(i+1,len(arr)):
        if arr[i] < arr[j] :
            ret +=1
print(ret)

