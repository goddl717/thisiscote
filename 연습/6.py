#알파벳이 들어왓을 때 최소값을 반환하는 함수.
def find_num(i):
    ret = 0
    a = ord(i) - ord('A')
    b = ord('Z') - ord(i) +1
    ret = min (a,b)
    
    return ret
    

def solution(name):
    answer = 0
    temp = ''
    for i in range(len(name)):
        temp += 'A'
    
    for i in range(len(name)):
        if temp == name :
            break
        temp = list(temp)
        answer +=1
        answer += find_num(name[i])
        temp[i] = name[i]
        temp = str(temp)
        
    
    return answer

print(solution("JAN"))
