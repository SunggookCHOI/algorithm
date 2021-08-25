# https://programmers.co.kr/learn/courses/30/lessons/84325
def solution(table, languages, preference):
    # 동점시 알파벳 순으로 빠른 것을 리턴해야하므로 정렬되어있어야한다.
    answer = 	['CONTENTS', 'GAME', 'HARDWARE', 'PORTAL', 'SI']
    # dic['직군']['언어']=점수
    dic={}
    for t in table:
        x=t.split()
        tmp={}
        for i in range(5):
            tmp[x[i+1]]=5-i
        dic[x[0]]=tmp
    # 직군별 점수 합계
    a=[(sum(dic[a][l]*p if l in dic[a] else 0 for l, p in zip(languages, preference))) for a in answer]
    
    return answer[a.index(max(a))]
