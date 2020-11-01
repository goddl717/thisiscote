n,k = map(int, input().split())

arr1 = list (map (int,input().split()))
arr2 = list(map(int,input().split()))

print(arr1)
print(arr2)

#기억해야하는 건 기본 함수인sorted 의 인자 reverse , key -> 람다식을 이용하거나 함수를 이용한다.

arr1 = sorted(arr1)
arr2 = sorted(arr2,reverse = True)

# 아니면 arr2.sort(reverse= True)거의 비슷하다 .아마 key도 되지 않을까 싶다.


for i in range (k):
    arr1[i],arr2[i] = arr2[i],arr1[i] 


#sum은 내장 함수 sum 을 사용하자 .
# list에서는 통하는 듯 

sum = 0
for i in range(len(arr1)):
    sum += arr1[i]
print(sum)
