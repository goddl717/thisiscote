def find_min (food_times) :
    min1 =100000001
    index = -1
    for i in range(len(food_times)) :
        if food_times[i] == 0:
            continue 
        if min1 > food_times[i] :
            index = i
            min1 = food_times[i]
    
    return [min1,index]
        
def find_notzero (food_times) :
    ret = 0
    for i in range(len(food_times)):
        if food_times[i] >0 :
            ret +=1
    return ret

        
def solution(food_times, k):
    current = 0
    while True :
        #최소값을 찾고
        #최소값 * 몇개
        temp_min,temp_index = find_min(food_times)
        multin = find_notzero(food_times)
        # 다음 값이 k
        if current + temp_min * multin > k :
            break
        else :
            for i in range(len(food_times)) :
                if food_times[i] > 0 :
                    food_times[i] -= temp_min
            current += temp_min*multin
    
    
    for i in range(len(food_times)):
        if current == k :
            return i+1
        if food_times[i] == 0:
            continue
        else : 
            current +=1 
        
    return -1
            
        
print(solution([3, 1, 2],	5))

    
    
    