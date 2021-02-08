# https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    return r_convert(convert(n,3)[::-1],3)

# 10진수인 n을 base진수로 변환
def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base) # n을 base로 나눈 몫과 나머지를 튜플형태로 반환
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

# base진수인 n을 10진수로 변환
def r_convert(n, base):
    l = len(n)
    ans = 0
    for i, v in enumerate(n):
        ans += int(n[i])*pow(base,l-i-1)
        print(ans)
    return ans
