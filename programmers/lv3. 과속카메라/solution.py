def solution(routes):
    routes.sort(key=lambda e: e[0])
    print(routes)
    answer = 1
    lastCamera = routes[0][1]
    for r in routes:
        if r[0]>lastCamera:
            answer+=1
            lastCamera = r[1]
        else:
            if r[1]<lastCamera:
                lastCamera = r[1]
    return answer
