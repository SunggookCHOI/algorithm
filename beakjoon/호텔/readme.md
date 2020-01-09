<h1> 호텔 </h1>
출처 : https://www.acmicpc.net/problem/1106 <br><br>

1. Dynamic programming 으로 풀었다. <br>
2. 먼저 dictionary에 고객의 수를 key로 그때의 비용을 value로 담는다. key가 중복될 경우 비용이 더 작은 값을 value로 취한다. (더 효율적이니까)<br>
3. 고객을 i명 늘렸을 때의 최소 비용 dp[i]을 점화식으로 쓰면 아래와 같다.<br>
> 각 k (key; 사람 수) ,v (value; 비용)에 대하여 <br>
> dp[i] = min(dp[i - k] + v) , given (k,v) in dictionary <br>
> (k와 v가 주어졌을 때 ( i명 늘렸을때의 비용) = (i-k 명 늘렸을 때의 비용) + ( k 명 늘리는 주어진 비용 ) <br>
4. 마지막으로 i 명보다 많이 받았을 때가 i명 받았을때보다 싸지는 경우가 있으므로 i명을 목표명수 까지가 아니라 목표명수 + k의 최댓값( 가장 큰 단위 )까지 해주면 된다.
