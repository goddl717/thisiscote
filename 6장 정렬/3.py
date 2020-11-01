def func(data):
    return data[1]


n = int(input())

arr = []
for i in range(n):
    name,score = input().split()
    arr.append((name,int(score)))

print(arr)

# 람다는 함수다.@
# lambda y,x : x+y 
# map 에서도 사용 가능 .

arr = sorted(arr,key = lambda data: data[1])

for i in range(len(arr)):
    print(arr[i][0], end = ' ')
