<h1>쉬운 계단수</h1>
출처 : https://www.acmicpc.net/problem/10844 <br><br>

1. Dynamic programming 으로 풀었다. <br>
2. dp[i]는 현재 depth에서 i로 끝나는 숫자의 개수이다. (0으로 시작하는 숫자는 없다고 했으므로 [0,1,1,1,1,1,1,1,1,1] 로 초기화해준다.<br>
3. temp는 다음 depth에서 i로 끝나는 숫자의 개수이다.
4. i로 끝나는 숫자의 개수의 규칙은 아래와 같다.<br>
> 0으로 끝나는 숫자는 전 depth에서 1로 끝나는 숫자이고, 9로 끝나는 숫자는 전 depth에서 8로 끝나는 숫자이다. 즉, temp[0]=dp[1], temp[9]=dp[8] <br>
> 1 ~ 8은 전 depth에서 각 숫자의 +-1로 끝나는 숫자의 개수의 합이다. 즉, temp[i]=dp[i-1]+dp[i+1]이 된다.
5. dp를 temp로 바꿔준 후, 위의 과정을 반복한다. <br>
