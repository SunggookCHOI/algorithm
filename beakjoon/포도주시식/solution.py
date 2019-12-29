n = int(input())
cup = []
for i in range(n):
    cup.append(int(input()))


if n==1 : print(cup[0])
elif n==2 : print(sum(cup))
else :
    dp = [cup[0],cup[0]+cup[1],max(cup[0]+cup[2],cup[1]+cup[2],cup[0]+cup[1])]
    for i in range(3,n):
        dp.append(max(dp[i-3]+cup[i-1]+cup[i], dp[i-2]+cup[i], dp[i-1]))
    print(dp[-1])
