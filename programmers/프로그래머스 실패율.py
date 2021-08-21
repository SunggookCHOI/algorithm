#https://programmers.co.kr/learn/courses/30/lessons/42889#
from collections import Counter
def solution(N, stages):
    tot=len(stages)
    c=Counter(stages)
    
    # stage i에 도전중인 사람 수
    ing = [c[i] if i in c else 0 for i in range(N+2)]
    #실패율
    f_rate = {}
    for i in range(N+1) :
        # i 단계의 실패율 : i 단계에 도전중인 사람 수 / i 단계 이상에 도전 중인 사람 수
        f_rate[i] = ing[i]/sum(ing[i:]) if sum(ing[i:])>0 else 0
    return sorted([i for i in range(1,N+1)], key=lambda x : f_rate[x], reverse=True)
