#https://programmers.co.kr/learn/courses/30/lessons/83201
from collections import Counter

def solution(scores):
    answer=''
    for i in range(len(scores)):
        # i가 받은 점수들, tmp[i]는 본인의 점수
        tmp = [scores[j][i] for j in range(len(scores))]
        counter = Counter(tmp)
        mn, mx = min(tmp), max(tmp)
        # 본인의 점수가 유일한 최고/최저값
        if (tmp[i] == mn or tmp[i] == mx) and counter[tmp[i]]==1:
            answer += get_grade((sum(tmp)-tmp[i])/(len(tmp)-1))
        else :
            answer += get_grade(sum(tmp)/len(tmp))
            
    return answer

def get_grade(score):
    if score >= 90:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70<= score < 80:
        return 'C'
    elif 50 <= score < 70:
        return 'D'
    else:
        return 'F'
