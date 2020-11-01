n = int(input())

arr = []
for i in range(n):  
    arr.append(int(input()))

arr.sort()

sum = arr[0] 
ret = 0

for i in range(1,len(arr)):
    sum += arr[i]
    ret += sum
print(ret)

    

    
#        1                1                   1
# (10 + 20) , (10 + 20 + 40)  (10 + 20 + 40 + 90) 이 최소가 되는 건가?
# 10, 30, 70 
# 1번 생각이 맞는 지 확인 ?
# 
