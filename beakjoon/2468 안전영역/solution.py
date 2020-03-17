import collections,sys

def bfs(r,c):
    q=collections.deque()
    q.append((r,c))
    while q:
        r,c = q.popleft()
        if r>0 and visit[r-1][c] == 0:
            q.append((r-1,c))
            visit[r-1][c]=1
        if r<n-1 and visit[r+1][c] == 0:
            q.append((r+1,c))
            visit[r+1][c] = 1
        if c>0 and visit[r][c-1] == 0 :
            q.append((r,c-1))
            visit[r][c-1] = 1
        if c<n-1 and visit[r][c+1] == 0:
            q.append((r,c+1))
            visit[r][c+1] = 1

def getArea(height):
    global visit
    visit = [[0 if maps[r][c] > height else 1 for c in range(n)] for r in range(n)]
    area = 0
    for r in range(n):
        for c in range(n):
            #print(r,c)
            if visit[r][c] == 0 :
                bfs(r,c)
                area+=1
    return area

def solution(maps,maxHeight):
    ans = 0
    for i in range(maxHeight):
        temp = getArea(i)
        if temp > ans:
            ans = temp 
    print(ans)

if __name__=="__main__":
    n = int(sys.stdin.readline())
    maps = []
    maxHeight = 0
    for _ in range(n):
        temp = list(map(int,sys.stdin.readline().split()))
        tempMax = max(temp)
        maps.append(temp)
        if tempMax>maxHeight:
            maxHeight = tempMax 
    solution(maps,maxHeight)
