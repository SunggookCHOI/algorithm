<h1>여행경로</h1>
출처 : https://programmers.co.kr/learn/courses/30/lessons/43164 <br><br>

1. dfs <br>
2. 모든 항공권을 사용할 수 있는 경우를 구하며, 여러개가 가능한 경우 알파벳 순으로 첫번째 것만 반환하는 문제이다. <br>
3. dfs로 가며 티켓을 모두 사용한 경우, 전역 변수로 지정해 놓은 answer와 맨 앞의 것 부터 순서대로 알파벳 순으로 비교하며 더 작은 경우 답으로 채택(cmp 함수)한다.<br>
4. path.copy()에 주의한다. 그냥 path를 넘겨줄 경우 path에 실패한 경로들이 계속 쌓임으로 path의 복사본을 넘겨 주어야한다.
