import sys
def solution():
    dp[0][0] = 1
    for r in range(n):
        for c in range(n):
            l = maps[r][c]
            if l == 0 or dp[r][c] == 0 :
                continue
            new_r = r+l
            new_c = c+l
            if new_r < n:
                dp[new_r][c] += dp[r][c]
            if new_c < n:
                dp[r][new_c] += dp[r][c]
    print(dp[n-1][n-1])
if __name__=="__main__":
    n = int(sys.stdin.readline())
    maps = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    dp=[[0 for i in range(n)] for j in range(n)]
    solution()
