def solution(d, budget):
    l = len(d)
    i=0
    d=sorted(d)
    while i-1<l and sum(d[:i+1]) <= budget:
        i += 1
    
    return min(i,l)
