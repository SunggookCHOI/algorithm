from collections import deque
T = "0123456789ABCDEF"

def convert(n, base):
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(n, t, m, p):
    q= deque()
    answer = ''
    
    #말해야할 숫자
    i = 0
    while len(answer) < t:
        c = convert(i,n)
        
        for s in list(c):
            q.append(s)
            
        while len(q) > m:
            answer+= q[p-1]
            for _ in range(m):
                q.popleft()
        i += 1
    return answer
