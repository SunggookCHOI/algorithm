import math

dp = [0,1]
n=int(input())

for i in range(2,n+1):
    dp.append(min(dp[i-(j**2)]+1 for j in range(1,int(math.sqrt(i))+1)))
print(dp[-1])
