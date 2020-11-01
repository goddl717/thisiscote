#알파벳이 들어왓을 때 최소값을 반환하는 함수.
def find_num(i):
    ret = 0
    a = ord(i) - ord('A')
    b = ord('Z') - ord(i) +1
    ret = min (abs(a),abs(b))
    
    return ret
    

def solution(name):
    answer = 0
    temp = ''
    temp2= ''
    temp = list(temp)
    temp2 = list(temp2)    
    for i in range(len(name)):
        temp += 'A'
        temp2 += 'A'
    a = 0
    a += find_num(name[0])
    temp[0] = name[0]
    print(a)

    
    for i in range(0,len(name)):
        if ''.join(temp) == str(name) :
            break
        a +=1
        a += find_num(name[i])
        temp[i] = name[i]
    b = 0
    b += find_num(name[0])
    temp2[0] = name[0]
    for i in range(len(name)-1,0,-1) :
        if ''.join(temp2) == str(name) :
            break
        b +=1
        b += find_num(name[i])
        temp2[i] = name[i]
    
    print(a,b)
    
   
    return min(a,b)

print(solution("BBBAAAB"))#9
print(solution("ABABAAAAABA")) #11