# 11399 ATM
출처 : https://www.acmicpc.net/problem/11399 <br><br>

1. 그리디 <br>
2. 6 line처럼 i번째 손님의 업무를 처리하는데 걸리는 시간은 sum(p[:i])+p[i] 또는 sum(p[:i+1]) 이므로, 이를 줄이려면 p를 오름차순으로 정렬한 후 수행하면 된다.
