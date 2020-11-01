def binary_search(arr1,value,start,end):
    if start > end :
        return None
    mid = (start + end)//2
    sum = 0 
    #여기가 헷갈린다.
    
    for i in range(mid,len(arr1)):
        sum += arr1[i] - arr1[mid]

    if sum == value :
        return arr1[mid]
    elif sum > value :
        return binary_search(arr1,value,start,mid-1)
    elif sum < value :
        return binary_search(arr1,value,mid+1,end)
    



import sys
n,m = map (int, input().split())

arr = list(map(int,sys.stdin.readline().rstrip().split()))
arr.sort()
print(binary_search(arr,m,0,n-1))

#니가 이진탐색 문제라고 ?
