# https://programmers.co.kr/learn/courses/30/lessons/17680#qna
from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0 : return len(cities) * 5
    answer = 5
    cache = deque([cities[0].upper()])
    for city in cities[1:]:
        c = city.upper()
        if c in cache:
            answer +=1
            cache.remove(c)
            cache.append(c)
        else:
            answer += 5
            cache.append(c)
            if len(cache) > cacheSize:
                cache.popleft()
    
    return answer
