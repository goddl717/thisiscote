n = int( input())
arr = []

for i in range(n):
    arr.append(int(input()))

arr.sort()
arr.reverse()
# 기본 정렬 함수를 사용하고, 인자로 reverse를 True를 만들어 준다.

# array = sorted(array,reverse = Ture)

print(arr)


