
def solution(number, k):
    number = list(number) 
    temp = []
    i = 0
    t = k
    while k > 0 and i < len(number):
        if len(temp) == 0:
            temp.append(number[i])
            i+=1
            
        while k > 0 and len(temp) > i and number[i] > temp[len(temp)-1] :
            temp.pop()
            k-=1
        temp.append(number[i])
        i+=1

    print(temp)
    for j in range(i,len(number)):
        temp.append (number[j])

    ret = temp[0:len(number)-t]
   
    return ''.join(ret)

print(solution("987654321",8 ))