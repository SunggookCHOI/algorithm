import sys
n,m,v = map(int,sys.stdin.readline().split())

edge = []
for i in range(m):
    edge.append(list(map(int,sys.stdin.readline().split())))

 
def bfs():
    visit = [0 for i in range(n+1)]
    visit[0] = 1
    visitNum = 0
    answer = ""
    queue = [v]
    while visitNum != n and len(queue) != 0: 
        target = queue.pop(0)
        if visit[target] == 0 :
            visit[target] = 1
            visitNum += 1
            answer += str(target)+" "
            queue.extend(getNeighbor(target))
    if visitNum ==1 : print(answer)
    else : print(answer[:-1])

def dfs():
    visit = [0 for i in range(n+1)]
    visit[0] = 1
    visitNum = 0
    answer = ""
    queue = [v]
    while visitNum != n and len(queue) != 0: 
        target = queue.pop(0)
        if visit[target] == 0 :
            visit[target] = 1
            visitNum += 1
            answer += str(target)+" "
            nei = getNeighbor(target)
            nei.extend(queue)
            queue = nei
    if visitNum ==1 : print(answer)
    else : print(answer[:-1])
    
def getNeighbor(target):
    nei=[]
    for e in edge:
        if e[0]==target:
            nei.append(e[1])
        elif e[1] ==target:
            nei.append(e[0])
    return sorted(nei)
dfs()
bfs()
