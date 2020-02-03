dp=[ 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
def sol(n):
    if n-1 < len(dp):
        return dp[n-1]
    for _ in range(len(dp),n):
        dp.append(dp[-1]+dp[-5])
    return dp[n-1]

i = int(input())
for _ in range(i):
    print(sol(int(input())))
