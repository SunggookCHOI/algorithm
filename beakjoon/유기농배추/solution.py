import collections
import sys

t= int(input())
for _ in range(t):
    m,n,k = map(int,sys.stdin.readline().split())
    visit = [[False for i in range(m)] for j in range(n)]
    cabbage = [[0 for i in range(m)] for j in range(n)]
    cab = collections.deque()
    for _num in range(k):
        c,r = map(int,sys.stdin.readline().split())
        cabbage[r][c]=1
        cab.append([r,c])
    
    answer = 0
    while cab:
        row,col = cab.popleft()
        if visit[row][col] == False:
            answer +=1
            visit[row][col]= True
            q=collections.deque()
            q.append([row,col])
            while q:
                r,c = q.popleft()
                if r>0 and visit[r-1][c]==False and cabbage[r-1][c]==1:
                    q.append([r-1,c])
                    visit[r-1][c]=True
                if r<n-1 and visit[r+1][c]==False and cabbage[r+1][c]==1:
                    q.append([r+1,c])
                    visit[r+1][c]=True
                if c>0 and visit[r][c-1]==False and cabbage[r][c-1]==1:
                    q.append([r,c-1])
                    visit[r][c-1]=True
                if c<m-1 and visit[r][c+1]==False and cabbage[r][c+1]==1:
                    q.append([r,c+1])
                    visit[r][c+1]=True
    print(answer)
