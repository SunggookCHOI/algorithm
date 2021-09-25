# https://programmers.co.kr/learn/courses/30/lessons/86051
def solution(numbers):
    answer = 0
    num = [i for i in range(10)]
    
    for n in num:
        if n not in numbers:
            answer += n
        else:
            numbers.remove(n)
    return answer

def solution2(numbers):
    return sum(n for n in range(10) if n not in numbers)
