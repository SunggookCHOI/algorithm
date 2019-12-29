<h1>평범한 배낭</h1>
출처 : https://www.acmicpc.net/problem/12865 <br><br>

1. Dynamic programming으로 knapsack이라는 유명한 문제이다. (주어진 무게 하에 최대 가치를 갖도록 고르는 문제) <br>
2. dp[i][j]는 i번째 짐에서 최대 무게가 j일 때 가질수 있는 최대 가치이다. <br>
i번째 짐의 무게가 j보다 작은 경우 선택할 수 있는 수는 아래와 같다. <br>
> 1. i번째 짐을 챙긴다 => dp[i][j] = dp[i-1][j-w[i]]+v[i]
> 2. i번재 짐을 포기한다 => dp[i][j] = dp[i-1][j]
3. 따라서 위의 두 경우 중 더 큰값을 dp[i][j]로 취한다. <br>

** 어려웠던 점<br>
아래 코드는 계속 시간초과로 실패했던 코드이다.

```
for i in range(1,n):
    for j in range(1,k+1):
        dp[i][j]=dp[i-1][j]
        if j>=w[i]:
            dp[i][j]=max(dp[i][j],dp[i-1][j-w[i]]+v[i])
print(dp[-1][-1])
```

즉, 3번째 줄을 else 문으로 처리하지 않고 위와 같이 하는 경우, 불필요한 연산이 한번 더 일어난다고 할 수 있다.
