import sys
n,m,k = map(int,sys.stdin.readline().split())
air = [[0 for i in range(n+1)] for j in range(n+1)]
#dp[도시][몇번째]
dp = [[0 for i in range(k+1)] for j in range(n+1)]
for _ in range(k):
    a,b,c = map(int,sys.stdin.readline().split())
    air[a][b] = max(air[a][b],c)
for b in range(2, n+1):
    dp[b][2] = air[1][b]
for b in range(2,n+1):
    for i in range(3,m+1):
        try:
            dp[b][i] = max(dp[a][i-1]+air[a][b] for a in range(1,b) if air[a][b] and dp[a][i-1])
        except:
            pass
print(max(dp[n]))
