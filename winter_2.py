def solution(encrypted_text, key, rotation):
    answer = ''
    #1. 암호화된 문자를 이용해서 원래의 값을 찾는다.
    #1. 알파벳을 변경한다. 더한다.
    #2. 자리를 바꾼다. 변경한다.
    
    temp = ['']*len(key)
    ret = ['']*len(key)
    
    #로테이션.
    for i in range(len(key)):
        temp[(i-rotation)%len(key)] = encrypted_text[i%len(key)]
    
    print(ord('y'))
    print(ord('a'))
    
    
    for i in range(len(key)):
        value = ord (temp[i]) - ord(key[i]) + ord('a')-1 
        if value < 97 :
            value += 26
        ret[i] = value

        print(value,end= " ")
        print(chr(value))
        

        #print(chr(ord (temp[i]) - ord(key[i]) + ord('a')-1 ))
    
    
    #for i in range(len(encrypted_text))
    #1.숫자로 자리를 바꾼다.
    #로테이션을 한다.
    
    
    
    return ret

print (solution("qyyigoptvfb",	"abcdefghijk"	,3))