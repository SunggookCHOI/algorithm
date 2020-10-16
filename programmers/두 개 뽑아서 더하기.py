def solution(numbers):
    answer = []
    for i,v in enumerate(numbers):
        for j,w in enumerate(numbers[i+1:]):
            answer.append(w+v)
    return sorted(list(set(answer)))
