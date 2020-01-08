<h1>토마토</h1>
출처 : https://www.acmicpc.net/problem/7576 <br><br>

1. BFS를 이용했다. <br>
2. queue 때문에 아주 고생했다.<br>
## 내장함수의 자료구조 별 시간복잡도

|내장함수|시간복잡도|
|------|---|
|list.pop(0)|O(n)|
|collections.deque().popleft()|O(1)|
|queue.Queue().get()|???|

list의 경우 0번을 빼면 인덱스 i를 i-1로 전부 당겨줘야하기 때문에 시간복잡도가 n이 된다. <br>
반면 collections.deque의 경우는 LinkedList로 만들어져있는것 같다.<br>
queue.Queue()로 할 경우도 시간초과가 뜬다. 내부적으로 어떻게 구현되어있는지 간단히 찾아보았는데 안나온다...

** Queue의 경우, 멀티쓰레드 시스템에서 Thread-safe한 자료구조를 제공하기 위한 모듈로, 일반적인 경우에는 deque가 20배 이상 빠르다고 한다. (deque의 경우, 내가 꺼내고 있는데 다른 쓰레드에서 꺼낼 경우 런타임 에러가 난다고 한다.)
