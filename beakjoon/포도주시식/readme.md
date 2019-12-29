<h1>포도주 시식</h1>
출처 : https://www.acmicpc.net/problem/2156 <br><br>

1. 계속해서 Dynamic programming 연습 중이다. <br>
2. i번째 위치에서 먹을 수 있는 경우의 수를 고려해보면
> 1. i-2는 먹지 않고, i-1과 i번째 포도주를 먹는다 => dp[i-3]+cup[i-1]+cup[i]
> 2. i-1을 먹지 않고, i-2와 i번째 포도주를 먹는다 => dp[i-2]+cup[i]
> 3. i번째 포도주를 먹지 않는다 => dp[i-1]
3. 따라서, 위의 세 경우 중 가장 큰 값을 dp에 계속 추가해준 후, dp의 마지막 값을 반환한다.
