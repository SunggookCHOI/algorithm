#https://hellya.tistory.com/101
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

''' 더 효율적인 코드 추가
from collections import deque

class Num():
    def __init__(self, base):
        self.num = [0]
        self.T = list("0123456789ABCDEF")
        self.base = base
    def add(self):
        self.addOne(1)
    def addOne(self,depth):
        if depth > len(self.num):
            self.num = [1] + self.num
            return ;
        if self.num[-depth] == self.base-1:
            self.num[-depth] = 0
            self.addOne(depth+1)
        else:
            self.num[-depth] += 1
    def getNum(self):
        return [self.T[x] for x in self.num]
    
def solution(n, t, m, p):
    q= deque()
    answer = ''
    
    #말해야할 숫자
    num = Num(n)
    while len(answer) < t:
        
        for s in num.getNum():
            q.append(s)
            
        while len(q) > m:
            answer+= q[p-1]
            for _ in range(m):
                q.popleft()
        num.add()
    return answer
'''
