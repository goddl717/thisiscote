# 90도를 가진 것을 만들기.
def make_4case (key):
    ret = [] 
    temp2= []
    for j in range(len(key)):
        temp1= []
        for i in range(len(key)-1,-1,-1):   
            temp1.append(key[i][j])
        temp2.append(temp1)  
    return temp2 

def part(key,arr,sy,sx):
    M = len(key)
    N = len(arr) - 2*M
    answer = True

    for i in range (M) :
        for j in range(M) :
            arr[i+sy][j+sx] += key[i][j]
    
    for i in range(M,N+M) :
        for j in range(M,M+N):
            if arr[i][j] != 1:
                answer = False 
    
    for i in range (M) :
        for j in range(M) :
            arr[i+sy][j+sx] -= key[i][j]
                
            
    return answer
def check(key,arr) :
    M = len(key)
    N = len(arr) - 2*M
    # M만큼 움직이면서 arr를 갱신 시킨다. 그리고 중간값에서 확인을 한다.
    # 확인을 해서 중간이 모두 1이면 True 를 리턴 아니면 false 를 리턴 한다.
    for i in range(0,N+M) :
        for j in range(0,M+N):
            if part(key,arr,i,j) == True :
                return True
            
            
    return False

    
            
            
        

def solution(key, lock):
    N = len(lock)
    M = len(key)
    case4 = []
    answer = True
    global arr
    arr = [[0]*(N + 2*M)for i in range( (N + 2*M))]
    
    
    for i in range(M,M+N) :
        for j in range(M,M+N) :
            arr[i][j] = lock[i-M][j-M]
    
    
    print(arr)    
    print(key)
    
    for i in range(4):
        temp = make_4case(key)
        case4.append(temp)
        key = temp
    #4가지 case에 대해서 모두 만듬.
    
    print(case4)
    for i in range(4):
        if check(case4[i],arr) == True :
            return True
    
    

    return False

print(solution ([[0,0,0],[1,0,0],[0,1,1]],[[1,1,1],[1,1,0],[1,0,1]]))