#https://www.acmicpc.net/problem/11057

n = int(input())
li = [1] * 10
for _ in range(n-1):
    tmp = [sum(li[:i+1])%10007 for i in range(10)]
    li = tmp.copy()
print(sum(li)%10007)
