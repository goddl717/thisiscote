n = int(input())

arr = list(input().split())

x=1
y=1
# x,y = 1,1 

# 1. arr 만큼
# 2. 4가지 방향에 대해서 맞다면 ?

for direction in arr:
    if direction == 'R':
        if x+1 <= n:
            x = x+1
    elif direction == 'L':
        if x-1 <= 1:
            x = x-1
    elif direction == 'U':
        if y-1 >= 1:
            y = y-1
    elif direction == 'D':
        if y+1 <= n:
            y = y+1

print(y,x)
