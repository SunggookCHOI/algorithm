# https://www.acmicpc.net/problem/1149

import sys
readline = sys.stdin.readline

def main(n):
    dp = list(map(int,readline().split()))
    for _ in range(n-1):
        r,g,b = map(int,readline().split())
        dp = [min(dp[1],dp[2])+r, min(dp[0],dp[2])+g,min(dp[0],dp[1])+b]
    print(min(dp))
if __name__ == '__main__':
    n =int(readline())
    main(n)
