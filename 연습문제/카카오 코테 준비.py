from collections import deque
from itertools import permutations


def solution(n, weak, dist):
    
    #1. 취약 지점을 이용해서 최약지역을 확인하는 데이터 셋을 만들자.
    len_weak = len(weak)
    for i in range(len_weak) :
        weak.append(weak[i]+n)

    for per in permutations(dist):
       
        for start in range(len_weak):
            count = 0
            value = weak[start]
            for i in range(start,start+len_weak) :
                count +=1 
                value += 



    
    
    
    
    
    
    answer = 0
    return answer

solution(12,[1,5,6,10],[1,2,3,4])
