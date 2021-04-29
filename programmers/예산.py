def solution(d, budget):
    l = len(d)
    i=0
    d=sorted(d)
    while i-1<l and sum(d[:i+1]) <= budget:
        i += 1
    
    return min(i,l)


# sol2
def solution(d, budget):
    if sum(d) <= budget:
        return len(d)
    for i,v in enumerate(sorted(d)):
        if budget >= v :
            budget -= v
        else :
            return i
    
    return i
