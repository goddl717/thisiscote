# 천번째로 못생긴 수의 갯은 어떻게 되겠냐 ?
# 1,2,3,2*2,5,2*3
# 못생긴 수의 1000째 값은 과연 어느정도일까 ?
# 최대값을 예상해 볼 수 있나 ?


import sys

n = int(sys.stdin.readline())
check = [0]*100000

i = 1
check[1] = 1
j = 0
while ( i < n) :
    if check[j//5] ==1 or check[j//2] ==1 or check[j//3] ==1 :
        check[j] = 1
        i+=1
    j+=1

print(j-1)

