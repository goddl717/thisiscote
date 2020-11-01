def solution(numbers):
    answer = ''
    numbers = sorted(numbers , key = lambda numbers : numbers%10,reverse = True)
    for i in numbers:
        answer += str(i)

    return answer

print(solution([3, 30, 34,5,9]))

