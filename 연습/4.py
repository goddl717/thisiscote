def solution(n, lost, reserve):
    answer = 0
    arr = [1] * (n+1)
    for i in lost :
        arr[i] = 0
    for i in reserve :
        arr[i] = 2
    
    for i in range(1,n):
        if arr[i] == 0 and arr[i-1] ==2 and arr[i+1] ==0:
            arr[i] = 1
            arr[i-1] = 1

        if arr[i] == 0 and arr[i-1] ==0 and arr[i+1] ==2:
            arr[i+1] = 1
            arr[i] = 1

    for i in range(1,n):
        if arr[i] == 2 and arr[i+1] == 0:
            arr[i] = 1
            arr[i+1] = 1

    for i in range(2,n+1):
        if arr[i] == 2 and arr[i-1] == 0:
            arr[i] = 1
            arr[i-1] = 1    
    

    for i in range(1,n):
        if arr[i] == 2 and  arr[i+1] ==0 :
            arr[i] =  1
            arr[i+1] =1 
    
    print(arr)

    for i in range(len(arr)): 
        if arr[i] >=1 :
            answer +=1

    return answer

solution(5	,[2, 4]	,[1, 3, 5])
solution(5	,[2, 4],	[3])
solution(3	,[3],	[1])