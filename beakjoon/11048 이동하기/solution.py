import sys
n,m = map(int,sys.stdin.readline().split())
dp = list(map(int,sys.stdin.readline().split()))
for j in range(1,m):
    dp[j] = dp[j-1]+dp[j]
for i in range(1,n):
    maze = list(map(int,sys.stdin.readline().split()))
    dp[0]+=maze[0]
    for j in range(1,m):
        dp[j] = max(dp[j-1]+maze[j],dp[j]+maze[j])
print(dp[-1])
