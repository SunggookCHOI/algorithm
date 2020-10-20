import sys
sys.setrecursionlimit(10000)
# 0: 상, 1: 좌, 2: 하, 3: 우
a = [0,-1,0,1]
b = [-1,0,1,0]
def dfs(x,y):
    if dp[y][x] == -1 : 
        dp[y][x] = 0
    if x<0 or x>n-1 or y<0 or y>m-1: return 0
    for i in range(4):
        nx = x + a[i]
        ny = y + b[i]
        if (0 <= nx <= n-1 and 0 <= ny <= m-1) and maps[ny][nx] > maps[y][x] :
            if dp[ny][nx] > 0:
                dp[y][x] += dp[ny][nx]
            # 방문한 적 없으면 dfs
            elif dp[ny][nx] == -1 :
                dp[y][x] += dfs(nx,ny)
    return dp[y][x]
        
if __name__ == '__main__':
    m,n = map(int,sys.stdin.readline().split())
    maps = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

    dp = [[-1] * n for _ in range(m)]
    dp[0][0] = 1
    dfs(n-1,m-1) 
    print(dp[-1][-1])
