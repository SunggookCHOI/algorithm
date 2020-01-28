def solution(n):
    dp = [0,1,2]
    if n<3:
        return dp[n]
    for i in range(3,n+1):
        dp.append((dp[-1]+dp[-2])%1234567)
    return dp[-1]
