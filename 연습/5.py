from itertools import combinations
def solution(number, k):
    ret = 0
    answer = ''
    com = list(combinations(number,len(number)-k))
    temp = ''
    print(com)
    for i in range(len(com)) :
        for j in range(len(com[i])) :
            temp += com[i][j]
        print(temp)
        if ret <= int(temp) :
            ret = int(temp)
        temp = ''
    answer = str(ret)
    print(com)
    return answer
print(solution("1924",2))