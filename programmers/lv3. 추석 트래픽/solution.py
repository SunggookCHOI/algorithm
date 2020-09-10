import datetime
from collections import deque

def solution(lines):
    answer = 0
    traffics = []
    
    for l in lines:
        date, time, t = l.split()
        tmp_date = list(map(int,date.split("-")))
        tmp_time = time.split(":")
        sec, msec = tmp_time[2].split('.')
        end = datetime.datetime(tmp_date[0],tmp_date[1],tmp_date[2],int(tmp_time[0]),int(tmp_time[1]),int(sec),int(float("0."+msec)*1000000))
        start = end - datetime.timedelta(seconds = float(t[:-1])) + datetime.timedelta(seconds = 0.001)
        
        traffics.append((start,end + datetime.timedelta(seconds = 1)))
    #기준 시간    
    for start, end in traffics:
        count_start = 0
        count_end = 0
        for s,e in traffics:
            if s < start <= e :
                count_start += 1
            if s < end <= e :
                count_end += 1
        if max(count_start,count_end) > answer :
            answer = max(count_start,count_end)
        
    return answer
