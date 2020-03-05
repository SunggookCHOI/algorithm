def solution(n, works):
    if sum(works) <=n: return 0
    works.sort(reverse=True)
    
    non_zero = 0
    for i in range(1,len(works)):
        d = works[i-1]-works[i]
        if d==0:
            continue
        elif d*i<=n:
            for j in range(i):
                works[j] = works[i]
                n-=d
        else :
            non_zero = i
            break
            
    non_zero = len([1 for i in range(len(works)) if works[i] != 0 ]) if non_zero ==0 else non_zero
    assign = n//non_zero
    for i in range(non_zero):
        works[i] -= assign
        n-=assign
    for i in range(n):
        works[i]-=1
    return sum(x**2 for x in works)
