<h1>숨바꼭질</h1>
출처 : https://www.acmicpc.net/problem/1697 <br><br>

1. BFS 으로 풀었다. <br>
2. 처음 수빈이의 위치가 3 이라면 수빈이의 n초 후의 가능 위치는 아래와 같다 <br>

시간|위치
---|---
0s|3|
1s|2,4,6
2s|1,3,5,8,7,12
...|...

3. queue 에 3을 넣어준 후, queue가 빌때까지 하나씩 꺼내며 꺼낸 원소+-1 과 2를 곱한 값이 동생의 위치와 다를경우 nextQ에 넣는다. 같다면 그때의 depth를 출력한다. <br>
4. queue가 비었다면 depth(solution.py)에서 answer의 값을 1 더해준 후, 과정 3을 반복한다. <br>
5. queue에 넣을 원소들의 방문여부를 체크하면 코드를 더 효율적으로 짤 수 있다. (예를 들면, 2초에 2를 방문했다면, 2초 이후에는 2를 또 방문할 필요가 없다. 해당 원소는 최적해가 될 수 없다.)
