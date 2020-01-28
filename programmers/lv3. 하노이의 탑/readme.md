# 하노이의 탑
출처 : https://programmers.co.kr/learn/courses/30/lessons/12946 <br><br>

1. 재귀함수를 이용하여 풀었다. <br>
2. move(n, poll1, poll2) 는 n개의 원판을 poll1에서 poll2로 옮기는 함수이며, 이를 위해서는 <br>
> 2-1. n-1개를 poll1과 poll2가 아닌 다른 기둥(poll3)으로 옮긴다. move(n-1, poll1,poll3) <br>
> 2-2. 남은 가장 큰 원판 한개를 poll1에서 poll2로 옮긴다. move(1, poll1, poll2) <br>
> 2-3. 2-1에서 옮긴 n-1개를 poll3에서 poll2로 옮긴다 move(n-1, poll3, poll2) <br>
