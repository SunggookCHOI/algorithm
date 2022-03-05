#https://programmers.co.kr/learn/courses/30/lessons/67258
#https://hellya.tistory.com/135

def solution(gems):
    tmp = set(gems)
    # 각 보석이 몇 개 있는 지
    c = {}
    for t in tmp:
        c[t] = 0
    # 보석의 종류 수 
    check = 0
    # 보석의 전체 종류
    tot = len(tmp)
    i = 0
    answer = [0,len(gems)]
    for j, item in enumerate(gems):
        if c[item] == 0 : check += 1
        c[item] += 1
        while i < j and c[gems[i]] > 1 :
            c[gems[i]] -= 1
            i += 1
        if check == tot and j-i < answer[1] - answer[0]:
            answer = [i+1,j+1]
    
    return answer
