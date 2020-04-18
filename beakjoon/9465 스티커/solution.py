import sys
s=[[50, 10, 100, 20, 40],
[30, 50, 70, 10, 60]]
def solution(s):
  dp = [[s[i][0]] + [0]*(len(s[0])-1) for i in range(2)]
  dp[0][1] = dp[1][0]+s[0][1]
  dp[1][1] = dp[0][0]+s[1][1]
  for i in range(2,len(s[0])):
    dp[0][i] = max(dp[0][i-2],dp[1][i-2],dp[1][i-1])+s[0][i]
    dp[1][i] = max(dp[1][i-2],dp[0][i-2],dp[0][i-1])+s[1][i]
  print(max(dp[0][-1],dp[1][-1]))

if __name__=="__main__":
  n = int(input())
  for _ in range(n):
    size = int(input())
    s = []
    for i in range(2):
      s.append(list(map(int,sys.stdin.readline().split())))
    solution(s)
