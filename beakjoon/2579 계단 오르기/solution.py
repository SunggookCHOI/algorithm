import sys
n = int(sys.stdin.readline())
s = [0 for i in range(n)]
dp = [0 for i in range(n)]

for i in range(min(3,n)):
    s[i]=int(sys.stdin.readline())
if n>3:
    dp[0]=s[0]
    dp[1]=s[0]+s[1]
    dp[2]=max(s[0]+s[2],s[1]+s[2])
    for i in range(3,n):
        s[i] = int(sys.stdin.readline())
        dp[i]=max(dp[i-2]+s[i],dp[i-3]+s[i-1]+s[i])
elif n==3:
    dp=[s[0],s[0]+s[1],max(s[0]+s[2],s[1]+s[2])]
else:
    dp=[sum(s)]
print(dp[-1])
