# set을 사용해도 되는데 과연 시간초과는 ??

def binary_search (arr1,value,start,end):
    if start > end :
        return 'no'
    else :
        mid = (start+end)//2
        if arr1[mid] == value:
            return 'yes'
        elif arr1[mid] > value:
            return binary_search(arr1,value,start,mid-1)
        elif arr1[mid] < value:
            return binary_search(arr1,value,mid+1,end)


import sys
n = int(input())
arr1 = list(map (int,sys.stdin.readline().rstrip().split()))
m = int(input())
arr2 = list(map(int,sys.stdin.readline().split()))

for i in range(len(arr2)):
    print (binary_search(arr1,arr2[i],0,n-1) , end = ' ') 



