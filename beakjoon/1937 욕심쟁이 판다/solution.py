import sys
sys.setrecursionlimit(40000)

n=int(sys.stdin.readline())
maps=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

lifes = [[0 for i in range(n)] for j in range(n)]

def getLife(i,j):
    if lifes[j][i] != 0:
        return lifes[j][i]
    nomi = []
    if j>0 and maps[j-1][i] > maps[j][i]:
        nomi.append(getLife(i,j-1)+1)
    if j < n-1 and maps[j+1][i] > maps[j][i]:
        nomi.append(getLife(i,j+1)+1)
    if i>0 and maps[j][i-1] > maps[j][i]:
        nomi.append(getLife(i-1,j)+1)
    if i < n-1 and maps[j][i+1] > maps[j][i]:
        nomi.append(getLife(i+1,j)+1)
    if len(nomi) == 0:
        lifes[j][i] = 1
    else :
        lifes[j][i] = max(nomi)
    return lifes[j][i]

ans = 0
for j in range(n):
    for i in range(n):
        temp = getLife(i,j)
        if temp > ans : 
            ans = temp
print(ans)
