#https://programmers.co.kr/learn/courses/30/lessons/42890
#https://hellya.tistory.com/134

from itertools import combinations

def solution(relation):
    rows = len(relation)
    cols = len(relation[0])
    keys = []
    
    for n in range(1,cols+1):
        for idxs in combinations(range(cols),n):
            # 최소성 and 유일성
            if min_check(keys,idxs) and \
                    len(set(tuple(relation[row][idx] for idx in idxs) for row in range(rows))) == rows :
                keys.append(idxs)
    
    return len(keys)

#최소성
def min_check(keys, target):
    for k in keys:
        if set(k).issubset(set(target)):
            return False
    return True
