n = int(input())
arr=(list(map(int,input().split())))

sum1 = 0
for i in range(n):
    sum1 += arr[i]

avg = sum1//n

index = -1
min1 = 987654321
for i in range(n):
    if min1 > abs(arr[i]-avg) :
        min1 = abs(arr[i]-avg)
        index = i

print(arr[index])
