def solution(record):
    answer = []
    # d['id'] = nickname
    d = dict()
    tmp = []
    for r in record:
        s = r.split()
        if s[0]=='Enter':
            d[s[1]]=s[2]
            tmp.append(s[:2])
        elif s[0]=='Leave':
            tmp.append(s[:2])
        else :
            d[s[1]]=s[2]
    #print(tmp)
    for t in tmp:
        answer.append(d[t[1]]+'님이 들어왔습니다.' if t[0]=='Enter'
                        else d[t[1]]+'님이 나갔습니다.')
    
    return answer
