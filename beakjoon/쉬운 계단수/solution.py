n= int(input())
dp=[0,1,1,1,1,1,1,1,1,1]
if n==1: print(9)
else:
    for i in range(n-1):
        temp = []
        for j in range(10):
            if j==0:
                temp.append(dp[1])
            elif j==9:
                temp.append(dp[8])
            else :
                temp.append(dp[j-1]+dp[j+1])
        dp=temp
    print(sum(dp)%1000000000)
