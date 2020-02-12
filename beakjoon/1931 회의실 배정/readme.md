# 1931 회의실 배정
출처 : https://www.acmicpc.net/problem/1931 <br><br>

1. 그리디 <br>
2. 빨리 끝나는 회의부터 처리하되, 끝나는 시간이 같을 경우, 빨리 시작하는 회의부터 처리함으로써 (5,8),(8,8) 과 같은 데이터가 들어왔을 경우, 두 회의 모두 
진행될 수 있도록 한다. <br>
3. 재미있는 것은 2번의 조건에 맞게 정렬을 하는 과정에서 <br>
3-1.
```
times.sort()
times.sort(key=lambda x: x[1])
```
3-2.
```
from functools import cmp_to_key

def compare(x, y):
    if x[1] < y[1] :
        return -1 
    elif x[1] > y[1] :
        return 1
    else: 
        if x[0] < y[0] :
            return -1
        else:
            return 1
times.sort(key=cmp_to_key(compare))
```
두가지 방법을 사용해 보았는데, 내장함수로 2번 정렬하는 것이 훨씬 효율적이었다.<br>
>3-1. 메모리 44944kb, 시간	328ms, 3-2. 메모리 50360kb, 시간	552ms
