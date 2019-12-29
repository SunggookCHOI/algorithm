import sys

n,k = map(int,sys.stdin.readline().split())
w=[]
v=[]
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    w.append(a)
    v.append(b)    

dp = [[0 for i in range(k+1)] for j in range(n)]
for j in range(k+1):
    if w[0]<=j:dp[0][j]=v[0]

for i in range(1,n):
    for j in range(1,k+1):
        if j>=w[i]:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i]]+v[i])
        else :
            dp[i][j]=dp[i-1][j] 
print(dp[-1][-1])
