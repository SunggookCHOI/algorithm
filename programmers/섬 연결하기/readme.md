<h1>섬 연결하기</h1>
출처 : https://programmers.co.kr/learn/courses/30/lessons/42861  <br><br>

<h3>문제 풀이</h3>
1. 탐욕법으로 풀었다.<br>
2. 연결들을 코스트 기준 오름차순으로 정렬한다.<br>
3. 첫 연결부터 살펴보며, 연결이 연결 해 주는 두 섬 중 하나가 giant component에 있는 경우, 연결을 채택하며 giant component에 연결되어 있지 않은 섬을 연결해 준다. <br>
4. 3의 과정을 giant component에 모든 섬이 들어갈 때까지 반복한다.
