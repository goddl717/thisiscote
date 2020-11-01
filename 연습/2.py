def solution(answers):
    # 가장 많은 점수를 가진 사람을 뽑는다.
    person1 = [1,2,3,4,5]*2000
    person2 = [2,1,2,3,2,4,2,5]*1250
    person3 = [3,3,1,1,2,2,4,4,5,5] * 2000
    ret1 = 0
    ret2 = 0
    ret3 = 0
   
    ret = []
    temp = []
    for i in range(len(answers)) :
        if answers[i] == person1[i] :
            ret1 +=1
        if answers[i] == person2[i] :
            ret2 +=1
        if answers[i] == person3[i] :
            ret3 +=1
    temp.append(ret1)
    temp.append(ret2)
    temp.append(ret3)

    for i in range(len(temp)):
        if max(temp) == temp[i] :
            ret.append(i+1)

    
    
    return ret

print(solution([1,2,3,4,5]))