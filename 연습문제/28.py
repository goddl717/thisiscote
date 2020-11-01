n = int(input())


arr =(list(map(int,input().split())))

def binary_search1(arr,start,end) :
    
    mid = (start + end)//2 
    if start > end :
        return -1
    if arr[mid] == mid :
        print(mid)
        return mid
    if arr[mid] > mid :
        return binary_search1(arr,start,mid-1)
    if arr[mid] < mid :
        return binary_search1(arr,mid+1,end)
    
    


print(binary_search1(arr,0,len(arr)-1))




