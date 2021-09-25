# https://programmers.co.kr/learn/courses/30/lessons/72411
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        tmp = []
        for order in orders:
            for x in combinations(order, c):
                tmp.append(''.join(sorted(x)))
        # 길이가 c인 조합의 등장 빈도 체크
        counter = Counter(tmp)
        if len(counter.values()):
            # 길이가 c인 조합 중 최대 등장 빈도
            m = max(counter.values())
            if m > 1:
                # 등장 빈도가 최대인 조합들을 answer에 넣는다
                answer += [k for k,v in counter.items() if v==m]
    
    return sorted(answer)
