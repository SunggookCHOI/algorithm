# 11052 카드 구매하기
출처 : https://www.acmicpc.net/problem/11052 <br><br>

1. dp <br>
2. 카드 i장을 구매하는 비용을 P(i)라 할때, 카드 n장을 구매하는 비용 A(n)의 점화식은 아래와 같다. <br>
> A(n) = A(n-i)+P(i) (A장을 산 금액은 A-i장을 사는데 쓴 금액 + i장 사는 금액)

```
for n in range(1,v+1):
    max_val = dp[-1]
    for i in range(n):
        temp = dp[-i-1]+p[i]
        if temp > max_val:
            max_val = temp
    dp.append(max_val)
```
처음엔 위와 같이 풀었다가 수정했더니 160ms에서 140ms로 줄었다.
