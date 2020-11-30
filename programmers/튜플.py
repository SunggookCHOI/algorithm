#문제 : https://programmers.co.kr/learn/courses/30/lessons/64065#

def solution(s):
    s = s[2:-2]
    co = {}
    for tuple in s.split('},{') :
        for t in tuple.split(','):
            tmp = int(t)
            if tmp in co:
                co[tmp] = co[tmp] + 1
            else:
                co[tmp] = 1
    return sorted(list(co.keys()), key = lambda x : co[x], reverse = True)
