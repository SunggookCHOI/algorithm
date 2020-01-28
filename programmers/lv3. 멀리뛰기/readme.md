# 멀리 뛰기
출처 : https://programmers.co.kr/learn/courses/30/lessons/12914 <br><br>

1. dp로 풀었다. <br>
2. n번으로 오는 방법은 n-1에서 1칸 뛰는 방법과 n-2에서 2칸 뛰는 방법이 있으므로 이를 점화식으로 나타내면 아래와 같다. <br>
> dp[n] = dp[n-1]+dp[n-2] <br><br>

* 사실 그냥 피보나치 수열이다.

