#https://programmers.co.kr/learn/courses/30/lessons/1844
import collections
def solution(maps):
    n,m=len(maps), len(maps[0])
    global answer
    answer = 99999
    global chk
    #0이면 방문, 1이며 미방문
    chk = [[1 for i in range(m)] for j in range(n)]
    chk[0][0]=1
    return bfs(0,0,n-1,m-1,1,maps)


def bfs(i,j,n,m,lv, maps):
    #(i,j,lv)
    q=collections.deque([(0,0,1)])
    while q:
        i,j,lv=q.popleft()
        if i==n and j==m:
            return lv
        if i+1<=n and maps[i+1][j]==1 and chk[i+1][j]:
            chk[i+1][j]=0
            q.append((i+1,j,lv+1))
        if i-1>=0 and maps[i-1][j]==1 and chk[i-1][j]:
            chk[i-1][j]=0
            q.append((i-1,j,lv+1))
        if j+1<=m and maps[i][j+1]==1 and chk[i][j+1]:
            chk[i][j+1]=0
            q.append((i,j+1,lv+1))
        if j-1>=0 and maps[i][j-1]==1 and chk[i][j-1]:
            chk[i][j-1]=0
            q.append((i,j-1,lv+1))
    return -1
  
  
''' 처음에 dfs로 시도했다가 시간초과 난 풀이
def solution(maps):
    n,m=len(maps), len(maps[0])
    global answer
    answer = 99999
    global chk
    chk = [[99999 for i in range(m)] for j in range(n)]
    chk[0][0]=1
    dfs(0,0,n-1,m-1,1,maps)
    return -1 if answer==99999 else answer

def dfs(i,j,n,m,lv, maps):
    #print(i,j,n,m)
    if i==n and j==m:
        global answer
        if answer > lv: answer=lv
        return ;
    if i+1<=n and maps[i+1][j]==1 and chk[i+1][j]>lv:
        chk[i+1][j]=lv
        dfs(i+1,j,n,m,lv+1,maps)
    if i-1>=0 and maps[i-1][j]==1 and chk[i-1][j]>lv:
        chk[i-1][j]=lv
        dfs(i-1,j,n,m,lv+1,maps)
    if j+1<=m and maps[i][j+1]==1 and chk[i][j+1]>lv:
        chk[i][j+1]=lv
        dfs(i,j+1,n,m,lv+1,maps)
    if j-1>=0 and maps[i][j-1]==1 and chk[i][j-1]>lv:
        chk[i][j-1]=lv
        dfs(i,j-1,n,m,lv+1,maps)
'''
