import collections
import sys


m,n = map(int,sys.stdin.readline().split())
row = 0
tomato = []
ripen=collections.deque()
obstacle_num =0
ripen_num=0
for i in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    for j in range(m):
        if temp[j]==1:
            ripen.append([row+1,j+1])
            ripen_num +=1
        elif temp[j] == -1:
            obstacle_num+=1
    temp.insert(0,-1)
    temp.append(-1)
    tomato.append(temp)
    row+=1

tomato.insert(0, [-1 for i in range(m+2)])
tomato.append([-1 for i in range(m+2)])

answer = -1
while len(ripen) != 0:
    answer+=1
    _num = len(ripen)
    for i in range(_num):
        t = ripen.popleft()
        #print(t)
        if tomato[t[0]+1][t[1]]==0:
            ripen.append([t[0]+1,t[1]])
            tomato[t[0]+1][t[1]]=1
            ripen_num+=1
        if tomato[t[0]-1][t[1]]==0:
            ripen.append([t[0]-1,t[1]])
            tomato[t[0]-1][t[1]]=1
            ripen_num+=1
        if tomato[t[0]][t[1]+1]==0:
            ripen.append([t[0],t[1]+1])
            tomato[t[0]][t[1]+1]=1
            ripen_num+=1
        if tomato[t[0]][t[1]-1]==0:
            ripen.append([t[0],t[1]-1])
            tomato[t[0]][t[1]-1]=1
            ripen_num+=1
if ripen_num+obstacle_num == n*m:
    print(answer)
else:
    print(-1)
