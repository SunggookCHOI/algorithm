def solution(budgets, M):
    answer = sum(budgets)
    if answer<=M:
        return max(budgets)

    top = answer
    bottom = 0
    mid = int((top+bottom)/2)
    while top>bottom:
        
        if calculate(budgets,mid)>M:
            top=mid-1
            mid = int((top+bottom)/2)
        elif calculate(budgets,mid)<M:
            bottom = mid+1
            mid = int((top+bottom)/2)
        elif calculate(budgets,mid)==M:
            return mid
    while calculate(budgets,mid)<M:
        mid+=1
    while calculate(budgets,mid)>M:
        mid-=1
    return mid

def calculate(budgets, maximum):
    answer = 0
    for b in budgets:
        if b<maximum:
            answer+=b
        else :
            answer+=maximum
    return answer
