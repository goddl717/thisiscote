#정렬을 해서 가장 앞의 값에서의 최대값을 구한다.
n,m = map(int,input().split())

arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))

print(arr)
ret = 0
for i in range(n):
    arr[i].sort()

#arr의 min을 이용하자.


for i in range(n):
    if arr[i][0] >= ret:
        ret = arr[i][0]


print(ret)

