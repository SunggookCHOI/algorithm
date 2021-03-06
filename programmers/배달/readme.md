<h1>배달</h1>
출처 : https://programmers.co.kr/learn/courses/30/lessons/12978  <br><br>

<h3>문제 요약</h3>
1 ~ N 노드가 있을 때, 1에서부터 거리가 K 이하인 마을의 개수를 반환한다. <br><br>

<h3>문제 풀이</h3>
1. 1번 노드부터 모든 노드까지의 최단경로를 찾는 문제로, 다익스트라 알고리즘(Dijkstra algorithm)을 활용했다.<br>
2. 기본적으로 BFS를 활용하는데, 해당노드를 방문했는지 아닌지를 체크하지 않고, 여태까지 도달하는데 사용된 코스트의 최솟값을 체크해둔다. 
즉, 1번 노드로부터 가까운 노드들부터 탐사하는데, 방문했던 노드라도 코스트가 더 적게 든다면 다시 방문한다.
3. 더이상 탐사할 곳이 없을 경우(queue가 비는 경우), 탐사를 멈추며, 그때 기록된 거리들이 1번 노드로 부터의 최단 경로이므로, 거리가 K 이하인 노드의 수를 반환한다.
