def solution(n, stations, w) : 

    answer = 0
    s_range = 2*w+1

    first = stations[0]-w
    if first>1:
        if first%s_range == 0:
            answer += first//s_range
        else:
            answer += first//s_range+1
    for i in range(len(stations)-1):
        gap = (stations[i+1]-w)-(stations[i]+w)-1
        if gap > 0 :
            if gap%s_range == 0:
                answer += gap//s_range
            else:
                answer += gap//s_range+1
    last = stations[-1]+w
    if last<n:
        gap = n-last
        if gap%s_range == 0:
                answer += gap//s_range
        else:
            answer += gap//s_range+1
    return answer
