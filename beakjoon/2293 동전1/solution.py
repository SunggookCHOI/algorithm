import sys
n, k = map(int,sys.stdin.readline().split())

coin=[]
for _ in range(n):
    c = int(sys.stdin.readline())
    if c <=k:coin.append(c)
n=len(coin)

dp = [1]+[1 if i%coin[0]==0 else 0 for i in range(1,k+1)]

for i in range(1,n):
    for j in range(coin[i],k+1):
       dp[j] += dp[j-coin[i]]

print(dp[-1])
