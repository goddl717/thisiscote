from bisect import bisect_left,bisect_right 

n ,x = map (int,input().split())
arr = list(map(int,input().split()))

a = bisect_left(arr,x)
b = bisect_right(arr,x)

print(a,b)
if (b == a) :
    print("-1")
else :
    print(b-a)