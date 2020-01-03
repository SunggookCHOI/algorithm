<h1>수 찾기</h1>
출처 : https://www.acmicpc.net/problem/1920 <br><br>

1. 정렬 후 이분탐색을 활용한다. <br>
2. 이분탐색을 활용하기 위해 target을 정렬한다.<br>
3. numbers 안의 값들을 하나씩 꺼내며 target에 대하여 이분탐색한다.<br>

** 효율성 문제
```
for number in numbers:
    if number in target:
        print(1)
    else:
        print(0)
```
과 같이 풀면 if 문도 for 문이 되어 효율성 면에서 좋지 않은 코드가 된다.
