#국어는 감소하는 순서로
#국어가 같으면 영어는 증가하는 순서로
#국어와 영어가 같으면 수학은 감소하는 순서로
#모든 순서가 같으면 사전 순으로.

n = int(input())
arr = []
for i  in range(n) :
    name,a,b,c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)

    arr.append((name,a,b,c))

arr = sorted(arr,key = lambda x : x[0])
arr = sorted(arr,key = lambda x : x[3],reverse= True)
arr = sorted(arr,key = lambda x : x[2])
arr = sorted(arr,key = lambda x : x[1], reverse= True)

for i in range(len(arr)):
    print(arr[i][0])
    
